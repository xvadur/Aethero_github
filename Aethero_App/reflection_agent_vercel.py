# AETH-TASK-004 :: ROLE: Archivus :: GOAL: Vercel-optimized reflection agent
# reflection_agent_vercel.py
# FastAPI-based Introspective Reflection Agent optimized for Vercel cold starts

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import logging
from datetime import datetime
import asyncio

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI router
router = APIRouter(prefix="/reflection", tags=["reflection"])

# Global variables for lazy loading
TRANSFORMERS_AVAILABLE = False
emotion_classifier = None
_classifier_loading = False

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
    analysis_method: str

async def lazy_load_classifier():
    """Lazy load emotion classifier to optimize cold starts"""
    global emotion_classifier, TRANSFORMERS_AVAILABLE, _classifier_loading
    
    if emotion_classifier is not None:
        return emotion_classifier
    
    if _classifier_loading:
        # Wait for ongoing loading
        while _classifier_loading:
            await asyncio.sleep(0.1)
        return emotion_classifier
    
    _classifier_loading = True
    
    try:
        from transformers import pipeline
        TRANSFORMERS_AVAILABLE = True
        logger.info("✅ Transformers available, loading emotion classifier...")
        
        emotion_classifier = pipeline(
            "text-classification", 
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
        logger.info("✅ Emotion classifier loaded successfully")
        
    except Exception as e:
        logger.warning(f"⚠️ Failed to load emotion classifier: {e}")
        emotion_classifier = None
        TRANSFORMERS_AVAILABLE = False
    finally:
        _classifier_loading = False
    
    return emotion_classifier

def fallback_emotion_analysis(text: str) -> List[Dict[str, Any]]:
    """Lightweight emotion analysis using keyword matching"""
    emotion_keywords = {
        "joy": ["happy", "joy", "excited", "cheerful", "delighted", "pleased", "glad", "elated"],
        "sadness": ["sad", "depressed", "melancholy", "sorrowful", "grief", "dejected", "gloomy"],
        "anger": ["angry", "furious", "rage", "irritated", "mad", "frustrated", "annoyed"],
        "fear": ["afraid", "scared", "terrified", "anxious", "worried", "panic", "nervous"],
        "surprise": ["surprised", "amazed", "astonished", "shocked", "startled", "stunned"],
        "love": ["love", "affection", "adore", "cherish", "devoted", "caring", "tender"]
    }
    
    text_lower = text.lower()
    scores = {}
    
    for emotion, keywords in emotion_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            scores[emotion] = score / len(keywords)
    
    if not scores:
        scores["neutral"] = 1.0
    
    # Normalize scores
    total_score = sum(scores.values())
    normalized_scores = {emotion: score/total_score for emotion, score in scores.items()}
    
    return [{"label": emotion, "score": score} for emotion, score in normalized_scores.items()]

def generate_introspective_insights(text: str, emotions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate introspective insights about the emotional analysis"""
    
    primary_emotion = emotions[0]["label"] if emotions else "neutral"
    emotion_diversity = len([e for e in emotions if e["score"] > 0.1])
    
    # Calculate cognitive metrics
    words = text.split()
    cognitive_load = min(10, max(1, len(words) // 10))
    emotional_complexity = min(1.0, emotion_diversity / 6.0)
    
    # Temporal focus analysis (optimized)
    temporal_indicators = {
        "past": ["was", "were", "had", "did", "before", "yesterday"],
        "future": ["will", "shall", "going", "tomorrow", "soon", "later"],
        "present": ["is", "are", "am", "now", "currently", "today"]
    }
    
    text_lower = text.lower()
    temporal_scores = {}
    
    for focus, indicators in temporal_indicators.items():
        temporal_scores[focus] = sum(1 for indicator in indicators if indicator in text_lower)
    
    temporal_focus = max(temporal_scores, key=temporal_scores.get) if any(temporal_scores.values()) else "present"
    
    # Constitutional alignment (AetheroOS specific)
    constitutional_keywords = ["transparent", "honest", "introspect", "reflect", "validate", "truth", "authentic"]
    constitutional_score = sum(1 for keyword in constitutional_keywords if keyword in text_lower)
    constitutional_alignment = min(1.0, constitutional_score / 3.0)
    
    return {
        "cognitive_load": cognitive_load,
        "emotional_complexity": emotional_complexity,
        "temporal_focus": temporal_focus,
        "constitutional_alignment": constitutional_alignment,
        "emotion_diversity": emotion_diversity,
        "analysis_confidence": emotions[0]["score"] if emotions else 0.5,
        "word_count": len(words),
        "sentiment_intensity": sum(e["score"] for e in emotions if e["label"] != "neutral")
    }

@router.post("/reflect", response_model=ReflectionOutput)
async def reflect(input_data: ReflectionInput):
    """
    Perform introspective reflection and emotion analysis on input text
    
    Args:
        input_data: ReflectionInput containing text and analysis parameters
        
    Returns:
        ReflectionOutput with emotions, insights, and introspective analysis
    """
    try:
        if not input_data.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty")
        
        # Try to load classifier (lazy loading)
        classifier = await lazy_load_classifier()
        analysis_method = "transformers" if classifier else "fallback"
        
        # Perform emotion analysis
        if classifier and TRANSFORMERS_AVAILABLE:
            try:
                results = classifier(input_data.text)
                # Ensure results is a list
                if not isinstance(results, list):
                    results = [results]
            except Exception as e:
                logger.warning(f"Transformers analysis failed, using fallback: {e}")
                results = fallback_emotion_analysis(input_data.text)
                analysis_method = "fallback"
        else:
            results = fallback_emotion_analysis(input_data.text)
        
        # Sort by confidence and limit results
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        limited_results = sorted_results[:input_data.max_emotions]
        
        # Convert to EmotionResult objects
        emotions = [
            EmotionResult(label=result['label'], score=result['score'])
            for result in limited_results
        ]
        
        # Generate introspective insights
        introspective_insights = generate_introspective_insights(
            input_data.text, 
            limited_results
        )
        
        return ReflectionOutput(
            text=input_data.text,
            emotions=emotions,
            primary_emotion=emotions[0].label if emotions else "neutral",
            confidence=emotions[0].score if emotions else 0.5,
            analysis_timestamp=datetime.now().isoformat(),
            introspective_insights=introspective_insights,
            analysis_method=analysis_method
        )
        
    except Exception as e:
        logger.error(f"Error in reflection analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    global emotion_classifier, TRANSFORMERS_AVAILABLE
    
    return {
        "status": "healthy",
        "transformers_available": TRANSFORMERS_AVAILABLE,
        "emotion_classifier_loaded": emotion_classifier is not None,
        "timestamp": datetime.now().isoformat(),
        "deployment": "vercel",
        "loading_strategy": "lazy"
    }

@router.get("/capabilities")
async def get_capabilities():
    """Get reflection agent capabilities"""
    return {
        "emotion_analysis": True,
        "introspective_insights": True,
        "cognitive_metrics": True,
        "constitutional_alignment": True,
        "transformers_backend": TRANSFORMERS_AVAILABLE,
        "fallback_analysis": True,
        "lazy_loading": True,
        "vercel_optimized": True,
        "supported_emotions": [
            "joy", "sadness", "anger", "fear", "surprise", "love", "neutral"
        ] if not TRANSFORMERS_AVAILABLE else "dynamic_from_model"
    }

@router.get("/warmup")
async def warmup():
    """Warmup endpoint to preload classifier"""
    classifier = await lazy_load_classifier()
    return {
        "status": "warmed_up",
        "classifier_loaded": classifier is not None,
        "timestamp": datetime.now().isoformat()
    }

# Export the main components
__all__ = [
    'router',
    'ReflectionInput', 
    'ReflectionOutput',
    'EmotionResult',
    'lazy_load_classifier',
    'fallback_emotion_analysis',
    'generate_introspective_insights'
]
