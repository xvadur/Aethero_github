#!/usr/bin/env python3
"""
AetheroOS Reflection API
FastAPI application with emotion analysis and introspective insights
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("🚀 Starting AetheroOS Reflection API...")

# Create FastAPI app
app = FastAPI(
    title="AetheroOS Introspective API",
    description="Introspective reflection and cognitive analysis system for AetheroOS",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load transformers if available
TRANSFORMERS_AVAILABLE = False
emotion_classifier = None

try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
    logger.info("✅ Transformers available")
    
    try:
        emotion_classifier = pipeline(
            "text-classification", 
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
        logger.info("✅ Emotion classifier loaded")
    except Exception as e:
        logger.warning(f"⚠️ Failed to load emotion classifier: {e}")
        emotion_classifier = None
        
except ImportError:
    logger.warning("⚠️ Transformers not available - using fallback")

# Pydantic models
class ReflectionInput(BaseModel):
    text: str
    include_confidence: bool = True
    max_emotions: int = 5

class EmotionResult(BaseModel):
    label: str
    score: float

class ReflectionOutput(BaseModel):
    text: str
    emotions: List[EmotionResult]
    primary_emotion: str
    confidence: float
    analysis_timestamp: str
    introspective_insights: Dict[str, Any]

# Fallback emotion analysis
def fallback_emotion_analysis(text: str) -> List[Dict[str, Any]]:
    """Basic emotion analysis using keyword matching"""
    emotion_keywords = {
        "joy": ["happy", "joy", "excited", "cheerful", "delighted", "pleased"],
        "sadness": ["sad", "depressed", "melancholy", "sorrowful", "grief"],
        "anger": ["angry", "furious", "rage", "irritated", "mad", "frustrated"],
        "fear": ["afraid", "scared", "terrified", "anxious", "worried", "panic"],
        "surprise": ["surprised", "amazed", "astonished", "shocked", "startled"],
        "love": ["love", "affection", "adore", "cherish", "devoted", "caring"]
    }
    
    text_lower = text.lower()
    scores = {}
    
    for emotion, keywords in emotion_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            scores[emotion] = score / len(keywords)
    
    if not scores:
        scores["neutral"] = 1.0
    
    total_score = sum(scores.values())
    normalized_scores = {emotion: score/total_score for emotion, score in scores.items()}
    
    return [{"label": emotion, "score": score} for emotion, score in normalized_scores.items()]

def generate_insights(text: str, emotions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate introspective insights"""
    primary_emotion = emotions[0]["label"] if emotions else "neutral"
    emotion_diversity = len([e for e in emotions if e["score"] > 0.1])
    
    cognitive_load = min(10, max(1, len(text.split()) // 10))
    emotional_complexity = min(1.0, emotion_diversity / 6.0)
    
    # Temporal focus analysis
    past_indicators = ["was", "were", "had", "did", "before", "yesterday"]
    future_indicators = ["will", "shall", "going to", "tomorrow", "soon", "later"]
    present_indicators = ["is", "are", "am", "now", "currently", "today"]
    
    text_lower = text.lower()
    past_count = sum(1 for indicator in past_indicators if indicator in text_lower)
    future_count = sum(1 for indicator in future_indicators if indicator in text_lower)
    present_count = sum(1 for indicator in present_indicators if indicator in text_lower)
    
    temporal_focus = "present"
    if past_count > max(future_count, present_count):
        temporal_focus = "past"
    elif future_count > max(past_count, present_count):
        temporal_focus = "future"
    
    constitutional_keywords = ["transparent", "honest", "introspect", "reflect", "validate", "truth"]
    constitutional_score = sum(1 for keyword in constitutional_keywords if keyword in text_lower)
    constitutional_alignment = min(1.0, constitutional_score / 3.0)
    
    return {
        "cognitive_load": cognitive_load,
        "emotional_complexity": emotional_complexity,
        "temporal_focus": temporal_focus,
        "constitutional_alignment": constitutional_alignment,
        "emotion_diversity": emotion_diversity,
        "analysis_confidence": emotions[0]["score"] if emotions else 0.5
    }

# API Endpoints
@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "message": "🧠 AetheroOS Introspective System",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "capabilities": {
            "emotion_analysis": True,
            "transformers_backend": TRANSFORMERS_AVAILABLE,
            "fallback_analysis": True
        }
    }

@app.post("/reflection/reflect", response_model=ReflectionOutput)
async def reflect(input_data: ReflectionInput):
    """Perform introspective reflection and emotion analysis"""
    try:
        if not input_data.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty")
        
        # Perform emotion analysis
        if emotion_classifier and TRANSFORMERS_AVAILABLE:
            results = emotion_classifier(input_data.text)
            if not isinstance(results, list):
                results = [results]
        else:
            results = fallback_emotion_analysis(input_data.text)
        
        # Sort and limit results
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        limited_results = sorted_results[:input_data.max_emotions]
        
        # Convert to EmotionResult objects
        emotions = [
            EmotionResult(label=result['label'], score=result['score'])
            for result in limited_results
        ]
        
        # Generate insights
        introspective_insights = generate_insights(input_data.text, limited_results)
        
        return ReflectionOutput(
            text=input_data.text,
            emotions=emotions,
            primary_emotion=emotions[0].label if emotions else "neutral",
            confidence=emotions[0].score if emotions else 0.5,
            analysis_timestamp=datetime.now().isoformat(),
            introspective_insights=introspective_insights
        )
        
    except Exception as e:
        logger.error(f"Error in reflection analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/reflection/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "transformers_available": TRANSFORMERS_AVAILABLE,
        "emotion_classifier_loaded": emotion_classifier is not None,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/reflection/capabilities")
async def get_capabilities():
    """Get reflection agent capabilities"""
    return {
        "emotion_analysis": True,
        "introspective_insights": True,
        "cognitive_metrics": True,
        "constitutional_alignment": True,
        "transformers_backend": TRANSFORMERS_AVAILABLE,
        "fallback_analysis": True,
        "supported_emotions": [
            "joy", "sadness", "anger", "fear", "surprise", "love", "neutral"
        ] if not TRANSFORMERS_AVAILABLE else "dynamic_from_model"
    }

@app.get("/health")
async def global_health():
    """Global health check"""
    return {
        "status": "healthy",
        "service": "AetheroOS Reflection API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting AetheroOS Reflection API server...")
    uvicorn.run(app, host="0.0.0.0", port=7860)
