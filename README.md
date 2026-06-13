# 🏠 AuraPredict — Real Estate Price Prediction

![AuraPredict Banner](https://img.shields.io/badge/AuraPredict-Enterprise%20Valuation%20Engine-224229?style=for-the-badge&logo=house&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=flat)

---

## 📌 Overview

**AuraPredict** is a full-stack, end-to-end Machine Learning web application that predicts real estate prices in **Bangalore, India**. It combines a trained Linear Regression model with a Flask REST API backend and a modern, premium-grade frontend UI.

Users can enter property details — location, square footage, BHK, and bathrooms — and instantly receive an AI-powered price estimate drawn from over **13,000 real property records**.

---

## ✨ Features

- 🧠 **ML-Powered Predictions** — Linear Regression model trained on Kaggle's Bengaluru House Price dataset
- 🌐 **REST API Backend** — Flask server exposes clean JSON endpoints
- 🎨 **Premium Frontend UI** — Glassmorphism design with smooth animations, searchable autocomplete, and responsive layout
- 📍 **241 Bangalore Localities** — Full sub-locality coverage via one-hot encoding
- 📴 **Offline Simulator Mode** — Works even without the server running (fallback mock estimator)
- 📊 **Market Insights Section** — Price trend chart and top-performing locality table
- 🔼 **Scroll-to-Top** & logo navigation built in

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn, Linear Regression, GridSearchCV, Cross Validation |
| **Model Serialization** | Pickle (`.pkl`) |
| **Backend API** | Flask, Flask-CORS |
| **Frontend** | HTML5, Vanilla CSS (Glassmorphism), JavaScript (ES6+) |
| **Typography** | Google Fonts — Outfit, Lora |
| **Icons** | Font Awesome 6 |

---

## 📁 Project Structure

```
House-Price-Prediction/
│
├── model/
│   ├── price_pred.ipynb              # Jupyter Notebook — full ML pipeline
│   ├── bangalore_price_pred.pkl      # Serialized trained model
│   └── columns.json                  # Feature column names (241 locations + features)
│
├── server/
│   ├── server.py                     # Flask REST API
│   ├── util.py                       # Model loading & prediction logic
│   └── artifacts/
│       ├── bangalore_price_pred.pkl  # Model copy used by the server
│       └── columns.json              # Columns copy used by the server
│
├── client/
│   ├── index.html                    # Main frontend page
│   ├── style.css                     # Premium glassmorphism styles
│   └── app.js                        # Frontend logic & API integration
│
└── README.md
```

---

## 📊 ML Pipeline Workflow

### 1. Data Cleaning
- Missing value handling
- Data standardization (total_sqft ranges → averages)
- Invalid data detection and removal

### 2. Feature Engineering
- BHK extraction from `size` column
- Price Per Square Foot (`price_per_sqft`) computed
- Location-based features with rare category handling (< 10 records → `other`)

### 3. Outlier Detection & Removal
- Location-wise price per sqft outlier removal (mean ± 1 std)
- BHK-based outlier removal (e.g. 2BHK cheaper than 1BHK in same area)
- Bathroom-based outlier removal (bathrooms > BHK + 2)

### 4. Data Encoding
- One-Hot Encoding for 241 Bangalore sub-localities
- Feature selection and dataset preparation

### 5. Model Development
- Train/Test split (80/20)
- K-Fold Cross Validation (k=5)
- GridSearchCV for hyperparameter tuning
- Best model selection and serialization with Pickle

---

## 🚀 Running Locally

### Prerequisites

```bash
pip install flask flask-cors scikit-learn numpy pandas
```

### Step 1 — Start the Flask API Server

```bash
cd House-Price-Prediction
python3 server/server.py
```

The server will start at `http://127.0.0.1:5000`

### Step 2 — Serve the Frontend

```bash
cd client
python3 -m http.server 8080
```

### Step 3 — Open the App

Navigate to **[http://localhost:8080](http://localhost:8080)** in your browser.

The status badge (top-right) will show 🟢 **AI Server Online** when successfully connected.

---

## 🔌 API Endpoints

### `GET/POST /get_location_names`
Returns all 241 Bangalore locality names.

**Response:**
```json
{
  "locations": ["1st block jayanagar", "whitefield", "hebbal", ...]
}
```

---

### `POST /get_estimated_price`
Returns an estimated price in **Lakhs (INR)**.

**Request Body:**
```json
{
  "total_sqft": 1500,
  "location": "Whitefield",
  "bhk": 3,
  "bath": 2
}
```

**Response:**
```json
{
  "estimated_price": 87.42
}
```

---

## 🖥️ Frontend Features

| Feature | Description |
|---|---|
| **Searchable Autocomplete** | Type to filter 241 localities with keyboard navigation |
| **Segmented BHK/Bath Selector** | Smooth iOS-style tab selectors |
| **Live Price Result Card** | Displays price in ₹ Lakhs/Crores + USD equivalent |
| **Offline Simulator** | Falls back to a local estimator when the server is offline |
| **Market Insights** | Price trend chart and top locality performance table |
| **FAQ Accordion** | Explains the model, dataset, and offline mode |
| **Responsive Layout** | Works on desktop, tablet, and mobile |
| **Scroll-to-Top Button** | Appears after scrolling 300px |

---

## 🗺️ Deployment

> ⏳ Deployment coming soon.

Planned deployment stack:
- **Backend:** Render / Railway (Flask API)
- **Frontend:** Vercel / Netlify (Static HTML)

---

## 📜 License

This project is developed for **educational and portfolio purposes**.

---

## 👤 Author

**Arunprakash** — [GitHub](https://github.com/Aruunprakash/House-Price-Prediction)
