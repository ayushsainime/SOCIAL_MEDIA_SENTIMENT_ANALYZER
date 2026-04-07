# Sentiment Analysis App

A minimal ML web app for sentiment analysis using FastAPI and Reflex.

## Project Structure

```
├── backend/           # FastAPI backend
│   ├── __init__.py
│   ├── main.py           # Main API application
│   ├── models_loader.py # Model loading utilities
│   └── preprocess.py    # Text preprocessing
├── frontend/          # Reflex frontend
│   ├── __init__.py
│   └── app.py            # Main frontend application
├── models/            # Pre-trained ML models
│   ├── tfidf_vectorizer.pkl
│   ├── svm_model.pkl
│   ├── random_forest_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── gradient_boosting_model.pkl
│   ├── lgbm_model.pkl
│   └── ada_boost_model.pkl
├── Dockerfile
├── start.sh
└── requirements.txt
```

## Available Models

- SVM
- Random Forest
- Logistic Regression
- Gradient Boosting
- AdaBoost

## Labels
- `-1`: Negative
- `0`: Neutral
- `1`: Positive