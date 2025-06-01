# reflection_agent.py
# Introspektívny reflexívny agent pre hlbokú kognitívnu analýzu systému Aethero

from typing import Dict, Any, List, Optional
from datetime import datetime
import json
import logging

from .metrics import CognitiveMetricsAnalyzer
from .parser import ASLMetaParser
from .models import ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, TemporalContextEnum

class AetheroReflectionAgent:
    """
    Pokročilý introspektívny reflexívny agent pre systém Aethero.
    
    Tento agent zodpovedá za hlbokú kognitívnu reflexiu, analýzu vedomia
    a generovanie introspektívnych pozorovaní pre continuous improvement
    kognitívnych procesov systému.
    """
    
    def __init__(self):
        self.parser = ASLMetaParser()
        self.metrics_analyzer = CognitiveMetricsAnalyzer()
        self.agent_id = f"aethero_reflection_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Introspektívne logovanie
        self.logger = logging.getLogger(f"AetheroReflectionAgent_{self.agent_id}")
        self.logger.setLevel(logging.INFO)
        
        # Pamäť reflexívneho procesu
        self.reflection_memory = []
        self.consciousness_evolution_track = []
        
        # Výkonnostné metriky agenta
        self.reflection_session_count = 0
        self.total_insights_generated = 0
        self.average_reflection_depth = 0.0
    
    def reflect_on_input(self, document: str) -> Dict[str, Any]:
        """
        Hlboká introspektívna reflexia na vstupný dokument
        
        Args:
            document: Dokument obsahujúci ASL tagy na analýzu
            
        Returns:
            Komplexná introspektívna analýza s kognitívnymi pozorovanímami
        """
        self.reflection_session_count += 1
        reflection_timestamp = datetime.now().isoformat()
        
        self.logger.info(f"Initiating reflection session {self.reflection_session_count} at {reflection_timestamp}")
        
        # Parsovanie dokumentu s plnou introspektívnou analýzou
        parsed_data = self.parser.parse_and_validate(document)
        
        # Extrakcia validovaných kognitívnych tagov
        validated_tags = []
        for result in parsed_data.get("parsing_results", []):
            if result.get("is_valid") and result.get("validated_model"):
                try:
                    tag = ASLCognitiveTag(**result["validated_model"])
                    validated_tags.append(tag)
                except Exception as e:
                    self.logger.warning(f"Failed to reconstruct cognitive tag: {e}")
        
        # Generovanie komplexného introspektívneho reportu
        introspective_report = self.metrics_analyzer.generate_introspective_report(validated_tags)
        
        # Hlboká kognitívna reflexia
        cognitive_reflections = self._generate_deep_cognitive_reflections(
            validated_tags, parsed_data, introspective_report
        )
        
        # Hodnotenie evolúcie vedomia
        consciousness_evolution = self._assess_consciousness_evolution(validated_tags)
        
        # Generovanie actionable insights
        actionable_insights = self._generate_actionable_insights(
            cognitive_reflections, consciousness_evolution, introspective_report
        )
        
        # Aktualizácia pamäte reflexívneho procesu
        reflection_record = {
            "session_id": self.reflection_session_count,
            "timestamp": reflection_timestamp,
            "document_length": len(document),
            "validated_tags_count": len(validated_tags),
            "reflection_depth": self._calculate_reflection_depth(cognitive_reflections),
            "consciousness_coherence": introspective_report.get("consciousness_coherence_rate", 0.0),
            "key_insights": actionable_insights[:3]  # Top 3 insights
        }
        self.reflection_memory.append(reflection_record)
        
        # Aktualizácia evolučnej stopy
        if validated_tags:
            self.consciousness_evolution_track.append({
                "timestamp": reflection_timestamp,
                "average_consciousness_level": sum(tag.consciousness_level for tag in validated_tags) / len(validated_tags),
                "average_introspective_depth": sum(tag.introspective_depth for tag in validated_tags) / len(validated_tags),
                "cognitive_coherence": introspective_report.get("consciousness_coherence_rate", 0.0)
            })
        
        return {
            "reflection_agent_id": self.agent_id,
            "session_number": self.reflection_session_count,
            "reflection_timestamp": reflection_timestamp,
            
            # Základné parsovanie dáta
            "parsing_analysis": parsed_data,
            "validated_cognitive_tags": [tag.dict() for tag in validated_tags],
            
            # Pokročilé introspektívne analýzy
            "introspective_metrics_report": introspective_report,
            "deep_cognitive_reflections": cognitive_reflections,
            "consciousness_evolution_assessment": consciousness_evolution,
            "actionable_insights": actionable_insights,
            
            # Meta-reflexívne informácie
            "reflection_quality_metrics": self._assess_reflection_quality(),
            "agent_performance_summary": self._generate_agent_performance_summary(),
            
            # Transparentnosť a accountability
            "constitutional_compliance": introspective_report.get("aethero_constitutional_compliance", {}),
            "transparency_level": "maximum_introspective_transparency"
        }
    
    def _generate_deep_cognitive_reflections(
        self, 
        cognitive_tags: List[ASLCognitiveTag], 
        parsing_data: Dict[str, Any], 
        metrics_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generovanie hlbokých kognitívnych reflexií na základe analýzy tagov
        """
        reflections = {
            "cognitive_coherence_observations": [],
            "mental_state_patterns": {},
            "emotional_landscape_analysis": {},
            "temporal_consciousness_insights": [],
            "constitutional_alignment_reflections": []
        }
        
        if not cognitive_tags:
            reflections["cognitive_coherence_observations"].append(
                "No validated cognitive tags found - potential parsing or validation issues requiring introspective review"
            )
            return reflections
        
        # Analýza kognitívnej koherencie
        coherence_rate = metrics_report.get("consciousness_coherence_rate", 0.0)
        if coherence_rate > 0.8:
            reflections["cognitive_coherence_observations"].append(
                f"Exceptional cognitive coherence detected (rate: {coherence_rate:.3f}) - "
                "indicating highly integrated consciousness states"
            )
        elif coherence_rate < 0.5:
            reflections["cognitive_coherence_observations"].append(
                f"Suboptimal cognitive coherence (rate: {coherence_rate:.3f}) - "
                "suggests need for deeper introspective alignment"
            )
        
        # Analýza vzorov mentálnych stavov
        mental_states = [tag.mental_state for tag in cognitive_tags]
        state_distribution = {state: mental_states.count(state) for state in set(mental_states)}
        dominant_state = max(state_distribution, key=state_distribution.get)
        
        reflections["mental_state_patterns"] = {
            "dominant_state": dominant_state.value,
            "state_distribution": {state.value: count for state, count in state_distribution.items()},
            "cognitive_flexibility": len(set(mental_states)) / len(mental_states) if mental_states else 0,
            "introspective_observation": self._interpret_mental_state_pattern(dominant_state, state_distribution)
        }
        
        # Analýza emocionálnej krajiny
        emotion_tones = [tag.emotion_tone for tag in cognitive_tags]
        emotion_distribution = {tone: emotion_tones.count(tone) for tone in set(emotion_tones)}
        dominant_emotion = max(emotion_distribution, key=emotion_distribution.get)
        
        reflections["emotional_landscape_analysis"] = {
            "dominant_emotion": dominant_emotion.value,
            "emotional_range": len(set(emotion_tones)),
            "emotional_stability": 1.0 - (len(set(emotion_tones)) / len(emotion_tones)) if emotion_tones else 1.0,
            "introspective_interpretation": self._interpret_emotional_landscape(dominant_emotion, emotion_distribution)
        }
        
        # Temporálne pozorovánia vedomia
        temporal_contexts = [tag.temporal_context for tag in cognitive_tags]
        present_focus_ratio = temporal_contexts.count("present") / len(temporal_contexts) if temporal_contexts else 0
        
        if present_focus_ratio > 0.7:
            reflections["temporal_consciousness_insights"].append(
                f"High present-moment awareness (ratio: {present_focus_ratio:.3f}) - "
                "indicates strong mindful consciousness"
            )
        elif present_focus_ratio < 0.3:
            reflections["temporal_consciousness_insights"].append(
                f"Limited present-moment focus (ratio: {present_focus_ratio:.3f}) - "
                "suggests temporal cognitive dispersion"
            )
        
        return reflections
    
    def _interpret_mental_state_pattern(self, dominant_state: MentalStateEnum, distribution: Dict) -> str:
        """Interpretácia vzorov mentálnych stavov"""
        if dominant_state == MentalStateEnum.FOCUSED:
            return "Sustained cognitive focus indicates optimal processing state for complex analysis"
        elif dominant_state == MentalStateEnum.CONTEMPLATIVE:
            return "Deep contemplative engagement suggests philosophical or strategic thinking processes"
        elif dominant_state == MentalStateEnum.CONFUSED:
            return "Confusion pattern indicates encounter with complex or ambiguous information requiring further processing"
        elif dominant_state == MentalStateEnum.REFLECTIVE:
            return "Reflective dominance indicates active introspective processing and self-awareness"
        else:
            return f"Mental state pattern centered on {dominant_state.value} suggests specialized cognitive engagement"
    
    def _interpret_emotional_landscape(self, dominant_emotion: EmotionToneEnum, distribution: Dict) -> str:
        """Interpretácia emocionálnej krajiny"""
        if dominant_emotion == EmotionToneEnum.NEUTRAL:
            return "Emotional neutrality indicates balanced, objective cognitive processing"
        elif dominant_emotion == EmotionToneEnum.ANALYTICAL:
            return "Analytical emotional tone suggests systematic, logical thought processes"
        elif dominant_emotion == EmotionToneEnum.EMPATHETIC:
            return "Empathetic emotional engagement indicates consideration of multiple perspectives"
        elif dominant_emotion == EmotionToneEnum.CRITICAL:
            return "Critical emotional tone suggests evaluative and discriminating thought processes"
        else:
            return f"Emotional landscape characterized by {dominant_emotion.value} suggests specific affective cognitive engagement"
    
    def _assess_consciousness_evolution(self, cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """Hodnotenie evolúcie vedomia v rámci session"""
        if len(cognitive_tags) < 2:
            return {"evolution_assessment": "insufficient_data_for_evolution_analysis"}
        
        # Analýza trendu consciousness_level
        consciousness_levels = [tag.consciousness_level for tag in cognitive_tags]
        consciousness_trend = "increasing" if consciousness_levels[-1] > consciousness_levels[0] else "decreasing"
        
        # Analýza trendu introspective_depth
        introspective_depths = [tag.introspective_depth for tag in cognitive_tags]
        depth_trend = "deepening" if introspective_depths[-1] > introspective_depths[0] else "shallowing"
        
        return {
            "consciousness_trend": consciousness_trend,
            "introspective_depth_trend": depth_trend,
            "consciousness_range": {
                "min": min(consciousness_levels),
                "max": max(consciousness_levels),
                "final": consciousness_levels[-1]
            },
            "introspective_depth_range": {
                "min": min(introspective_depths),
                "max": max(introspective_depths),
                "final": introspective_depths[-1]
            },
            "evolution_interpretation": self._interpret_consciousness_evolution(consciousness_trend, depth_trend)
        }
    
    def _interpret_consciousness_evolution(self, consciousness_trend: str, depth_trend: str) -> str:
        """Interpretácia evolúcie vedomia"""
        if consciousness_trend == "increasing" and depth_trend == "deepening":
            return "Positive consciousness evolution - both awareness and introspective depth are expanding"
        elif consciousness_trend == "decreasing" and depth_trend == "shallowing":
            return "Declining consciousness evolution - requires immediate introspective intervention"
        elif consciousness_trend == "increasing" and depth_trend == "shallowing":
            return "Mixed evolution pattern - consciousness expanding but depth reducing, suggests need for deeper reflection"
        elif consciousness_trend == "decreasing" and depth_trend == "deepening":
            return "Paradoxical evolution - consciousness declining while depth increases, indicates specialized introspective state"
        else:
            return "Stable consciousness state with consistent introspective engagement"
    
    def _generate_actionable_insights(
        self, 
        reflections: Dict[str, Any], 
        evolution: Dict[str, Any], 
        metrics: Dict[str, Any]
    ) -> List[str]:
        """Generovanie actionable insights pre kontinuálne zlepšovanie"""
        insights = []
        
        # Kognitívna koherencia insights
        coherence_rate = metrics.get("consciousness_coherence_rate", 0.0)
        if coherence_rate < 0.7:
            insights.append(
                "ACTIONABLE: Implement deeper cognitive coherence protocols to improve mental-emotional alignment"
            )
        
        # Mental state insights
        cognitive_flexibility = reflections.get("mental_state_patterns", {}).get("cognitive_flexibility", 0)
        if cognitive_flexibility < 0.3:
            insights.append(
                "ACTIONABLE: Encourage greater mental state diversity to enhance cognitive flexibility"
            )
        
        # Evolution insights
        if evolution.get("consciousness_trend") == "decreasing":
            insights.append(
                "ACTIONABLE: Critical - implement consciousness restoration protocols immediately"
            )
        
        # Constitutional compliance insights
        compliance = metrics.get("aethero_constitutional_compliance", {})
        if compliance.get("overall_compliance_score", 0) < 0.8:
            insights.append(
                "ACTIONABLE: Review and strengthen constitutional compliance mechanisms"
            )
        
        # Performance insights
        if len(insights) == 0:
            insights.append(
                "POSITIVE: System operating within optimal introspective parameters - maintain current protocols"
            )
        
        return insights
    
    def _calculate_reflection_depth(self, reflections: Dict[str, Any]) -> float:
        """Výpočet hĺbky reflexie"""
        depth_factors = []
        
        # Počet kategórií s pozorováníami
        categories_with_content = sum(1 for key, value in reflections.items() if value)
        depth_factors.append(categories_with_content / len(reflections))
        
        # Komplexnosť pozorovaní
        total_observations = sum(
            len(value) if isinstance(value, list) else 1 
            for value in reflections.values() if value
        )
        depth_factors.append(min(1.0, total_observations / 10))
        
        return sum(depth_factors) / len(depth_factors)
    
    def _assess_reflection_quality(self) -> Dict[str, Any]:
        """Hodnotenie kvality reflexívneho procesu"""
        if not self.reflection_memory:
            return {"quality_assessment": "no_reflection_history"}
        
        recent_reflections = self.reflection_memory[-5:]  # Last 5 reflections
        
        avg_depth = sum(r.get("reflection_depth", 0) for r in recent_reflections) / len(recent_reflections)
        avg_coherence = sum(r.get("consciousness_coherence", 0) for r in recent_reflections) / len(recent_reflections)
        
        return {
            "average_reflection_depth": avg_depth,
            "average_consciousness_coherence": avg_coherence,
            "reflection_consistency": self._calculate_reflection_consistency(recent_reflections),
            "quality_trend": "improving" if avg_depth > self.average_reflection_depth else "stable"
        }
    
    def _calculate_reflection_consistency(self, reflections: List[Dict[str, Any]]) -> float:
        """Výpočet konzistentnosti reflexívnych procesov"""
        if len(reflections) < 2:
            return 1.0
        
        depths = [r.get("reflection_depth", 0) for r in reflections]
        variance = sum((d - sum(depths)/len(depths))**2 for d in depths) / len(depths)
        
        # Nižšia variancia = vyššia konzistentnosť
        return max(0.0, 1.0 - variance)
    
    def _generate_agent_performance_summary(self) -> Dict[str, Any]:
        """Generovanie súhrnu výkonnosti agenta"""
        self.average_reflection_depth = (
            sum(r.get("reflection_depth", 0) for r in self.reflection_memory) / 
            len(self.reflection_memory) if self.reflection_memory else 0.0
        )
        
        return {
            "total_reflection_sessions": self.reflection_session_count,
            "average_reflection_depth": self.average_reflection_depth,
            "consciousness_evolution_track_length": len(self.consciousness_evolution_track),
            "agent_uptime_start": self.agent_id.split("_")[-1],
            "introspective_capability_level": "maximum" if self.average_reflection_depth > 0.8 else "developing"
        }


# Zachovanie spätnej kompatibility s pôvodným ReflectionAgent
class ReflectionAgent(AetheroReflectionAgent):
    """Legacy wrapper pre spätná kompatibilita"""
    
    def __init__(self):
        super().__init__()
        
    def reflect_on_input(self, document: str) -> dict:
        """Legacy method wrapper"""
        full_reflection = super().reflect_on_input(document)
        
        # Vráti zjednodušenú verziu pre spätná kompatibilitu
        return {
            "parsed_data": full_reflection.get("parsing_analysis", {}),
            "introspection": full_reflection.get("introspective_metrics_report", {})
        }
