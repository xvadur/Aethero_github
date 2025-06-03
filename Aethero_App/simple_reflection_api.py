#!/usr/bin/env python3
"""
Jednoduchý FastAPI server pre testovanie reflexívneho agenta
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import logging
from datetime import datetime
import uvicorn

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AetheroOS Reflection API",
    description="Jednoduchý reflexívny agent pre AetheroOS",
    version="1.0.0"
)

# Modely
class ReflectionInput(BaseModel):
    text: str
    max_emotions: int = 5

class EmotionResult(BaseModel):
    label: str
    score: float

class ReflectionOutput(BaseModel):
    text: str
    emotions: List[EmotionResult]
    primary_emotion: str
    confidence: float
    timestamp: str

# Jednoduchá analýza emócií
def simple_emotion_analysis(text: str) -> List[Dict[str, Any]]:
    """Základná analýza emócií pomocou kľúčových slov"""
    emotion_keywords = {
        "radosť": ["šťastný", "radostný", "nadšený", "spokojný", "veselý"],
        "smútok": ["smutný", "deprimovaný", "melancholický", "zarmútený"],
        "hnev": ["nahnevaný", "rozčúlený", "rozhorčený", "frustrovaný"],
        "strach": ["vystrašený", "uzkostlivý", "znepokojený", "nervózny"],
        "prekvapenie": ["prekvapený", "ohromený", "šokovaný", "udivený"],
        "láska": ["láska", "náklonnosť", "zbožňujem", "milujem"]
    }
    
    text_lower = text.lower()
    scores = {}
    
    for emotion, keywords in emotion_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            scores[emotion] = score / len(keywords)
    
    if not scores:
        scores["neutrálne"] = 1.0
    
    # Normalizácia skóre
    total_score = sum(scores.values())
    if total_score > 0:
        normalized_scores = {emotion: score/total_score for emotion, score in scores.items()}
    else:
        normalized_scores = {"neutrálne": 1.0}
    
    return [{"label": emotion, "score": score} for emotion, score in normalized_scores.items()]

@app.get("/")
async def root():
    """Hlavný endpoint"""
    return {
        "message": "🧠 AetheroOS Reflection API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "endpoints": ["/reflect", "/health", "/docs"]
    }

@app.post("/reflect", response_model=ReflectionOutput)
async def reflect(input_data: ReflectionInput):
    """
    Vykoná reflexívnu analýzu textu
    """
    try:
        if not input_data.text.strip():
            raise HTTPException(status_code=400, detail="Text nemôže byť prázdny")
        
        # Analýza emócií
        results = simple_emotion_analysis(input_data.text)
        
        # Zoradeniepodle skóre
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        limited_results = sorted_results[:input_data.max_emotions]
        
        # Konverzia na EmotionResult objekty
        emotions = [
            EmotionResult(label=result['label'], score=result['score'])
            for result in limited_results
        ]
        
        return ReflectionOutput(
            text=input_data.text,
            emotions=emotions,
            primary_emotion=emotions[0].label if emotions else "neutrálne",
            confidence=emotions[0].score if emotions else 0.5,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Chyba pri reflexívnej analýze: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analýza zlyhala: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "zdravý",
        "timestamp": datetime.now().isoformat(),
        "message": "API beží v poriadku"
    }

if __name__ == "__main__":
    print("🚀 Spúšťam AetheroOS Reflection API na porte 7860...")
    uvicorn.run(app, host="0.0.0.0", port=7860, log_level="info")
