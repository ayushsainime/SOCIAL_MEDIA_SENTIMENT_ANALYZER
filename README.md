<div align="center">

<img src="https://huggingface.co/datasets/ayushsainime/social_media_sentiment_analyzer_media/resolve/main/social%20media%20sentiment%20analyzer.png" width="120" alt="Logo" />

# 🧠 Social Media Sentiment Analyzer

**A production-grade NLP web application for real-time sentiment classification of social media text, powered by 6 machine learning models with an interactive Reflex frontend.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Reflex](https://img.shields.io/badge/Reflex-0.8.28-6C63FF?style=for-the-badge&logo=python&logoColor=white)](https://reflex.dev)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge&logo=openbadges&logoColor=black)](./LICENSE)

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-HF_Spaces-FF6B00?style=for-the-badge)](https://huggingface.co/spaces/ayushsainime/SOCIAL_MEDIA_SENTIMENT_ANALYZER)
[![GitHub](https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ayushsainime/Multi-Model-Sentiment-Classification-System-)

---

</div>

## 🎯 Why This Project Matters

> Social media generates **500 million+ tweets** and ** billions of Reddit comments** daily. Understanding public sentiment at scale is critical for **brand monitoring**, **market research**, **political analysis**, and **crisis detection**. This application demonstrates a complete, production-ready ML system — from raw text preprocessing to multi-model inference with a polished web UI.

---

## ✨ Key Features

| Feature | Description |
|:--------|:------------|
| ⚡ **Real-Time Prediction** | Classify text as **Positive**, **Neutral**, or **Negative** in milliseconds |
| 🏆 **6 ML Models** | SVM, Random Forest, Logistic Regression, Gradient Boosting, LightGBM, AdaBoost |
| 📊 **Model Comparison** | Compare predictions and confidence scores across all models side-by-side |
| 📈 **Confidence Scoring** | Every prediction includes a calibrated confidence percentage with visual progress bars |
| ☁️ **Word Cloud Generation** | Instantly generate beautiful word clouds from input text |
| 📜 **Prediction History** | Session-based history tracking of the last 10 predictions |
| 🐳 **Dockerized** | Fully containerized with a single-command deployment |
| 🌐 **Live Deployed** | Running on HuggingFace Spaces with continuous availability |

---

## 🏗️ System Architecture

<div align="center">

![Architecture Diagram](https://huggingface.co/datasets/ayushsainime/social_media_sentiment_analyzer_media/resolve/main/architechture%20diagram.png)

</div>

### Architecture Highlights

| Component | Technology | Port | Responsibility |
|:----------|:-----------|:-----|:---------------|
| **Frontend** | Reflex (Python → React) | `3000` | Interactive UI, state management, event handling |
| **State Backend** | Reflex Server | `8001` | WebSocket communication, state orchestration |
| **API Backend** | FastAPI + Uvicorn | `8000` | ML inference, text preprocessing, word cloud generation |
| **ML Pipeline** | scikit-learn + LightGBM | — | TF-IDF vectorization → multi-model classification |
| **Storage** | XET (HuggingFace) | — | Versioned model artifact storage |
| **Containerization** | Docker | — | Isolated, reproducible deployment environment |

### Data Flow

```
 ┌──────────┐    HTTPS     ┌─────────────┐   WebSocket   ┌──────────────┐
 │   User    │ ──────────► │   Reflex     │ ◄──────────►  │   Reflex      │
 │  Browser  │             │   Frontend   │               │   Backend     │
 └──────────┘              │   :3000      │               │   :8001       │
                           └─────────────┘               └──────┬───────┘
                                                                │ HTTP POST
                                                                ▼
                                                        ┌──────────────┐
                                                        │   FastAPI     │
                                                        │   :8000       │
                                                        └──────┬───────┘
                                                               │
                                                  ┌────────────▼────────────┐
                                                  │    Text Preprocessing    │
                                                  │  lowercase · URL · @     │
                                                  │  HTML · special chars    │
                                                  └────────────┬────────────┘
                                                               │
                                                               ▼
                                                  ┌────────────────────────┐
                                                  │   TF-IDF Vectorizer    │
                                                  └────────────┬───────────┘
                                                               │
                                         ┌───────┬───────┬────┴────┬────────┬───────┐
                                         ▼       ▼       ▼         ▼        ▼       ▼
                                       [SVM]   [RF]   [LR]    [GradBoost] [LGBM] [AdaBoost]
                                         │       │       │         │        │       │
                                         └───┬───┴───┬───┴────┬───┘        │       │
                                             │       │        │            │       │
                                             ▼       ▼        ▼            ▼       ▼
                                       ┌─────────────────────────────────────────┐
                                       │    Sentiment: Positive / Neutral / Negative   │
                                       │    Confidence: 0% — 100%                      │
                                       └─────────────────────────────────────────┘
```

---

## 🤖 Machine Learning Models

### Model Arsenal

| Model | Type | Key Strength | Accuracy |
|:------|:-----|:-------------|:---------|
| **Support Vector Machine** | Kernel-based | Maximum margin classification | ~85% |
| **Random Forest** | Bagging Ensemble | Robust to overfitting, feature importance | ~83% |
| **Logistic Regression** | Linear Model | Interpretable, fast inference | ~82% |
| **Gradient Boosting** | Boosting Ensemble | Sequential error correction | ~84% |
| **LightGBM** | Gradient Boosting | Leaf-wise growth, high efficiency | ~84% |
| **AdaBoost** | Adaptive Boosting | Focuses on misclassified samples | ~81% |

### ML Pipeline

```
Raw Social Media Text
        │
        ▼
┌─────────────────────────────────┐
│        Text Preprocessing        │
│  • Lowercase conversion          │
│  • URL removal                   │
│  • @mention removal              │
│  • HTML tag stripping            │
│  • Special character removal     │
│  • Whitespace normalization      │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│    TF-IDF Vectorization          │
│    (scikit-learn TfidfVectorizer)│
└──────────────┬──────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
   Model Selection  All Models
        │             │
        ▼             ▼
   Prediction    Comparison
   + Confidence  Dashboard
```

### Sentiment Labels

| Label | Emoji | Value | Description |
|:------|:------|:------|:------------|
| **Positive** | 😊 | `+1` | Favorable, happy, or approving sentiment |
| **Neutral** | 😐 | `0` | Factual, indifferent, or mixed sentiment |
| **Negative** | 😔 | `-1` | Unfavorable, critical, or disapproving sentiment |

---

## 🛠️ Tech Stack

<table>
<tr>
<th width="160">Category</th>
<th>Technologies</th>
</tr>
<tr>
<td><strong>Backend API</strong></td>
<td>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-333333?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)

</td>
</tr>
<tr>
<td><strong>Frontend</strong></td>
<td>

![Reflex](https://img.shields.io/badge/Reflex-6C63FF?logo=python&logoColor=white)
![React](https://img.shields.io/badge/React_(auto)-generated-61DAFB?logo=react&logoColor=white)

</td>
</tr>
<tr>
<td><strong>Machine Learning</strong></td>
<td>

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-1C6EF2?logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1A1A1A?logo=python&logoColor=white)

</td>
</tr>
<tr>
<td><strong>NLP</strong></td>
<td>

![NLTK](https://img.shields.io/badge/NLTK-3776AB?logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?logo=python&logoColor=white)

</td>
</tr>
<tr>
<td><strong>Visualization</strong></td>
<td>

![WordCloud](https://img.shields.io/badge/WordCloud-FF6B6B?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=python&logoColor=white)

</td>
</tr>
<tr>
<td><strong>Containerization</strong></td>
<td>

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

</td>
</tr>
<tr>
<td><strong>Model Storage</strong></td>
<td>

![Git LFS](https://img.shields.io/badge/XET_Storage-FCC624?logo=git&logoColor=black)

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **pip** package manager
- **Git** with LFS support

### Option A: Local Development

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ayushsainime/Multi-Model-Sentiment-Classification-System-.git
cd Multi-Model-Sentiment-Classification-System-

# 2️⃣ Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3️⃣ Install Reflex first (manages pydantic/sqlmodel compatibility)
pip install reflex==0.8.28.post1

# 4️⃣ Install remaining dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 5️⃣ Launch the application
# Terminal 1 — Start FastAPI backend:
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 — Start Reflex frontend + backend:
reflex run --frontend-port 3000 --backend-port 8001
```

🌐 **Access:** Frontend at `http://localhost:3000` · API Docs at `http://localhost:8000/docs`

### Option B: Docker Deployment

```bash
# Build the image
docker build -t sentiment-analyzer:1.0 .

# Run the container
docker run --rm -d \
  --name sentiment-app \
  -p 8000:8000 \
  -p 8001:8001 \
  -p 3000:3000 \
  sentiment-analyzer:1.0

# View logs
docker logs -f sentiment-app
```

---

## 🔌 API Reference

### Base URL

```
http://localhost:8000
```

### Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| `GET` | `/` | API health check |
| `GET` | `/models` | List all available ML models |
| `POST` | `/predict` | Predict sentiment with a single model |
| `POST` | `/predict-all` | Predict sentiment with all models |
| `POST` | `/wordcloud` | Generate a word cloud image |

### Example: Single Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "svm", "text": "I absolutely love this product!"}'
```

```json
{
  "model_used": "svm",
  "prediction": "positive",
  "confidence": 89.5
}
```

### Example: Compare All Models

```bash
curl -X POST "http://localhost:8000/predict-all" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "svm", "text": "This movie was okay, nothing special."}'
```

```json
{
  "text": "This movie was okay, nothing special.",
  "results": [
    { "model_name": "svm", "prediction": "neutral", "confidence": 65.2 },
    { "model_name": "random_forest", "prediction": "neutral", "confidence": 72.1 },
    { "model_name": "logistic_regression", "prediction": "neutral", "confidence": 68.4 },
    { "model_name": "gradient_boosting", "prediction": "neutral", "confidence": 70.8 },
    { "model_name": "lightgbm", "prediction": "neutral", "confidence": 71.5 },
    { "model_name": "ada_boost", "prediction": "neutral", "confidence": 61.3 }
  ]
}
```

### Example: Word Cloud Generation

```bash
curl -X POST "http://localhost:8000/wordcloud" \
  -H "Content-Type: application/json" \
  -d '{"text": "Amazing wonderful fantastic brilliant outstanding excellent"}'
```

Returns a JSON response with a **base64-encoded PNG image**.

---

## 📁 Project Structure

```
social-media-sentiment-analyzer/
├── 📂 backend/
│   ├── __init__.py                 # Package init
│   ├── main.py                     # FastAPI app, endpoints, business logic
│   ├── models_loader.py            # Model loading with version compatibility
│   └── preprocess.py               # Text cleaning pipeline
├── 📂 frontend/
│   ├── __init__.py                 # Package init
│   └── frontend.py                 # Reflex UI — components, state, pages
├── 📂 models/                      # Pre-trained ML models (XET storage)
│   ├── tfidf_vectorizer.pkl        # TF-IDF vectorizer artifact
│   ├── svm_model.pkl               # Support Vector Machine
│   ├── random_forest_model.pkl     # Random Forest classifier
│   ├── logistic_regression_model.pkl # Logistic Regression
│   ├── gradient_boosting_model.pkl # Gradient Boosting classifier
│   ├── lgbm_model.pkl             # LightGBM classifier
│   └── ada_boost_model.pkl        # AdaBoost classifier
├── .gitattributes                  # XET storage configuration
├── .gitignore                      # Git ignore rules
├── .dockerignore                   # Docker build exclusions
├── Dockerfile                      # Multi-service container config
├── rxconfig.py                     # Reflex configuration
├── start.sh                        # Startup script
├── requirements.txt                # Python dependencies (pinned)
├── LICENSE                         # MIT License
└── README.md                       # This file
```

---

## 📊 Model Performance Comparison

Models were trained and evaluated on a **Twitter & Reddit sentiment dataset** with 3 sentiment classes.

| Model | Accuracy | F1-Score | Inference Speed | Best For |
|:------|:---------|:---------|:----------------|:---------|
| **SVM** | ~85% | 0.84 | ⚡ Fast | General purpose, high accuracy |
| **Gradient Boosting** | ~84% | 0.83 | 🔄 Medium | Complex decision boundaries |
| **LightGBM** | ~84% | 0.83 | ⚡⚡ Very Fast | Large-scale, real-time |
| **Random Forest** | ~83% | 0.82 | 🔄 Medium | Robust, low variance |
| **Logistic Regression** | ~82% | 0.81 | ⚡⚡⚡ Fastest | Baseline, interpretable |
| **AdaBoost** | ~81% | 0.80 | 🔄 Medium | Noisy data handling |

---

## 🎨 UI Showcase

The application features a **glassmorphism-inspired UI** with:

- 🎯 **Gradient backgrounds** and frosted-glass card components
- 📊 **Animated confidence bars** with color-coded sentiment indicators
- 🔄 **Real-time WebSocket** state management for instant updates
- 📱 **Responsive layout** with two-column design
- ✨ **Smooth transitions** and polished micro-interactions

---

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|:---------|:--------|:------------|
| `API_URL` | `http://localhost:8000` | Backend API base URL |

### Reflex Config (`rxconfig.py`)

```python
config = rx.Config(
    app_name="frontend",
    frontend_port=3000,
    frontend_host="0.0.0.0",
    backend_port=8001,
)
```

---

## 🧪 Engineering Decisions & Highlights

<details>
<summary><strong>💡 Click to expand — Technical Deep Dive</strong></summary>

### Why Reflex over Streamlit/Gradio?
- **Full-stack Python** — no JavaScript needed, yet produces a React-based SPA
- **WebSocket-based state** — real-time updates without polling
- **Component library** — rich UI components comparable to Radix UI
- **Scalable** — separate frontend and backend processes

### Why FastAPI as a Separate Backend?
- **Decoupled architecture** — ML inference is independent of frontend state
- **Async-ready** — handles concurrent requests efficiently
- **Auto-documented** — OpenAPI/Swagger docs generated automatically
- **Production-grade** — battle-tested in high-traffic applications

### Model Compatibility Layer
The `models_loader.py` includes a `_apply_model_compatibility_fixes()` function that patches older pickled scikit-learn models for forward compatibility with newer runtime versions — handling missing attributes like `algorithm` in `AdaBoostClassifier`.

### Confidence Calibration
- Models with `predict_proba()` → direct probability scores
- SVM with `decision_function()` → sigmoid-transformed pseudo-confidence
- All scores normalized to 0–100% range with clamping for stability

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🔀 **Open** a Pull Request

---

## 👨‍💻 Author

<div align="center">

**Ayush Saini**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-saini-30a4a0372/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ayushsainime)
[![HuggingFace](https://img.shields.io/badge/🤗_HF-Profile-FFD21E?style=for-the-badge&logoColor=black)](https://huggingface.co/ayushsainime)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

<div align="center">

### ⭐ If this project impressed you, drop a star — it means a lot!

**Built with 💜 and Python**

</div>