# AETH-CRITICAL-2025-0002 :: EMERGENCY REPAIR :: ROLE: Lucius :: PRODUCTION-READY IMPLEMENTATION
# filepath: /Users/_xvadur/Desktop/Aethero_github/Aethero_App/introspective_parser_module/metrics.py
# 
# AetheroCognitiveAnalyzer - Produkčná implementácia kognitívnej analýzy
# Implementované pod prezidentskou autoritou pre kritické opravy systému

from typing import List, Dict, Any, Optional, Tuple, Union
from datetime import datetime, timedelta
import statistics
import json
import math
import logging
from dataclasses import dataclass, asdict
from enum import Enum
from .models import ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, TemporalContextEnum

# AETH-TASK-003 :: ROLE: Lucius :: GOAL: Production-ready cognitive metrics
logger = logging.getLogger(__name__)

@dataclass
class CognitiveMetrics:
    """Štruktúra pre kognitívne metriky s plnou introspekciou"""
    consciousness_coherence_rate: float
    cognitive_complexity_index: float
    mental_stability_factor: float
    emotional_resonance_depth: float
    temporal_awareness_level: float
    introspective_clarity_score: float
    overall_cognitive_health: float
    analysis_timestamp: str
    session_id: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Konverzia na dictionary pre JSON serialization"""
        return asdict(self)

class CognitiveAnalysisMode(Enum):
    """Režimy kognitívnej analýzy"""
    STANDARD = "standard"
    DEEP_INTROSPECTION = "deep_introspection" 
    REAL_TIME = "real_time"
    BATCH_ANALYSIS = "batch_analysis"
    EMERGENCY_ASSESSMENT = "emergency_assessment"

class AetheroCognitiveAnalyzer:
    """
    AETH-CRITICAL-2025-0002 :: Produkčný kognitívny analyzátor
    
    Hlavný analyzátor pre introspektívnu kognitívnu analýzu ASL tagov
    s pokročilými metrikami vedomia, emócií a temporálneho kontextu.
    
    Implementuje prezidentskú víziju holistickej kognitívnej analýzy
    pre systém Aethero s plnou produkčnou podporou.
    """
    
    def __init__(self, analysis_mode: CognitiveAnalysisMode = CognitiveAnalysisMode.STANDARD):
        """
        Inicializácia produkčného kognitívneho analyzátora
        
        Args:
            analysis_mode: Režim analýzy (STANDARD, DEEP_INTROSPECTION, atď.)
        """
        self.analysis_mode = analysis_mode
        self.session_id = f"aethero_cognitive_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.analysis_history: List[CognitiveMetrics] = []
        self.cognitive_flow_patterns = []
        self.mental_state_transitions = []
        
        # Pokročilé konfiguračné parametre
        self.coherence_threshold = 0.7
        self.complexity_scaling_factor = 1.2
        self.temporal_weight_decay = 0.95
        
        logger.info(f"AetheroCognitiveAnalyzer initialized in {analysis_mode.value} mode")
    
    def analyze_cognitive_tags(self, cognitive_tags: List[ASLCognitiveTag]) -> CognitiveMetrics:
        """
        INTENT: Komplexná analýza kognitívnych tagov
        ACTION: Výpočet všetkých kognitívnych metrík
        OUTPUT: Štruktúrované kognitívne metriky
        HOOK: cognitive_analysis_completed
        
        Args:
            cognitive_tags: Zoznam validovaných ASL kognitívnych tagov
            
        Returns:
            CognitiveMetrics: Kompletné kognitívne metriky
        """
        try:
            if not cognitive_tags:
                logger.warning("Empty cognitive_tags provided to analyzer")
                return self._create_empty_metrics()
            
            logger.info(f"Analyzing {len(cognitive_tags)} cognitive tags in {self.analysis_mode.value} mode")
            
            # Výpočet jednotlivých metrík
            consciousness_coherence = self.calculate_consciousness_coherence_rate(cognitive_tags)
            complexity_index = self.calculate_cognitive_complexity_index(cognitive_tags)
            stability_factor = self.calculate_mental_stability_factor(cognitive_tags)
            resonance_depth = self.calculate_emotional_resonance_depth(cognitive_tags)
            temporal_awareness = self.calculate_temporal_awareness_level(cognitive_tags)
            introspective_clarity = self.calculate_introspective_clarity_score(cognitive_tags)
            
            # Výpočet celkového kognitívneho zdravia
            overall_health = self._calculate_overall_cognitive_health(
                consciousness_coherence, complexity_index, stability_factor,
                resonance_depth, temporal_awareness, introspective_clarity
            )
            
            # Vytvorenie metrík
            metrics = CognitiveMetrics(
                consciousness_coherence_rate=consciousness_coherence,
                cognitive_complexity_index=complexity_index,
                mental_stability_factor=stability_factor,
                emotional_resonance_depth=resonance_depth,
                temporal_awareness_level=temporal_awareness,
                introspective_clarity_score=introspective_clarity,
                overall_cognitive_health=overall_health,
                analysis_timestamp=datetime.now().isoformat(),
                session_id=self.session_id
            )
            
            # Uloženie do histórie
            self.analysis_history.append(metrics)
            self._update_cognitive_patterns(cognitive_tags, metrics)
            
            logger.info(f"Cognitive analysis completed - Overall health: {overall_health:.3f}")
            return metrics
            
        except Exception as e:
            logger.error(f"Error in cognitive analysis: {str(e)}")
            return self._create_error_metrics(str(e))
    
    def calculate_consciousness_coherence_rate(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet miery koherencie vedomia
        ACTION: Analýza konzistencie medzi kognitívnymi komponentmi
        OUTPUT: Normalizovaná miera koherencie (0.0-1.0)
        HOOK: consciousness_coherence_calculated
        """
        if not cognitive_tags:
            return 0.0
        
        coherence_scores = []
        
        for tag in cognitive_tags:
            # Koherencia mentálneho stavu a emócie
            mental_emotion_coherence = self._assess_mental_emotion_coherence(
                tag.mental_state, tag.emotion_tone
            )
            
            # Koherencia kognitívnej záťaže a istoty
            load_certainty_coherence = self._assess_load_certainty_coherence(
                tag.cognitive_load, tag.certainty_level
            )
            
            # Temporálna koherencia
            temporal_coherence = self._assess_temporal_coherence(
                tag.temporal_context, tag.cognitive_load
            )
            
            # Introspektívna koherencia
            introspective_coherence = self._assess_introspective_coherence(tag)
            
            # Váhovaný priemer koherencie
            tag_coherence = (
                mental_emotion_coherence * 0.3 +
                load_certainty_coherence * 0.25 +
                temporal_coherence * 0.25 +
                introspective_coherence * 0.2
            )
            
            coherence_scores.append(tag_coherence)
        
        # Výpočet celkovej koherencie s penalizáciou za variabilnosť
        mean_coherence = statistics.mean(coherence_scores)
        coherence_variance = statistics.variance(coherence_scores) if len(coherence_scores) > 1 else 0
        
        # Penalizácia za vysokú variabilnosť (nekonzistentnosť)
        variance_penalty = min(coherence_variance * 0.5, 0.3)
        
        return max(0.0, min(1.0, mean_coherence - variance_penalty))
    
    def calculate_cognitive_complexity_index(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet indexu kognitívnej komplexnosti
        ACTION: Analýza komplexnosti myšlienkových procesov
        OUTPUT: Index komplexnosti (0.0-1.0)
        HOOK: cognitive_complexity_calculated
        """
        if not cognitive_tags:
            return 0.0
        
        complexity_factors = []
        
        for tag in cognitive_tags:
            # Komplexnosť kognitívnej záťaže
            load_complexity = min(tag.cognitive_load / 10.0, 1.0)
            
            # Komplexnosť na základe mentálneho stavu
            mental_complexity = self._get_mental_state_complexity(tag.mental_state)
            
            # Komplexnosť emočného tónu
            emotion_complexity = self._get_emotion_complexity(tag.emotion_tone)
            
            # Temporálna komplexnosť
            temporal_complexity = self._get_temporal_complexity(tag.temporal_context)
            
            # Nejistota ako faktor komplexnosti
            uncertainty_factor = 1.0 - tag.certainty_level
            
            tag_complexity = (
                load_complexity * 0.3 +
                mental_complexity * 0.25 +
                emotion_complexity * 0.2 +
                temporal_complexity * 0.15 +
                uncertainty_factor * 0.1
            )
            
            complexity_factors.append(tag_complexity)
        
        # Aplikácia scaling faktora pre pokročilé analýzy
        raw_complexity = statistics.mean(complexity_factors)
        scaled_complexity = raw_complexity * self.complexity_scaling_factor
        
        return min(1.0, scaled_complexity)
    
    def calculate_mental_stability_factor(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet faktora mentálnej stability
        ACTION: Analýza konzistencie mentálnych stavov
        OUTPUT: Faktor stability (0.0-1.0)
        HOOK: mental_stability_calculated
        """
        if not cognitive_tags:
            return 0.5  # Neutrálna stabilita
        
        # Sledovanie prechodov medzi mentálnymi stavmi
        mental_states = [tag.mental_state for tag in cognitive_tags]
        
        if len(set(mental_states)) == 1:
            # Úplná konzistencia - vysoká stabilita
            base_stability = 0.9
        else:
            # Výpočet stability na základe prechodov
            transitions = self._count_mental_state_transitions(mental_states)
            max_possible_transitions = len(mental_states) - 1
            
            if max_possible_transitions > 0:
                transition_ratio = transitions / max_possible_transitions
                base_stability = 1.0 - (transition_ratio * 0.6)
            else:
                base_stability = 0.9
        
        # Úprava na základe kognitívnej záťaže
        avg_load = statistics.mean([tag.cognitive_load for tag in cognitive_tags])
        load_factor = 1.0 - min(avg_load / 15.0, 0.3)  # Vysoká záťaž znižuje stabilitu
        
        # Úprava na základe istoty
        avg_certainty = statistics.mean([tag.certainty_level for tag in cognitive_tags])
        certainty_factor = avg_certainty * 0.2 + 0.8  # Istota zvyšuje stabilitu
        
        final_stability = base_stability * load_factor * certainty_factor
        return max(0.0, min(1.0, final_stability))
    
    def calculate_emotional_resonance_depth(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet hĺbky emočnej rezonancie
        ACTION: Analýza emočnej intenzity a konzistencie
        OUTPUT: Hĺbka emočnej rezonancie (0.0-1.0)
        HOOK: emotional_resonance_calculated
        """
        if not cognitive_tags:
            return 0.0
        
        emotion_scores = []
        
        for tag in cognitive_tags:
            # Základná emočná intenzita
            emotion_intensity = self._get_emotion_intensity(tag.emotion_tone)
            
            # Súlad s mentálnym stavom
            mental_emotion_alignment = self._assess_mental_emotion_coherence(
                tag.mental_state, tag.emotion_tone
            )
            
            # Emočná konzistencia s istotou
            certainty_emotion_alignment = self._assess_certainty_emotion_alignment(
                tag.certainty_level, tag.emotion_tone
            )
            
            tag_resonance = (
                emotion_intensity * 0.4 +
                mental_emotion_alignment * 0.4 +
                certainty_emotion_alignment * 0.2
            )
            
            emotion_scores.append(tag_resonance)
        
        # Výpočet hĺbky s ohľadom na emočnú variabilnosť
        mean_resonance = statistics.mean(emotion_scores)
        
        # Bonifikácia za emočnú hĺbku (nie len intenzitu)
        emotion_variety = len(set(tag.emotion_tone for tag in cognitive_tags))
        variety_bonus = min(emotion_variety * 0.1, 0.2)
        
        return min(1.0, mean_resonance + variety_bonus)
    
    def calculate_temporal_awareness_level(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet úrovne temporálneho vedomia
        ACTION: Analýza časového kontextu a sekvencií
        OUTPUT: Úroveň temporálneho vedomia (0.0-1.0)
        HOOK: temporal_awareness_calculated
        """
        if not cognitive_tags:
            return 0.0
        
        temporal_scores = []
        
        for i, tag in enumerate(cognitive_tags):
            # Základná temporálna orientácia
            temporal_orientation = self._get_temporal_orientation_score(tag.temporal_context)
            
            # Temporálna kontinuita (ak máme predchádzajúce tagy)
            if i > 0:
                continuity = self._assess_temporal_continuity(
                    cognitive_tags[i-1], tag
                )
            else:
                continuity = 0.8  # Prvý tag má dobrú kontinuitu
            
            # Temporálna koherencia s kognitívnou záťažou
            load_temporal_coherence = self._assess_load_temporal_coherence(
                tag.cognitive_load, tag.temporal_context
            )
            
            tag_temporal_score = (
                temporal_orientation * 0.4 +
                continuity * 0.3 +
                load_temporal_coherence * 0.3
            )
            
            # Aplikácia váhového rozkladu pre starší kontext
            weight = self.temporal_weight_decay ** i
            temporal_scores.append(tag_temporal_score * weight)
        
        return statistics.mean(temporal_scores) if temporal_scores else 0.0
    
    def calculate_introspective_clarity_score(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """
        INTENT: Výpočet skóre introspektívnej jasnosti
        ACTION: Analýza kvality sebapoznania a reflexie
        OUTPUT: Skóre introspektívnej jasnosti (0.0-1.0)
        HOOK: introspective_clarity_calculated
        """
        if not cognitive_tags:
            return 0.0
        
        clarity_scores = []
        
        for tag in cognitive_tags:
            # Jasnosť sebapoznania na základe istoty
            self_awareness_clarity = tag.certainty_level
            
            # Jasnosť mentálnej reflexie
            mental_clarity = self._assess_mental_clarity(tag.mental_state)
            
            # Emočná jasnosť
            emotional_clarity = self._assess_emotional_clarity(tag.emotion_tone)
            
            # Temporálna jasnosť
            temporal_clarity = self._assess_temporal_clarity(tag.temporal_context)
            
            # Kognitívna jasnosť (inverzne úmerná záťaži)
            cognitive_clarity = max(0.0, 1.0 - (tag.cognitive_load / 12.0))
            
            tag_clarity = (
                self_awareness_clarity * 0.25 +
                mental_clarity * 0.25 +
                emotional_clarity * 0.2 +
                temporal_clarity * 0.15 +
                cognitive_clarity * 0.15
            )
            
            clarity_scores.append(tag_clarity)
        
        # Bonus za konzistentnú jasnosť
        clarity_variance = statistics.variance(clarity_scores) if len(clarity_scores) > 1 else 0
        consistency_bonus = max(0.0, 0.1 - clarity_variance)
        
        mean_clarity = statistics.mean(clarity_scores)
        return min(1.0, mean_clarity + consistency_bonus)
    
    
    # =================================================================
    # PRIVATE HELPER METHODS - KOGNITÍVNE HODNOTENIE
    # =================================================================
    
    def _assess_mental_emotion_coherence(self, mental_state: MentalStateEnum, emotion_tone: EmotionToneEnum) -> float:
        """Hodnotenie koherencie medzi mentálnym stavom a emočným tónom"""
        coherence_matrix = {
            MentalStateEnum.CALM: {
                EmotionToneEnum.NEUTRAL: 1.0,
                EmotionToneEnum.POSITIVE: 0.9,
                EmotionToneEnum.EMPATHETIC: 0.9,
                EmotionToneEnum.ANALYTICAL: 0.7,
                EmotionToneEnum.CRITICAL: 0.4,
                EmotionToneEnum.NEGATIVE: 0.2
            },
            MentalStateEnum.FOCUSED: {
                EmotionToneEnum.ANALYTICAL: 1.0,
                EmotionToneEnum.NEUTRAL: 0.9,
                EmotionToneEnum.CRITICAL: 0.8,
                EmotionToneEnum.POSITIVE: 0.7,
                EmotionToneEnum.EMPATHETIC: 0.5,
                EmotionToneEnum.NEGATIVE: 0.3
            },
            MentalStateEnum.CONTEMPLATIVE: {
                EmotionToneEnum.NEUTRAL: 1.0,
                EmotionToneEnum.ANALYTICAL: 0.9,
                EmotionToneEnum.EMPATHETIC: 0.8,
                EmotionToneEnum.CRITICAL: 0.7,
                EmotionToneEnum.POSITIVE: 0.6,
                EmotionToneEnum.NEGATIVE: 0.4
            },
            MentalStateEnum.CONFUSED: {
                EmotionToneEnum.NEGATIVE: 0.8,
                EmotionToneEnum.NEUTRAL: 0.7,
                EmotionToneEnum.CRITICAL: 0.6,
                EmotionToneEnum.ANALYTICAL: 0.5,
                EmotionToneEnum.EMPATHETIC: 0.4,
                EmotionToneEnum.POSITIVE: 0.2
            }
        }
        return coherence_matrix.get(mental_state, {}).get(emotion_tone, 0.5)
    
    def _assess_load_certainty_coherence(self, cognitive_load: int, certainty_level: float) -> float:
        """Hodnotenie koherencie medzi kognitívnou záťažou a úrovňou istoty"""
        # Vysoká záťaž by mala korelovať s nižšou istotou
        expected_certainty = max(0.1, 1.0 - (cognitive_load / 12.0))
        certainty_difference = abs(certainty_level - expected_certainty)
        return max(0.0, 1.0 - certainty_difference)
    
    def _assess_temporal_coherence(self, temporal_context: TemporalContextEnum, cognitive_load: int) -> float:
        """Hodnotenie temporálnej koherencie"""
        temporal_load_coherence = {
            TemporalContextEnum.IMMEDIATE: {
                "low_load": (0, 4, 0.9),
                "medium_load": (4, 8, 0.8),
                "high_load": (8, 12, 0.6)
            },
            TemporalContextEnum.SHORT_TERM: {
                "low_load": (0, 6, 0.8),
                "medium_load": (6, 10, 0.9),
                "high_load": (10, 12, 0.7)
            },
            TemporalContextEnum.LONG_TERM: {
                "low_load": (0, 5, 0.7),
                "medium_load": (5, 9, 0.8),
                "high_load": (9, 12, 0.9)
            }
        }
        
        context_mapping = temporal_load_coherence.get(temporal_context, {})
        for load_category, (min_load, max_load, coherence) in context_mapping.items():
            if min_load <= cognitive_load <= max_load:
                return coherence
        return 0.5
    
    def _assess_introspective_coherence(self, tag: ASLCognitiveTag) -> float:
        """Hodnotenie introspektívnej koherencie tagu"""
        # Komplexná analýza vnútornej konzistencie
        factors = []
        
        # Súlad istoty s komplexnosťou úlohy
        complexity_certainty_coherence = self._assess_complexity_certainty_alignment(tag)
        factors.append(complexity_certainty_coherence)
        
        # Emočná autenticita
        emotional_authenticity = self._assess_emotional_authenticity(tag)
        factors.append(emotional_authenticity)
        
        # Temporálna realistickosť
        temporal_realism = self._assess_temporal_realism(tag)
        factors.append(temporal_realism)
        
        return statistics.mean(factors) if factors else 0.5
    
    def _get_mental_state_complexity(self, mental_state: MentalStateEnum) -> float:
        """Získanie komplexnosti mentálneho stavu"""
        complexity_mapping = {
            MentalStateEnum.CALM: 0.2,
            MentalStateEnum.FOCUSED: 0.6,
            MentalStateEnum.CONTEMPLATIVE: 0.8,
            MentalStateEnum.CONFUSED: 0.9
        }
        return complexity_mapping.get(mental_state, 0.5)
    
    def _get_emotion_complexity(self, emotion_tone: EmotionToneEnum) -> float:
        """Získanie komplexnosti emočného tónu"""
        complexity_mapping = {
            EmotionToneEnum.NEUTRAL: 0.1,
            EmotionToneEnum.POSITIVE: 0.3,
            EmotionToneEnum.NEGATIVE: 0.4,
            EmotionToneEnum.ANALYTICAL: 0.7,
            EmotionToneEnum.CRITICAL: 0.8,
            EmotionToneEnum.EMPATHETIC: 0.9
        }
        return complexity_mapping.get(emotion_tone, 0.5)
    
    def _get_temporal_complexity(self, temporal_context: TemporalContextEnum) -> float:
        """Získanie temporálnej komplexnosti"""
        complexity_mapping = {
            TemporalContextEnum.IMMEDIATE: 0.3,
            TemporalContextEnum.SHORT_TERM: 0.6,
            TemporalContextEnum.LONG_TERM: 0.9
        }
        return complexity_mapping.get(temporal_context, 0.5)
    
    def _count_mental_state_transitions(self, mental_states: List[MentalStateEnum]) -> int:
        """Počítanie prechodov medzi mentálnymi stavmi"""
        transitions = 0
        for i in range(1, len(mental_states)):
            if mental_states[i] != mental_states[i-1]:
                transitions += 1
        return transitions
    
    def _get_emotion_intensity(self, emotion_tone: EmotionToneEnum) -> float:
        """Získanie intenzity emócie"""
        intensity_mapping = {
            EmotionToneEnum.NEUTRAL: 0.1,
            EmotionToneEnum.POSITIVE: 0.7,
            EmotionToneEnum.NEGATIVE: 0.8,
            EmotionToneEnum.ANALYTICAL: 0.5,
            EmotionToneEnum.CRITICAL: 0.9,
            EmotionToneEnum.EMPATHETIC: 0.8
        }
        return intensity_mapping.get(emotion_tone, 0.5)
    
    def _assess_certainty_emotion_alignment(self, certainty_level: float, emotion_tone: EmotionToneEnum) -> float:
        """Hodnotenie súladu istoty s emóciou"""
        # Vysoká istota by mala korelovať s pozitívnymi/neutrálnymi emóciami
        if emotion_tone in [EmotionToneEnum.POSITIVE, EmotionToneEnum.NEUTRAL]:
            return certainty_level
        elif emotion_tone == EmotionToneEnum.NEGATIVE:
            return 1.0 - certainty_level  # Nízka istota súladí s negatívnymi emóciami
        else:
            return 0.7  # Analytické/kritické/empatické emócie sú nezávislé od istoty
    
    def _get_temporal_orientation_score(self, temporal_context: TemporalContextEnum) -> float:
        """Získanie skóre temporálnej orientácie"""
        orientation_mapping = {
            TemporalContextEnum.IMMEDIATE: 0.9,  # Vysoká orientácia v prítomnosti
            TemporalContextEnum.SHORT_TERM: 0.7,  # Dobrá orientácia v blízkej budúcnosti
            TemporalContextEnum.LONG_TERM: 0.6   # Stredná orientácia v dlhodobom kontexte
        }
        return orientation_mapping.get(temporal_context, 0.5)
    
    def _assess_temporal_continuity(self, prev_tag: ASLCognitiveTag, current_tag: ASLCognitiveTag) -> float:
        """Hodnotenie temporálnej kontinuity medzi tagmi"""
        # Logické následnosti v temporálnom kontexte
        continuity_scores = []
        
        # Kontinuita mentálneho stavu
        if prev_tag.mental_state == current_tag.mental_state:
            continuity_scores.append(0.9)
        else:
            # Penalizácia za náhle zmeny
            continuity_scores.append(0.6)
        
        # Kontinuita kognitívnej záťaže
        load_difference = abs(prev_tag.cognitive_load - current_tag.cognitive_load)
        load_continuity = max(0.0, 1.0 - (load_difference / 10.0))
        continuity_scores.append(load_continuity)
        
        # Kontinuita istoty
        certainty_difference = abs(prev_tag.certainty_level - current_tag.certainty_level)
        certainty_continuity = max(0.0, 1.0 - certainty_difference)
        continuity_scores.append(certainty_continuity)
        
        return statistics.mean(continuity_scores) if continuity_scores else 0.5
    
    def _assess_load_temporal_coherence(self, cognitive_load: int, temporal_context: TemporalContextEnum) -> float:
        """Hodnotenie koherencie záťaže s temporálnym kontextom"""
        # Dlhodobé úlohy môžu mať vyššiu záťaž
        if temporal_context == TemporalContextEnum.LONG_TERM:
            return min(1.0, (cognitive_load / 10.0) + 0.3)
        elif temporal_context == TemporalContextEnum.SHORT_TERM:
            return max(0.3, 1.0 - abs(cognitive_load - 6) / 8.0)
        else:  # IMMEDIATE
            return max(0.2, 1.0 - (cognitive_load / 12.0))
    
    def _assess_mental_clarity(self, mental_state: MentalStateEnum) -> float:
        """Hodnotenie jasnosti mentálneho stavu"""
        clarity_mapping = {
            MentalStateEnum.FOCUSED: 0.9,
            MentalStateEnum.CALM: 0.8,
            MentalStateEnum.CONTEMPLATIVE: 0.7,
            MentalStateEnum.CONFUSED: 0.2
        }
        return clarity_mapping.get(mental_state, 0.5)
    
    def _assess_emotional_clarity(self, emotion_tone: EmotionToneEnum) -> float:
        """Hodnotenie emočnej jasnosti"""
        clarity_mapping = {
            EmotionToneEnum.NEUTRAL: 0.9,
            EmotionToneEnum.ANALYTICAL: 0.8,
            EmotionToneEnum.POSITIVE: 0.7,
            EmotionToneEnum.EMPATHETIC: 0.7,
            EmotionToneEnum.CRITICAL: 0.6,
            EmotionToneEnum.NEGATIVE: 0.4
        }
        return clarity_mapping.get(emotion_tone, 0.5)
    
    def _assess_temporal_clarity(self, temporal_context: TemporalContextEnum) -> float:
        """Hodnotenie temporálnej jasnosti"""
        clarity_mapping = {
            TemporalContextEnum.IMMEDIATE: 0.9,
            TemporalContextEnum.SHORT_TERM: 0.7,
            TemporalContextEnum.LONG_TERM: 0.5
        }
        return clarity_mapping.get(temporal_context, 0.5)
    
    # =================================================================
    # POKROČILÉ ANALYTICKÉ METÓDY
    # =================================================================
    
    def _calculate_overall_cognitive_health(self, consciousness_coherence: float, 
                                          complexity_index: float, stability_factor: float,
                                          resonance_depth: float, temporal_awareness: float, 
                                          introspective_clarity: float) -> float:
        """Výpočet celkového kognitívneho zdravia"""
        # Vážené skóre s dôrazom na koherenciu a stabilitu
        weights = {
            'coherence': 0.25,
            'complexity': 0.15,
            'stability': 0.25, 
            'resonance': 0.15,
            'temporal': 0.1,
            'clarity': 0.1
        }
        
        weighted_score = (
            consciousness_coherence * weights['coherence'] +
            complexity_index * weights['complexity'] +
            stability_factor * weights['stability'] +
            resonance_depth * weights['resonance'] +
            temporal_awareness * weights['temporal'] +
            introspective_clarity * weights['clarity']
        )
        
        # Bonus za vyvážené skóre (žiadny extrém)
        scores = [consciousness_coherence, complexity_index, stability_factor, 
                 resonance_depth, temporal_awareness, introspective_clarity]
        score_variance = statistics.variance(scores) if len(scores) > 1 else 0
        balance_bonus = max(0.0, 0.05 - score_variance * 0.1)
        
        return min(1.0, weighted_score + balance_bonus)
    
    def _update_cognitive_patterns(self, cognitive_tags: List[ASLCognitiveTag], metrics: CognitiveMetrics):
        """Aktualizácia kognitívnych vzorov pre dlhodobú analýzu"""
        pattern = {
            'timestamp': metrics.analysis_timestamp,
            'tag_count': len(cognitive_tags),
            'dominant_mental_state': self._get_dominant_mental_state(cognitive_tags),
            'dominant_emotion': self._get_dominant_emotion(cognitive_tags),
            'avg_cognitive_load': statistics.mean([tag.cognitive_load for tag in cognitive_tags]),
            'avg_certainty': statistics.mean([tag.certainty_level for tag in cognitive_tags]),
            'overall_health': metrics.overall_cognitive_health
        }
        
        self.cognitive_flow_patterns.append(pattern)
        
        # Udržiavanie histórie (max 100 vzorov)
        if len(self.cognitive_flow_patterns) > 100:
            self.cognitive_flow_patterns.pop(0)
    
    def _get_dominant_mental_state(self, cognitive_tags: List[ASLCognitiveTag]) -> str:
        """Získanie dominantného mentálneho stavu"""
        if not cognitive_tags:
            return "unknown"
        
        state_counts = {}
        for tag in cognitive_tags:
            state = tag.mental_state.value
            state_counts[state] = state_counts.get(state, 0) + 1
        
        return max(state_counts, key=state_counts.get)
    
    def _get_dominant_emotion(self, cognitive_tags: List[ASLCognitiveTag]) -> str:
        """Získanie dominantnej emócie"""
        if not cognitive_tags:
            return "unknown"
        
        emotion_counts = {}
        for tag in cognitive_tags:
            emotion = tag.emotion_tone.value
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        return max(emotion_counts, key=emotion_counts.get)
    
    # =================================================================
    # PODPORNÉ METÓDY PRE PRODUKČNÉ PROSTREDIE
    # =================================================================
    
    def _create_empty_metrics(self) -> CognitiveMetrics:
        """Vytvorenie prázdnych metrík pre edge cases"""
        return CognitiveMetrics(
            consciousness_coherence_rate=0.0,
            cognitive_complexity_index=0.0,
            mental_stability_factor=0.5,
            emotional_resonance_depth=0.0,
            temporal_awareness_level=0.0,
            introspective_clarity_score=0.0,
            overall_cognitive_health=0.0,
            analysis_timestamp=datetime.now().isoformat(),
            session_id=self.session_id
        )
    
    def _create_error_metrics(self, error_message: str) -> CognitiveMetrics:
        """Vytvorenie error metrík pri zlyhaní analýzy"""
        return CognitiveMetrics(
            consciousness_coherence_rate=0.0,
            cognitive_complexity_index=0.0,
            mental_stability_factor=0.0,
            emotional_resonance_depth=0.0,
            temporal_awareness_level=0.0,
            introspective_clarity_score=0.0,
            overall_cognitive_health=0.0,
            analysis_timestamp=datetime.now().isoformat(),
            session_id=f"error_{self.session_id}"
        )
    
    def _assess_complexity_certainty_alignment(self, tag: ASLCognitiveTag) -> float:
        """Hodnotenie súladu komplexnosti s istotou"""
        # Vysoká komplexnosť by mala korelovať s nižšou istotou
        complexity_score = (
            self._get_mental_state_complexity(tag.mental_state) * 0.4 +
            self._get_emotion_complexity(tag.emotion_tone) * 0.3 +
            min(tag.cognitive_load / 10.0, 1.0) * 0.3
        )
        
        expected_certainty = max(0.1, 1.0 - complexity_score * 0.7)
        certainty_difference = abs(tag.certainty_level - expected_certainty)
        return max(0.0, 1.0 - certainty_difference)
    
    def _assess_emotional_authenticity(self, tag: ASLCognitiveTag) -> float:
        """Hodnotenie emočnej autenticity"""
        # Autenticita na základe konzistencie emócie s ostatnými faktormi
        mental_emotion_coherence = self._assess_mental_emotion_coherence(
            tag.mental_state, tag.emotion_tone
        )
        
        certainty_emotion_coherence = self._assess_certainty_emotion_alignment(
            tag.certainty_level, tag.emotion_tone
        )
        
        return (mental_emotion_coherence + certainty_emotion_coherence) / 2.0
    
    def _assess_temporal_realism(self, tag: ASLCognitiveTag) -> float:
        """Hodnotenie temporálnej realistickosti"""
        # Realistickosť kombinácií temporálneho kontextu s ostatnými faktormi
        temporal_complexity = self._get_temporal_complexity(tag.temporal_context)
        cognitive_complexity = min(tag.cognitive_load / 10.0, 1.0)
        
        # Dlhodobé úlohy môžu byť komplexnejšie
        complexity_difference = abs(temporal_complexity - cognitive_complexity)
        return max(0.3, 1.0 - complexity_difference)
    
    # =================================================================
    # PUBLIC API PRE POKROČILÉ FUNKCIE
    # =================================================================
    
    def get_cognitive_trends(self) -> Dict[str, Any]:
        """
        INTENT: Získanie trendov kognitívneho zdravia
        ACTION: Analýza historických dát
        OUTPUT: Trendy a insights
        HOOK: cognitive_trends_analyzed
        """
        if len(self.analysis_history) < 2:
            return {"message": "Insufficient data for trend analysis"}
        
        recent_metrics = self.analysis_history[-5:]  # Posledných 5 analýz
        
        trends = {
            "coherence_trend": self._calculate_trend([m.consciousness_coherence_rate for m in recent_metrics]),
            "stability_trend": self._calculate_trend([m.mental_stability_factor for m in recent_metrics]),
            "complexity_trend": self._calculate_trend([m.cognitive_complexity_index for m in recent_metrics]),
            "overall_health_trend": self._calculate_trend([m.overall_cognitive_health for m in recent_metrics]),
            "session_count": len(self.analysis_history),
            "average_health": statistics.mean([m.overall_cognitive_health for m in self.analysis_history])
        }
        
        return trends
    
    def _calculate_trend(self, values: List[float]) -> str:
        """Výpočet trendu hodnôt"""
        if len(values) < 2:
            return "stable"
        
        differences = [values[i] - values[i-1] for i in range(1, len(values))]
        avg_change = statistics.mean(differences)
        
        if avg_change > 0.05:
            return "improving"
        elif avg_change < -0.05:
            return "declining"
        else:
            return "stable"
    
    def export_session_data(self) -> Dict[str, Any]:
        """
        INTENT: Export kompletných dát session
        ACTION: Serializácia všetkých dát analyzátora
        OUTPUT: JSON-serializable dictionary
        HOOK: session_data_exported
        """
        return {
            "session_id": self.session_id,
            "analysis_mode": self.analysis_mode.value,
            "analysis_history": [metrics.to_dict() for metrics in self.analysis_history],
            "cognitive_flow_patterns": self.cognitive_flow_patterns,
            "session_summary": {
                "total_analyses": len(self.analysis_history),
                "session_duration": self._calculate_session_duration(),
                "average_metrics": self._calculate_average_metrics()
            }
        }
    
    def _calculate_session_duration(self) -> str:
        """Výpočet dĺžky session"""
        if not self.analysis_history:
            return "0 minutes"
        
        start_time = datetime.fromisoformat(self.analysis_history[0].analysis_timestamp)
        end_time = datetime.fromisoformat(self.analysis_history[-1].analysis_timestamp)
        duration = end_time - start_time
        
        return f"{duration.total_seconds() / 60:.1f} minutes"
    
    def _calculate_average_metrics(self) -> Dict[str, float]:
        """Výpočet priemerných metrík session"""
        if not self.analysis_history:
            return {}
        
        return {
            "avg_consciousness_coherence": statistics.mean([m.consciousness_coherence_rate for m in self.analysis_history]),
            "avg_cognitive_complexity": statistics.mean([m.cognitive_complexity_index for m in self.analysis_history]),
            "avg_mental_stability": statistics.mean([m.mental_stability_factor for m in self.analysis_history]),
            "avg_emotional_resonance": statistics.mean([m.emotional_resonance_depth for m in self.analysis_history]),
            "avg_temporal_awareness": statistics.mean([m.temporal_awareness_level for m in self.analysis_history]),
            "avg_introspective_clarity": statistics.mean([m.introspective_clarity_score for m in self.analysis_history]),
            "avg_overall_health": statistics.mean([m.overall_cognitive_health for m in self.analysis_history])
        }


# =================================================================
# KOMPATIBILNÁ WRAPPING FUNKCIA PRE SPÄTNÝ CHOD
# =================================================================

class CognitiveMetricsAnalyzer:
    """
    DEPRECATED: Legacy wrapper pre spätný chod
    Použite AetheroCognitiveAnalyzer pre nové implementácie
    """
    
    def __init__(self):
        logger.warning("CognitiveMetricsAnalyzer is deprecated. Use AetheroCognitiveAnalyzer instead.")
        self._analyzer = AetheroCognitiveAnalyzer(CognitiveAnalysisMode.STANDARD)
    
    def calculate_consciousness_coherence_rate(self, cognitive_tags: List[ASLCognitiveTag]) -> float:
        """Legacy metóda - deleguje na nový analyzátor"""
        return self._analyzer.calculate_consciousness_coherence_rate(cognitive_tags)
    
    def analyze_cognitive_tags(self, cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """Legacy metóda - deleguje na nový analyzátor a konvertuje výstup"""
        metrics = self._analyzer.analyze_cognitive_tags(cognitive_tags)
        return metrics.to_dict()


# =================================================================
# FACTORY FUNKCIE PRE JEDNODUCHÉ POUŽITIE
# =================================================================

def create_standard_analyzer() -> AetheroCognitiveAnalyzer:
    """Vytvorenie štandardného analyzátora"""
    return AetheroCognitiveAnalyzer(CognitiveAnalysisMode.STANDARD)

def create_deep_analyzer() -> AetheroCognitiveAnalyzer:
    """Vytvorenie analyzátora pre hlbokú introspekciu"""
    return AetheroCognitiveAnalyzer(CognitiveAnalysisMode.DEEP_INTROSPECTION)

def create_realtime_analyzer() -> AetheroCognitiveAnalyzer:
    """Vytvorenie analyzátora pre real-time analýzu"""
    return AetheroCognitiveAnalyzer(CognitiveAnalysisMode.REAL_TIME)

def analyze_tags_simple(cognitive_tags: List[ASLCognitiveTag]) -> Dict[str, float]:
    """
    Jednoduchá funkcia pre rýchlu analýzu tagov
    
    Args:
        cognitive_tags: Zoznam ASL kognitívnych tagov
        
    Returns:
        Dictionary s kľúčovými metrikami
    """
    analyzer = create_standard_analyzer()
    metrics = analyzer.analyze_cognitive_tags(cognitive_tags)
    
    return {
        "coherence": metrics.consciousness_coherence_rate,
        "complexity": metrics.cognitive_complexity_index,
        "stability": metrics.mental_stability_factor,
        "overall_health": metrics.overall_cognitive_health
    }
