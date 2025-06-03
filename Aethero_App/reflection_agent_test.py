# reflection_agent.py
# FastAPI-based Introspective Reflection Agent for AetheroOS
# Implements emotion analysis using Hugging Face Transformers

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import logging
from datetime import datetime

# Graceful import for transformers
try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
    print("✅ Transformers imported successfully")
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️ Transformers not available")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("🔍 Creating FastAPI router...")

# Create FastAPI router
router = APIRouter(prefix="/reflection", tags=["reflection"])

print("✅ Router created successfully")

# Initialize emotion classifier if transformers is available
if TRANSFORMERS_AVAILABLE:
    try:
        emotion_classifier = pipeline(
            "text-classification", 
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
        logger.info("✅ Emotion classifier loaded successfully")
        print("✅ Emotion classifier loaded")
    except Exception as e:
        logger.warning(f"⚠️ Failed to load emotion classifier: {e}")
        emotion_classifier = None
        print(f"⚠️ Failed to load emotion classifier: {e}")
else:
    emotion_classifier = None
    logger.warning("⚠️ Transformers not available - using fallback emotion analysis")

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

class IntrospectiveAnalysis(BaseModel):
    cognitive_load: int
    emotional_complexity: float
    temporal_focus: str
    constitutional_alignment: float

# Fallback emotion analysis for when transformers is not available
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
    
    # Normalize scores
    total_score = sum(scores.values())
    normalized_scores = {emotion: score/total_score for emotion, score in scores.items()}
    
    return [{"label": emotion, "score": score} for emotion, score in normalized_scores.items()]

def generate_introspective_insights(text: str, emotions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate introspective insights about the emotional analysis"""
    
    primary_emotion = emotions[0]["label"] if emotions else "neutral"
    emotion_diversity = len([e for e in emotions if e["score"] > 0.1])
    
    # Calculate cognitive metrics
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
    
    # Constitutional alignment (transparency, introspection, validation)
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
        
        # Perform emotion analysis
        if emotion_classifier and TRANSFORMERS_AVAILABLE:
            results = emotion_classifier(input_data.text)
            # Ensure results is a list
            if not isinstance(results, list):
                results = [results]
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
            introspective_insights=introspective_insights
        )
        
    except Exception as e:
        logger.error(f"Error in reflection analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "transformers_available": TRANSFORMERS_AVAILABLE,
        "emotion_classifier_loaded": emotion_classifier is not None,
        "timestamp": datetime.now().isoformat()
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
        "supported_emotions": [
            "joy", "sadness", "anger", "fear", "surprise", "love", "neutral"
        ] if not TRANSFORMERS_AVAILABLE else "dynamic_from_model"
    }

# Export the main components
__all__ = [
    'router',
    'ReflectionInput', 
    'ReflectionOutput',
    'EmotionResult',
    'IntrospectiveAnalysis',
    'fallback_emotion_analysis',
    'generate_introspective_insights'
]

print("✅ reflection_agent module setup complete")
