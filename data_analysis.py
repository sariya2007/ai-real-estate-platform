import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_and_save_model():
    print("Training Machine Learning Price Prediction Model...")
    
    # Folder check & creation
    os.makedirs("models", exist_ok=True)
    os.makedirs("dataset", exist_ok=True)

    # Generate Synthetic Dataset if not exists
    np.random.seed(42)
    n_samples = 500
    
    sqft = np.random.randint(500, 5000, n_samples)
    quality = np.random.randint(1, 11, n_samples)
    bedrooms = np.random.randint(1, 6, n_samples)
    
    # Price Formula with noise
    price = (sqft * 160) + (quality * 9500) + (bedrooms * 15000) + np.random.normal(0, 10000, n_samples)
    
    df = pd.DataFrame({'sqft': sqft, 'quality': quality, 'bedrooms': bedrooms, 'price': price})
    df.to_csv("dataset/properties_data.csv", index=False)
    print("Saved dataset to dataset/properties_data.csv")

    # Features and Target
    X = df[['quality', 'sqft']]  # Matching features used in prediction API
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    print(f"Model Trained Successfully! R2 Score: {r2:.4f}")

    # Save Model
    joblib.dump(model, "models/price_model.pkl")
    print("Saved model to models/price_model.pkl")

if __name__ == "__main__":
    train_and_save_model()