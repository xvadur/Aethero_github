# metrics.py
# Introspektívne metriky pre kognitívnu analýzu Aethero systému

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import statistics
import json
from .models import ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, TemporalContextEnum

class CognitiveMetricsAnalyzer:
    """
    Introspektívny analyzátor metrík pre hlbokú kognitívnu analýzu
    ASL tagov a procesov vedomia v systéme Aethero
    """
    
    def __init__(self):
        self.analysis_session_id = datetime.now().isoformat()
        self.cognitive_flow_history = []
    
    def calculate_consciousness_coherence_rate(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        Výpočet miery koherencie vedomia na základe introspektívnych tagov
        
        Args:
            cognitive_tags: Zoznam validovaných ASL kognitívnych tagov
            
        Returns:
            Miera koherencie vedomia (0.0 - 1.0)
        """
        if not cognitive_tags:
            return 0.0
        
        coherence_scores = []
        for tag in cognitive_tags:
            # Analýza koherencie medzi mentálnym stavom a emočným tónom
            mental_emotion_coherence = self._assess_mental_emotion_coherence(
                tag.mental_state, tag.emotion_tone
            )
            
            # Analýza koherencie medzi kognitívnou záťažou a istotou
            load_certainty_coherence = self._assess_load_certainty_coherence(
                tag.cognitive_load, tag.certainty_level
            )
            
            # Analýza temporálnej koherencie
            temporal_coherence = self._assess_temporal_coherence(
                tag.temporal_context, tag.cognitive_load
            )
            
            # Celková koherencia pre tag
            tag_coherence = (
                mental_emotion_coherence * 0.4 +
                load_certainty_coherence * 0.4 +
                temporal_coherence * 0.2
            )
            
            coherence_scores.append(tag_coherence)
        
        return statistics.mean(coherence_scores) if coherence_scores else 0.0
    
    def _assess_mental_emotion_coherence(self, mental_state: MentalStateEnum, emotion_tone: EmotionToneEnum) -> float:
        """Hodnotenie koherencie medzi mentálnym stavom a emočným tónom"""
        coherence_matrix = {
            MentalStateEnum.CALM: {
                EmotionToneEnum.NEUTRAL: 1.0,
                EmotionToneEnum.POSITIVE: 0.8,
                EmotionToneEnum.ANALYTICAL: 0.7,
                EmotionToneEnum.EMPATHETIC: 0.9,
                EmotionToneEnum.NEGATIVE: 0.3,
                EmotionToneEnum.CRITICAL: 0.4
            },
            MentalStateEnum.FOCUSED: {
                EmotionToneEnum.ANALYTICAL: 1.0,
                EmotionToneEnum.NEUTRAL: 0.9,
                EmotionToneEnum.POSITIVE: 0.7,
                EmotionToneEnum.CRITICAL: 0.8,
                EmotionToneEnum.EMPATHETIC: 0.5,
                EmotionToneEnum.NEGATIVE: 0.4
            },
            MentalStateEnum.CONTEMPLATIVE: {
                EmotionToneEnum.NEUTRAL: 1.0,
                EmotionToneEnum.ANALYTICAL: 0.9,
                EmotionToneEnum.EMPATHETIC: 0.8,
                EmotionToneEnum.POSITIVE: 0.6,
                EmotionToneEnum.CRITICAL: 0.7,
                EmotionToneEnum.NEGATIVE: 0.5
            },
            MentalStateEnum.CONFUSED: {
                EmotionToneEnum.NEGATIVE: 0.8,
                EmotionToneEnum.NEUTRAL: 0.7,
                EmotionToneEnum.CRITICAL: 0.6,
                EmotionToneEnum.ANALYTICAL: 0.5,
                EmotionToneEnum.POSITIVE: 0.3,
                EmotionToneEnum.EMPATHETIC: 0.4
            }
        }
        
        return coherence_matrix.get(mental_state, {}).get(emotion_tone, 0.5)
    
    def _assess_load_certainty_coherence(self, cognitive_load: int, certainty_level: float) -> float:
        """Hodnotenie koherencie medzi kognitívnou záťažou a úrovňou istoty"""
        # Vysoká kognitívna záťaž by mala korešpondovať s vysokou alebo nízkou istotou
        # (vysoká istota = dobre pochopený zložitý problém, nízka istota = nejasný zložitý problém)
        
        if cognitive_load >= 8:
            # Vysoká záťaž - istota môže byť extrémna
            if certainty_level >= 0.8 or certainty_level <= 0.3:
                return 1.0
            else:
                return 0.6
        elif cognitive_load <= 3:
            # Nízka záťaž - mierka istota je vhodná
            if 0.4 <= certainty_level <= 0.8:
                return 1.0
            else:
                return 0.5
        else:
            # Stredná záťaž - stredná istota
            if 0.3 <= certainty_level <= 0.9:
                return 1.0
            else:
                return 0.7
    
    def _assess_temporal_coherence(self, temporal_context, cognitive_load: int) -> float:
        """Hodnotenie temporálnej koherencie"""
        # Súčasné a okamžité kontexty vyžadujú vyššiu kognitívnu záťaž
        immediate_contexts = [TemporalContextEnum.PRESENT]
        
        if temporal_context in immediate_contexts:
            return 1.0 if cognitive_load >= 5 else 0.7
        else:
            return 1.0 if cognitive_load <= 7 else 0.8
    
    def analyze_cognitive_evolution(self, cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """
        Analýza evolúcie kognitívnych procesov v čase
        
        Args:
            cognitive_tags: Chronologicky usporiadané kognitívne tagy
            
        Returns:
            Analýza kognitívnej evolúcie
        """
        if len(cognitive_tags) < 2:
            return {"insufficient_data": True}
        
        # Analýza trendov v kognitívnej záťaži
        load_trend = self._calculate_trend([tag.cognitive_load for tag in cognitive_tags])
        
        # Analýza trendov v istote
        certainty_trend = self._calculate_trend([tag.certainty_level for tag in cognitive_tags])
        
        # Analýza stability mentálneho stavu
        mental_state_stability = self._calculate_stability([tag.mental_state.value for tag in cognitive_tags])
        
        # Analýza emocionálnej stability
        emotion_stability = self._calculate_stability([tag.emotion_tone.value for tag in cognitive_tags])
        
        return {
            "cognitive_load_trend": load_trend,
            "certainty_trend": certainty_trend,
            "mental_state_stability": mental_state_stability,
            "emotion_stability": emotion_stability,
            "overall_cognitive_evolution": self._assess_overall_evolution(
                load_trend, certainty_trend, mental_state_stability, emotion_stability
            ),
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    def _calculate_trend(self, values: List[float]) -> Dict[str, Any]:
        """Výpočet trendu v číselných hodnotách"""
        if len(values) < 2:
            return {"trend": "insufficient_data"}
        
        # Jednoduchá lineárna regresia
        n = len(values)
        x_values = list(range(n))
        
        sum_x = sum(x_values)
        sum_y = sum(values)
        sum_xy = sum(x * y for x, y in zip(x_values, values))
        sum_x2 = sum(x * x for x in x_values)
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
        
        if slope > 0.1:
            trend = "increasing"
        elif slope < -0.1:
            trend = "decreasing"
        else:
            trend = "stable"
        
        return {
            "trend": trend,
            "slope": slope,
            "values": values,
            "variance": statistics.variance(values) if len(values) > 1 else 0
        }
    
    def _calculate_stability(self, values: List[str]) -> Dict[str, Any]:
        """Výpočet stability kategorických hodnôt"""
        if not values:
            return {"stability": 0.0}
        
        unique_values = len(set(values))
        total_values = len(values)
        
        stability_score = 1.0 - (unique_values - 1) / max(1, total_values - 1)
        
        return {
            "stability_score": stability_score,
            "unique_values": unique_values,
            "total_values": total_values,
            "most_frequent": max(set(values), key=values.count) if values else None
        }
    
    def _assess_overall_evolution(self, load_trend, certainty_trend, mental_stability, emotion_stability) -> str:
        """Celkové hodnotenie kognitívnej evolúcie"""
        if (load_trend["trend"] == "increasing" and 
            certainty_trend["trend"] == "increasing" and 
            mental_stability["stability_score"] > 0.7):
            return "positive_cognitive_growth"
        
        elif (load_trend["trend"] == "decreasing" and 
              certainty_trend["trend"] == "decreasing"):
            return "cognitive_simplification"
        
        elif (mental_stability["stability_score"] < 0.5 or 
              emotion_stability["stability_score"] < 0.5):
            return "cognitive_instability"
        
        else:
            return "stable_cognitive_state"

    def generate_introspective_report(self, cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """
        Generovanie komplexného introspektívneho reportu
        
        Args:
            cognitive_tags: Zoznam kognitívnych tagov na analýzu
            
        Returns:
            Komplexný introspektívny report
        """
        consciousness_coherence = self.calculate_consciousness_coherence_rate(cognitive_tags)
        cognitive_evolution = self.analyze_cognitive_evolution(cognitive_tags)
        
        # Štatistiky kognitívnej záťaže
        cognitive_loads = [tag.cognitive_load for tag in cognitive_tags]
        load_stats = {
            "mean": statistics.mean(cognitive_loads) if cognitive_loads else 0,
            "median": statistics.median(cognitive_loads) if cognitive_loads else 0,
            "stdev": statistics.stdev(cognitive_loads) if len(cognitive_loads) > 1 else 0,
            "min": min(cognitive_loads) if cognitive_loads else 0,
            "max": max(cognitive_loads) if cognitive_loads else 0
        }
        
        # Štatistiky istoty
        certainty_levels = [tag.certainty_level for tag in cognitive_tags]
        certainty_stats = {
            "mean": statistics.mean(certainty_levels) if certainty_levels else 0,
            "median": statistics.median(certainty_levels) if certainty_levels else 0,
            "stdev": statistics.stdev(certainty_levels) if len(certainty_levels) > 1 else 0,
            "min": min(certainty_levels) if certainty_levels else 0,
            "max": max(certainty_levels) if certainty_levels else 0
        }
        
        return {
            "session_id": self.analysis_session_id,
            "total_tags_analyzed": len(cognitive_tags),
            "consciousness_coherence_rate": consciousness_coherence,
            "cognitive_evolution_analysis": cognitive_evolution,
            "cognitive_load_statistics": load_stats,
            "certainty_level_statistics": certainty_stats,
            "introspective_insights": self._generate_introspective_insights(
                consciousness_coherence, cognitive_evolution, load_stats, certainty_stats
            ),
            "aethero_constitutional_compliance": self._assess_constitutional_compliance(cognitive_tags),
            "report_generation_timestamp": datetime.now().isoformat()
        }
    
    def _generate_introspective_insights(self, coherence_rate, evolution, load_stats, certainty_stats) -> List[str]:
        """Generovanie introspektívnych pozorovaní"""
        insights = []
        
        if coherence_rate > 0.8:
            insights.append("Vysoká miera koherencie vedomia - systém vykazuje konštantnú introspektívnu kvalitu")
        elif coherence_rate < 0.5:
            insights.append("Nízka koherencia vedomia - potreba hlbšieji introspektívnej analýzy")
        
        if load_stats["mean"] > 7:
            insights.append("Vysoká priemerná kognitívna záťaž - systém spracováva komplexné myšlienky")
        elif load_stats["mean"] < 3:
            insights.append("Nízka kognitívna záťaž - možnosť pre hlbšiu analýzu")
        
        if certainty_stats["stdev"] > 0.3:
            insights.append("Vysoká variabilita istoty - systém prechádza rôznymi úrovňami kognitívnej istoty")
        
        if evolution.get("overall_cognitive_evolution") == "positive_cognitive_growth":
            insights.append("Pozitívny kognitívny rast - systém sa vyvíja smerom k vyššej introspektívnej kvalite")
        
        return insights
    
    def _assess_constitutional_compliance(self, cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """Hodnotenie súladu s ústavnými princípmi Aethero"""
        compliance_factors = {
            "transparency": all(tag.consciousness_level >= 0.3 for tag in cognitive_tags),
            "introspective_depth": all(tag.introspective_depth >= 0.3 for tag in cognitive_tags),
            "constitutional_law_references": all(bool(tag.constitutional_law) for tag in cognitive_tags),
            "memory_linkage": all(bool(tag.aeth_mem_link) for tag in cognitive_tags)
        }
        
        compliance_score = sum(compliance_factors.values()) / len(compliance_factors)
        
        return {
            "overall_compliance_score": compliance_score,
            "compliance_factors": compliance_factors,
            "constitutional_status": "compliant" if compliance_score >= 0.8 else "needs_improvement"
        }


# Zachovanie spätnej kompatibility
def calculate_success_rate(validated_blocks: int, total_blocks: int) -> float:
    """Legacy function - calculate the success rate of parsing."""
    if total_blocks == 0:
        return 0.0
    return validated_blocks / total_blocks

def analyze_cognitive_load(tags: list) -> dict:
    """Legacy function - analyze cognitive load from a list of ASL tags."""
    loads = [tag.get("cognitive_load", 0) for tag in tags]
    return {
        "average_load": sum(loads) / len(loads) if loads else 0,
        "max_load": max(loads, default=0),
        "min_load": min(loads, default=0),
    }

def generate_introspection_report(tags: list) -> dict:
    """Legacy function - generate a report based on introspective tags."""
    return {
        "certainty_levels": [tag.get("certainty_level", 0.0) for tag in tags],
        "memory_links": [tag.get("aeth_mem_link", "") for tag in tags],
    }
