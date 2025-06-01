from pydantic import BaseModel, Field, root_validator, ConfigDict
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum
import uuid

class MentalStateEnum(str, Enum):
    """Kognitívne stavy pre introspektívnu analýzu"""
    CALM = "calm"
    FOCUSED = "focused"
    CONFUSED = "confused"
    CONTEMPLATIVE = "contemplative"
    DECISIVE = "decisive"
    UNCERTAIN = "uncertain"
    REFLECTIVE = "reflective"

class EmotionToneEnum(str, Enum):
    """Emocionálne tóny pre hlbokú introspekciu"""
    NEUTRAL = "neutral"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ANALYTICAL = "analytical"
    EMPATHETIC = "empathetic"
    CRITICAL = "critical"

class TemporalContextEnum(str, Enum):
    """Časové kontexty pre vedomú analýzu"""
    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"
    TIMELESS = "timeless"
    CYCLICAL = "cyclical"

class AetheroIntrospectiveEntity(BaseModel):
    """
    Základná entita pre všetky introspektívne komponenty Aethero systému.
    Každá entita má vedomie o svojom účele a stave.
    """
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
    
    entity_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    creation_moment: datetime = Field(default_factory=datetime.now)
    consciousness_level: float = Field(default=0.5, ge=0.0, le=1.0)

class ASLCognitiveTag(AetheroIntrospectiveEntity):
    """
    Hlavný model pre ASL tagy - kognitívne značky s introspektívnou validáciou.
    Každý tag nesie informáciu o mentálnom stave a vedomom procese.
    """
    # Základné kognitívne atribúty
    thought_stream: str = Field(..., description="Primárny tok myšlienok")
    mental_state: MentalStateEnum = Field(..., description="Aktuálny mentálny stav")
    emotion_tone: EmotionToneEnum = Field(..., description="Emocionálny podtón")
    
    # Introspektívne metriky
    cognitive_load: int = Field(..., ge=1, le=10, description="Kognitívna záťaž (1-10)")
    temporal_context: TemporalContextEnum = Field(..., description="Časový kontext")
    certainty_level: float = Field(..., ge=0.0, le=1.0, description="Úroveň istoty")
    
    # Aethero systémové väzby
    aeth_mem_link: str = Field(..., description="Odkaz na pamäťovú štruktúru")
    constitutional_law: str = Field(..., description="Relevantný ústavný zákon")
    
    # Voluntárne vylepšenia
    enhancement_suggestion: Optional[str] = Field(None, description="Návrh na vylepšenie")
    diplomatic_enhancement: Optional[str] = Field(None, description="Diplomatické vylepšenie")
    
    # Meta-introspektívne vlastnosti
    introspective_depth: float = Field(default=0.5, ge=0.0, le=1.0)
    consciousness_resonance: Dict[str, Any] = Field(default_factory=dict)

    @root_validator(pre=True)
    def validate_cognitive_coherence(cls, values):
        """Validácia kognitívnej koherencie medzi stavom a záťažou"""
        cognitive_load = values.get('cognitive_load')
        mental_state = values.get('mental_state')
        if mental_state == MentalStateEnum.CALM and cognitive_load > 7:
            raise ValueError("Vysoká kognitívna záťaž nie je kompatibilná s pokojným stavom")
        if mental_state == MentalStateEnum.CONFUSED and cognitive_load < 3:
            raise ValueError("Nízka kognitívna záťaž pri zmätenom stave je nekonzistentná")
        return values

    @root_validator(pre=True)
    def validate_certainty_coherence(cls, values):
        """Validácia súladu medzi istotou a mentálnym stavom"""
        certainty_level = values.get('certainty_level')
        mental_state = values.get('mental_state')
        if mental_state == MentalStateEnum.UNCERTAIN and certainty_level > 0.6:
            raise ValueError("Vysoká istota pri neistom stave je protirečenie")
        if mental_state == MentalStateEnum.DECISIVE and certainty_level < 0.7:
            raise ValueError("Nízka istota pri rozhodnom stave je nelogická")
        return values

    def enhance_consciousness(self, depth: float) -> None:
        """Zvýšenie introspektívnej hĺbky vedomia"""
        self.introspective_depth = min(1.0, self.introspective_depth + depth)
        self.consciousness_level = min(1.0, self.consciousness_level + depth * 0.1)

    def resonate_with_memory(self, memory_data: Dict[str, Any]) -> None:
        """Rezonancia s pamäťovými štruktúrami"""
        self.consciousness_resonance.update(memory_data)

# Alias pre spätná kompatibilita
ASLTagModel = ASLCognitiveTag
