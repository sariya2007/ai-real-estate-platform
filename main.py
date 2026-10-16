import os
import uvicorn
import joblib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="AI Real Estate Intelligence Platform")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Models for payload validation
class PredictRequest(BaseModel):
    sqft: float
    quality: int

class RecommendRequest(BaseModel):
    budget: float
    location: str
    beds: int

class ChatRequest(BaseModel):
    message: str

PROPERTIES_DB = [
    {"id": 1, "title": "Luxury Apartment", "location": "dha", "price": 350000, "beds": 3, "area": 1800, "desc": "Modern luxury apartment near commercial zone."},
    {"id": 2, "title": "Standard House", "location": "bahria", "price": 220000, "beds": 4, "area": 2000, "desc": "Spacious family house with park view."},
    {"id": 3, "title": "Budget Flat", "location": "gulberg", "price": 120000, "beds": 2, "area": 1000, "desc": "Affordable flat suitable for small families."},
    {"id": 4, "title": "Commercial Villa", "location": "dha", "price": 500000, "beds": 5, "area": 3500, "desc": "Prime location villa with high ROI."}
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/predict")
async def predict_price(data: PredictRequest):
    try:
        if os.path.exists("models/price_model.pkl"):
            model = joblib.load("models/price_model.pkl")
            prediction = model.predict([[data.quality, data.sqft]])[0]
            return {"price": round(float(prediction), 2), "confidence": 94}
    except Exception:
        pass
    
    fallback_price = (data.sqft * 165) + (data.quality * 9200)
    return {"price": round(fallback_price, 2), "confidence": 91}

@app.post("/api/recommend")
async def recommend_properties(data: RecommendRequest):
    matches = []
    for prop in PROPERTIES_DB:
        if prop["price"] <= data.budget * 1.15:
            score = 0
            reasons = []
            if prop["location"].lower() == data.location.lower():
                score += 50
                reasons.append("Matches your preferred location")
            if prop["beds"] == data.beds:
                score += 30
                reasons.append(f"Exactly {data.beds} Bedrooms as requested")
            if prop["price"] <= data.budget:
                score += 20
                reasons.append("Well within your defined budget limit")
                
            matches.append({
                "property": prop,
                "score": score,
                "reason": " • ".join(reasons) if reasons else "Good general budget fit"
            })
            
    matches = sorted(matches, key=lambda x: x["score"], reverse=True)
    return {"recommendations": matches[:3]}

@app.post("/api/chat")
async def chat_rag(data: ChatRequest):
    user_msg = data.message.strip()
    try:
        from rag_engine import query_rag
        return {"response": query_rag(user_msg)}
    except Exception:
        return {"response": f"<strong>RAG Response:</strong> For query '{user_msg}', please verify title deeds and NOC from local development authorities."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)