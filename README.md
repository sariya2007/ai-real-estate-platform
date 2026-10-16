<div align="center">

# 🏰 AI Real Estate Intelligence Platform

**An End-to-End Artificial Intelligence Platform for Property Price Prediction, Market Analytics, and RAG-Driven Decision Support.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](#)

---

### 🌐 System Overview

The **AI Real Estate Intelligence Platform** integrates machine learning valuation models, exploratory data analytics, heuristic recommendation engines, and context-aware retrieval-augmented generation (RAG) into a single, cohesive FastAPI web platform.

</div>

---

## ⚡ Core Capabilities

- **📊 Market EDA Dashboard:** Visualizes property area vs. price distribution and quality ratings using Matplotlib and Seaborn.
- **💰 ML Valuation Engine:** Predicts property market prices using a trained **Random Forest Regressor** model based on area and quality metrics.
- **🏠 Property Recommender System:** Matches user preferences (budget, location, room count) with automated reasoning explaining match criteria.
- **🤖 RAG Knowledge Assistant:** Context-aware AI assistant querying local property guidelines, legal documents, and area documentation.
- **🎨 Modern Responsive UI:** Modern dashboard interface with interactive theme switching (Light and Dark modes).

---

## 📂 Project Architecture

```text
ai-real-estate-platform/
│
├── dataset/
│   └── properties_data.csv       # Preprocessed Real Estate Dataset
├── documents/
│   ├── buying_guide.txt          # Knowledge Base Document 1
│   └── real_estate_guide.txt     # Knowledge Base Document 2
├── models/
│   └── price_model.pkl           # Trained ML Valuation Model
├── static/
│   ├── css/
│   │   └── style.css             # Theme Styling & UX
│   ├── js/
│   │   └── app.js                # Frontend Interactions
│   └── eda_dashboard.png         # Analytics Charts
├── templates/
│   └── index.html                # Multi-Tab Web Interface
├── data_analysis.py              # Data Processing & EDA Script
├── train_model.py                # Machine Learning Pipeline
├── rag_engine.py                 # Document Retrieval Engine
├── main.py                       # FastAPI Application Server
├── requirements.txt              # System Dependencies
└── README.md                     # Documentation