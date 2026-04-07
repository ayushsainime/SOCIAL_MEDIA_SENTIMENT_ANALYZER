# Reflex Frontend - Phase 5 & 6
# Main frontend application for sentiment analysis

import reflex as rx
import requests
from typing import List, Dict
from datetime import datetime

# API base URL
API_URL = "http://localhost:8000"


class PredictionResult:
    """Single model prediction result."""
    model_name: str
    prediction: str
    confidence: float = 0.0


class SentimentState(rx.State):
    """State management for sentiment analysis app."""
    
    # Input values
    text: str = ""
    selected_model: str = "svm"
    
    # Single prediction output
    result: str = ""
    confidence: float = 0.0
    error: str = ""
    is_loading: bool = False
    
    # Model comparison results
    comparison_results: List[Dict] = []
    show_comparison: bool = False
    
    # Word cloud
    wordcloud_image: str = ""
    show_wordcloud: bool = False
    
    # Prediction history (last 10)
    history: List[Dict] = []
    max_history: int = 10
    
    # Available models (fetched from API)
    available_models: List[str] = []
    
    def on_mount(self):
        """Fetch available models when component mounts."""
        try:
            response = requests.get(f"{API_URL}/models")
            if response.status_code == 200:
                self.available_models = response.json()["models"]
        except Exception as e:
            self.error = f"Failed to fetch models: {str(e)}"
    
    def predict_sentiment(self):
        """Call FastAPI backend to predict sentiment with single model."""
        if not self.text.strip():
            self.error = "Please enter some text"
            return
        
        self.is_loading = True
        self.error = ""
        self.result = ""
        self.comparison_results = []
        self.show_comparison = False
        
        try:
            payload = {
                "model_name": self.selected_model,
                "text": self.text
            }
            response = requests.post(
                f"{API_URL}/predict",
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                self.result = data['prediction'].upper()
                self.confidence = data.get('confidence', 0.0) or 0.0
                
                # Add to history
                self._add_to_history(self.selected_model, self.result, self.confidence)
            else:
                self.error = f"Error: {response.json().get('detail', 'Unknown error')}"
        except Exception as e:
            self.error = f"Connection error: {str(e)}"
        finally:
            self.is_loading = False
    
    def predict_all_models(self):
        """Call FastAPI backend to predict sentiment with ALL models."""
        if not self.text.strip():
            self.error = "Please enter some text"
            return
        
        self.is_loading = True
        self.error = ""
        self.result = ""
        self.show_comparison = True
        self.comparison_results = []
        
        try:
            payload = {
                "model_name": "svm",  # Required but ignored by predict-all
                "text": self.text
            }
            response = requests.post(
                f"{API_URL}/predict-all",
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                self.comparison_results = [
                    {
                        "model_name": r["model_name"],
                        "prediction": r["prediction"].upper(),
                        "confidence": r.get("confidence", 0.0) or 0.0
                    }
                    for r in data["results"]
                ]
            else:
                self.error = f"Error: {response.json().get('detail', 'Unknown error')}"
                self.show_comparison = False
        except Exception as e:
            self.error = f"Connection error: {str(e)}"
            self.show_comparison = False
        finally:
            self.is_loading = False
    
    def generate_wordcloud(self):
        """Generate word cloud from input text."""
        if not self.text.strip():
            self.error = "Please enter some text"
            return
        
        self.is_loading = True
        self.error = ""
        
        try:
            payload = {"text": self.text}
            response = requests.post(
                f"{API_URL}/wordcloud",
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                self.wordcloud_image = data["image"]
                self.show_wordcloud = True
            else:
                self.error = f"Error: {response.json().get('detail', 'Unknown error')}"
        except Exception as e:
            self.error = f"Connection error: {str(e)}"
        finally:
            self.is_loading = False
    
    def _add_to_history(self, model: str, prediction: str, confidence: float):
        """Add prediction to history."""
        entry = {
            "text": self.text[:50] + "..." if len(self.text) > 50 else self.text,
            "model": model,
            "prediction": prediction,
            "confidence": confidence,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.history.insert(0, entry)
        # Keep only last max_history entries
        if len(self.history) > self.max_history:
            self.history = self.history[:self.max_history]
    
    def clear_history(self):
        """Clear prediction history."""
        self.history = []
    
    def toggle_comparison(self):
        """Toggle comparison view."""
        self.show_comparison = not self.show_comparison
        if not self.show_comparison:
            self.comparison_results = []
    
    def toggle_wordcloud(self):
        """Toggle word cloud view."""
        self.show_wordcloud = not self.show_wordcloud
        if not self.show_wordcloud:
            self.wordcloud_image = ""


def get_sentiment_color(prediction: str) -> str:
    """Get color based on sentiment."""
    if prediction == "POSITIVE":
        return "green"
    elif prediction == "NEGATIVE":
        return "red"
    return "yellow"


def index() -> rx.Component:
    """Main page component."""
    return rx.container(
        rx.vstack(
            # Header
            rx.heading("🔍 Sentiment Analysis", size="lg"),
            rx.text("Analyze text sentiment using ML models", size="sm", color="gray"),
            
            rx.spacer(size="md"),
            
            # Model selection dropdown
            rx.vstack(
                rx.text("Select Model:", weight="bold"),
                rx.select(
                    value=SentimentState.selected_model,
                    on_change=SentimentState.set_selected_model,
                    options=SentimentState.available_models,
                    placeholder="Choose a model...",
                ),
                width="100%",
            ),
            
            rx.spacer(size="sm"),
            
            # Text input area
            rx.vstack(
                rx.text("Enter Text:", weight="bold"),
                rx.text_area(
                    value=SentimentState.text,
                    on_change=SentimentState.set_text,
                    placeholder="Type or paste your text here...",
                    min_height=150,
                ),
                width="100%",
            ),
            
            rx.spacer(size="sm"),
            
            # Action buttons
            rx.hstack(
                rx.button(
                    "Analyze (Single)",
                    on_click=SentimentState.predict_sentiment,
                    is_loading=SentimentState.is_loading,
                    color="blue",
                    size="lg",
                ),
                rx.button(
                    "Compare All Models",
                    on_click=SentimentState.predict_all_models,
                    is_loading=SentimentState.is_loading,
                    color="purple",
                    size="lg",
                    variant="outline",
                ),
                rx.button(
                    "Word Cloud",
                    on_click=SentimentState.generate_wordcloud,
                    is_loading=SentimentState.is_loading,
                    color="teal",
                    size="lg",
                    variant="outline",
                ),
                spacing="sm",
                wrap="wrap",
            ),
            
            rx.spacer(size="md"),
            
            # Error display
            rx.cond(
                SentimentState.error != "",
                rx.callout(
                    SentimentState.error,
                    color="red",
                ),
            ),
            
            # Single prediction result with confidence
            rx.cond(
                SentimentState.result != "",
                rx.vstack(
                    rx.text("Prediction Result:", weight="bold", size="lg"),
                    rx.hstack(
                        rx.badge(
                            SentimentState.result,
                            color_scheme=rx.cond(
                                SentimentState.result == "POSITIVE",
                                "green",
                                rx.cond(
                                    SentimentState.result == "NEGATIVE",
                                    "red",
                                    "yellow"
                                )
                            ),
                            size="lg",
                        ),
                        rx.text(
                            f"Confidence: {SentimentState.confidence:.1f}%",
                            size="sm",
                            color="gray",
                        ),
                    ),
                    # Confidence bar
                    rx.progress(
                        value=SentimentState.confidence,
                        width="100%",
                    ),
                    width="100%",
                    align="center",
                ),
            ),
            
            rx.spacer(size="md"),
            
            # Model Comparison Results
            rx.cond(
                SentimentState.show_comparison,
                rx.vstack(
                    rx.text("📊 Model Comparison:", weight="bold", size="lg"),
                    rx.box(
                        rx.foreach(
                            SentimentState.comparison_results,
                            lambda r: rx.hstack(
                                rx.text(r["model_name"], width="150px", weight="medium"),
                                rx.badge(
                                    r["prediction"],
                                    color_scheme=rx.cond(
                                        r["prediction"] == "POSITIVE",
                                        "green",
                                        rx.cond(
                                            r["prediction"] == "NEGATIVE",
                                            "red",
                                            "yellow"
                                        )
                                    ),
                                ),
                                rx.text(f"{r['confidence']:.1f}%", size="sm", color="gray"),
                                rx.progress(value=r["confidence"], width="100px"),
                                width="100%",
                                justify="start",
                                padding_y="4px",
                            ),
                        ),
                        width="100%",
                        padding="4",
                        border_radius="md",
                        border="1px solid",
                        border_color="gray.200",
                    ),
                    width="100%",
                ),
            ),
            
            rx.spacer(size="md"),
            
            # Word Cloud Display
            rx.cond(
                SentimentState.show_wordcloud,
                rx.vstack(
                    rx.text("☁️ Word Cloud:", weight="bold", size="lg"),
                    rx.box(
                        rx.image(
                            src=f"data:image/png;base64,{SentimentState.wordcloud_image}",
                            width="100%",
                            max_width="800px",
                        ),
                        padding="4",
                        border_radius="md",
                        border="1px solid",
                        border_color="gray.200",
                    ),
                    width="100%",
                    align="center",
                ),
            ),
            
            rx.spacer(size="lg"),
            
            # Prediction History
            rx.cond(
                SentimentState.history.length() > 0,
                rx.vstack(
                    rx.hstack(
                        rx.text("📜 History (Last 10):", weight="bold", size="lg"),
                        rx.button(
                            "Clear",
                            on_click=SentimentState.clear_history,
                            size="sm",
                            color="red",
                            variant="ghost",
                        ),
                        width="100%",
                        justify="space-between",
                    ),
                    rx.box(
                        rx.foreach(
                            SentimentState.history,
                            lambda h: rx.hstack(
                                rx.text(h["timestamp"], size="xs", color="gray", width="60px"),
                                rx.text(h["text"], size="sm", width="200px", truncate=True),
                                rx.text(h["model"], size="xs", color="blue", width="100px"),
                                rx.badge(
                                    h["prediction"],
                                    color_scheme=rx.cond(
                                        h["prediction"] == "POSITIVE",
                                        "green",
                                        rx.cond(
                                            h["prediction"] == "NEGATIVE",
                                            "red",
                                            "yellow"
                                        )
                                    ),
                                    size="sm",
                                ),
                                rx.text(f"{h['confidence']:.1f}%", size="xs", color="gray"),
                                width="100%",
                                spacing="sm",
                                padding_y="2px",
                            ),
                        ),
                        width="100%",
                        max_height="200px",
                        overflow_y="auto",
                        padding="4",
                        border_radius="md",
                        border="1px solid",
                        border_color="gray.200",
                    ),
                    width="100%",
                ),
            ),
            
            rx.spacer(size="lg"),
            
            # Footer
            rx.divider(),
            rx.hstack(
                rx.text("Available models: ", weight="bold"),
                rx.text(", ".join(SentimentState.available_models), color="gray"),
            ),
            width="100%",
            max_width="800px",
        ),
        padding="4",
    )


# Create app and add page
app = rx.App()
app.add_page(index)