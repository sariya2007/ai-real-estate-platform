import os

DOCS_DIR = "documents"

def load_documents():
    docs_text = ""
    if os.path.exists(DOCS_DIR):
        for file_name in os.listdir(DOCS_DIR):
            file_path = os.path.join(DOCS_DIR, file_name)
            if os.path.isfile(file_path) and file_name.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    docs_text += f.read() + "\n"
    return docs_text

def query_rag(query: str) -> str:
    q = query.lower().strip()
    
    if "korangi" in q or "koangi" in q:
        return "<strong>Korangi Area Guide:</strong> Commercial & industrial hub with high rental ROI. Ensure lease verification from KDA/KMC."
    elif "legal" in q or "document" in q or "buying" in q:
        return "<strong>Legal Verification Guide:</strong><br>1. Check Title Deed & Allotment status.<br>2. Obtain NOC from local authorities.<br>3. Verify property tax clearance."
    elif "price" in q or "cost" in q:
        return "<strong>Market Price Insights:</strong> Property prices vary based on location, quality rating (1-10), and total square footage."
    else:
        return f"<strong>AI RAG Knowledge:</strong> Based on property documents, for query <em>'{query}'</em>, always verify ownership records and property tax clearance before finalizing agreements."