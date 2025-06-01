import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import json

from introspective_parser_module.parser import ASLMetaParser, IntrospectiveLogger
from introspective_parser_module.models import (
    ASLCognitiveTag, ASLTagModel, MentalStateEnum, 
    EmotionToneEnum, TemporalContextEnum, AetheroIntrospectiveEntity
)
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer
from introspective_parser_module.reflection_agent import AetheroReflectionAgent, ReflectionAgent

class TestASLCognitiveTag(unittest.TestCase):
    def test_create_valid_tag(self):
        tag = ASLCognitiveTag(
            thought_stream="Analyzing introspection",
            mental_state=MentalStateEnum.REFLECTIVE,
            emotion_tone=EmotionToneEnum.NEUTRAL,
            temporal_context=TemporalContextEnum.PRESENT,
            cognitive_load=5,
            certainty_level=0.9,
            aeth_mem_link="session_123",
            constitutional_law="transparency_principle"
        )
        self.assertEqual(tag.mental_state, MentalStateEnum.REFLECTIVE)
        self.assertEqual(tag.temporal_context, TemporalContextEnum.PRESENT)

    def test_invalid_tag(self):
        with self.assertRaises(ValueError):
            ASLCognitiveTag(
                thought_stream="Invalid introspection",
                mental_state="INVALID_STATE",
                emotion_tone=EmotionToneEnum.NEUTRAL,
                temporal_context=TemporalContextEnum.PRESENT,
                cognitive_load=5,
                certainty_level=0.9,
                aeth_mem_link="session_123",
                constitutional_law="transparency_principle"
            )

class TestIntrospectiveLogger(unittest.TestCase):
    def setUp(self):
        self.logger = IntrospectiveLogger("TestLogger")

    def test_log_cognitive_state(self):
        with self.assertLogs(self.logger.logger, level="INFO") as log:
            self.logger.log_cognitive_state("TEST_OPERATION", {"key": "value"})
        self.assertIn("COGNITIVE_OP: TEST_OPERATION", log.output[0])

    def test_log_introspective_reflection(self):
        with self.assertLogs(self.logger.logger, level="INFO") as log:
            self.logger.log_introspective_reflection("Test reflection", 0.8)
        self.assertIn("REFLECTION: Test reflection", log.output[0])

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = ASLMetaParser()

    def test_parse_line_with_valid_asl(self):
        line = "# [ASL] mental_state: reflective, emotion_tone: neutral"
        result = self.parser.parse_line(line)
        self.assertIn("mental_state", result)
        self.assertEqual(result["mental_state"], MentalStateEnum.REFLECTIVE.value)

    def test_parse_line_with_invalid_asl(self):
        line = "# [ASL] invalid_key: value"
        result = self.parser.parse_line(line)
        self.assertNotIn("invalid_key", result)

    def test_validate_asl_block(self):
        asl_components = {
            "thought_stream": "Analyzing introspection",
            "mental_state": MentalStateEnum.REFLECTIVE.value,
            "emotion_tone": EmotionToneEnum.NEUTRAL.value,
            "temporal_context": TemporalContextEnum.PRESENT.value,
            "cognitive_load": 5,
            "certainty_level": 0.9,
            "aeth_mem_link": "session_123",
            "constitutional_law": "transparency_principle"
        }
        is_valid, validated_model = self.parser.validate_asl_block(asl_components)
        self.assertTrue(is_valid)
        self.assertIsNotNone(validated_model)

class TestIntrospectiveLogger(unittest.TestCase):
    """Testy pre introspektívny logovací systém"""
    
    def setUp(self):
        self.logger = IntrospectiveLogger("TestModule")
    
    def test_cognitive_state_logging(self):
        """Test logovania kognitívneho stavu"""
        test_context = {"operation": "test", "certainty": 0.8}
        
        # Should not raise exception
        self.logger.log_cognitive_state("TEST_OPERATION", test_context)
        
        # Verify logger instance exists
        self.assertIsNotNone(self.logger.logger)
        self.assertEqual(self.logger.module_name, "TestModule")
    
    def test_introspective_reflection_logging(self):
        """Test logovania introspektívnych reflexií"""
        self.logger.log_introspective_reflection("Test reflection", 0.9)
        
        # Should complete without error
        self.assertTrue(True)

class TestASLCognitiveTagModel(unittest.TestCase):
    """Komplexné testy pre ASL kognitívny tag model"""
    
    def setUp(self):
        self.valid_tag_data = {
            "thought_stream": "Analyzing current system capabilities",
            "mental_state": MentalStateEnum.FOCUSED,
            "emotion_tone": EmotionToneEnum.ANALYTICAL,
            "cognitive_load": 7,
            "temporal_context": TemporalContextEnum.PRESENT,
            "certainty_level": 0.85,
            "aeth_mem_link": "test_memory_link_001",
            "constitutional_law": "transparency_principle"
        }
    
    def test_valid_cognitive_tag_creation(self):
        """Test vytvárania validného kognitívneho tagu"""
        tag = ASLCognitiveTag(**self.valid_tag_data)
        
        self.assertEqual(tag.thought_stream, "Analyzing current system capabilities")
        self.assertEqual(tag.mental_state, MentalStateEnum.FOCUSED)
        self.assertEqual(tag.emotion_tone, EmotionToneEnum.ANALYTICAL)
        self.assertEqual(tag.cognitive_load, 7)
        self.assertEqual(tag.certainty_level, 0.85)
    
    def test_cognitive_coherence_validation(self):
        """Test validácie kognitívnej koherencie"""
        # Test nekompatibilného stavu - pokojný stav s vysokou záťažou
        invalid_data = self.valid_tag_data.copy()
        invalid_data["mental_state"] = MentalStateEnum.CALM
        invalid_data["cognitive_load"] = 9
        
        with self.assertRaises(ValueError):
            ASLCognitiveTag(**invalid_data)
    
    def test_certainty_coherence_validation(self):
        """Test validácie súladu istoty s mentálnym stavom"""
        # Test nekonzistentnosti - neistý stav s vysokou istotou
        invalid_data = self.valid_tag_data.copy()
        invalid_data["mental_state"] = MentalStateEnum.UNCERTAIN
        invalid_data["certainty_level"] = 0.9
        
        with self.assertRaises(ValueError):
            ASLCognitiveTag(**invalid_data)
    
    def test_consciousness_enhancement(self):
        """Test zvyšovania úrovne vedomia"""
        tag = ASLCognitiveTag(**self.valid_tag_data)
        initial_consciousness = tag.consciousness_level
        initial_depth = tag.introspective_depth
        
        tag.enhance_consciousness(0.2)
        
        self.assertGreater(tag.consciousness_level, initial_consciousness)
        self.assertGreater(tag.introspective_depth, initial_depth)
    
    def test_memory_resonance(self):
        """Test rezonancie s pamäťovými štruktúrami"""
        tag = ASLCognitiveTag(**self.valid_tag_data)
        memory_data = {"context": "test", "relevance": 0.8}
        
        tag.resonate_with_memory(memory_data)
        
        self.assertIn("context", tag.consciousness_resonance)
        self.assertEqual(tag.consciousness_resonance["relevance"], 0.8)
    
    def test_alias_compatibility(self):
        """Test spätnej kompatibility cez ASLTagModel alias"""
        tag = ASLTagModel(**self.valid_tag_data)
        self.assertIsInstance(tag, ASLCognitiveTag)

class TestASLMetaParser(unittest.TestCase):
    """Komplexné testy pre ASL Meta Parser"""
    
    def setUp(self):
        self.parser = ASLMetaParser()
    
    def test_parse_line_valid_asl(self):
        """Test parsovania validného ASL riadku"""
        line = "# [ASL] thought_stream: Deep analytical processing"
        result = self.parser.parse_line(line)
        
        self.assertIn("thought_stream", result)
        self.assertEqual(result["thought_stream"], "Deep analytical processing")
    
    def test_parse_line_invalid_format(self):
        """Test parsovania nevalidného formátu"""
        line = "Invalid line without ASL format"
        result = self.parser.parse_line(line)
        
        self.assertEqual(result, {})
    
    def test_cognitive_value_processing(self):
        """Test spracovania kognitívnych hodnôt"""
        # Test cognitive_load processing
        load_value = self.parser._process_cognitive_value("cognitive_load", "7")
        self.assertEqual(load_value, 7)
        self.assertIsInstance(load_value, int)
        
        # Test certainty_level processing
        certainty_value = self.parser._process_cognitive_value("certainty_level", "0.85")
        self.assertEqual(certainty_value, 0.85)
        self.assertIsInstance(certainty_value, float)
        
        # Test mental_state enum processing
        state_value = self.parser._process_cognitive_value("mental_state", "focused")
        self.assertEqual(state_value, MentalStateEnum.FOCUSED.value)
    
    def test_enum_validation_with_fallback(self):
        """Test validácie enum hodnôt s fallback"""
        # Test neznámeho mental_state
        unknown_state = self.parser._process_cognitive_value("mental_state", "unknown_state")
        self.assertEqual(unknown_state, MentalStateEnum.REFLECTIVE.value)
        
        # Test neznámeho emotion_tone
        unknown_emotion = self.parser._process_cognitive_value("emotion_tone", "unknown_emotion")
        self.assertEqual(unknown_emotion, EmotionToneEnum.NEUTRAL.value)
    
    def test_legacy_field_mapping(self):
        """Test mapovania legacy polí"""
        legacy_components = {
            "statement": "Test statement",
            "law": "test_law",
            "mental_state": "focused"
        }
        
        mapped_components = self.parser._map_legacy_fields(legacy_components)
        
        self.assertIn("thought_stream", mapped_components)
        self.assertIn("constitutional_law", mapped_components)
        self.assertEqual(mapped_components["thought_stream"], "Test statement")
        self.assertEqual(mapped_components["constitutional_law"], "test_law")
    
    def test_complete_parsing_and_validation(self):
        """Test komplexného parsovania a validácie dokumentu"""
        document = """
        # [ASL] thought_stream: Analyzing system state mental_state: focused emotion_tone: analytical
        # [ASL] cognitive_load: 6 temporal_context: present certainty_level: 0.8
        # [ASL] aeth_mem_link: test_link constitutional_law: transparency_principle
        """
        
        result = self.parser.parse_and_validate(document)
        
        self.assertIn("validated_blocks", result)
        self.assertIn("parsing_results", result)
        self.assertIn("introspective_reflection", result)
        self.assertGreater(len(result["parsing_results"]), 0)
    
    def test_parse_valid_input(self):
        valid_input = """
        # [ASL] thought_stream: Analyzing introspection mental_state: reflective
        # [ASL] emotion_tone: neutral cognitive_load: 5 temporal_context: present
        """
        result = self.parser.parse_and_validate(valid_input)
        self.assertIn("validated_blocks", result)
        self.assertGreater(len(result["validated_blocks"]), 0)

    def test_parse_invalid_input(self):
        invalid_input = "# [InvalidTag]"
        result = self.parser.parse_and_validate(invalid_input)
        self.assertEqual(len(result["validated_blocks"]), 0)

class TestCognitiveMetricsAnalyzer(unittest.TestCase):
    """Testy pre analyzátor kognitívnych metrík"""
    
    def setUp(self):
        self.analyzer = CognitiveMetricsAnalyzer()
        self.sample_tags = [
            ASLCognitiveTag(
                thought_stream="First analysis",
                mental_state=MentalStateEnum.FOCUSED,
                emotion_tone=EmotionToneEnum.ANALYTICAL,
                cognitive_load=7,
                temporal_context=TemporalContextEnum.PRESENT,
                certainty_level=0.85,
                aeth_mem_link="link1",
                constitutional_law="law1"
            ),
            ASLCognitiveTag(
                thought_stream="Second analysis",
                mental_state=MentalStateEnum.CONTEMPLATIVE,
                emotion_tone=EmotionToneEnum.NEUTRAL,
                cognitive_load=5,
                temporal_context=TemporalContextEnum.PRESENT,
                certainty_level=0.7,
                aeth_mem_link="link2",
                constitutional_law="law2"
            )
        ]
    
    def test_consciousness_coherence_calculation(self):
        """Test výpočtu koherencie vedomia"""
        coherence_rate = self.analyzer.calculate_consciousness_coherence_rate(self.sample_tags)
        
        self.assertIsInstance(coherence_rate, float)
        self.assertGreaterEqual(coherence_rate, 0.0)
        self.assertLessEqual(coherence_rate, 1.0)
    
    def test_mental_emotion_coherence_assessment(self):
        """Test hodnotenia koherencie mental_state a emotion_tone"""
        coherence = self.analyzer._assess_mental_emotion_coherence(
            MentalStateEnum.FOCUSED, EmotionToneEnum.ANALYTICAL
        )
        
        self.assertEqual(coherence, 1.0)  # Perfect match
        
        # Test weak coherence
        weak_coherence = self.analyzer._assess_mental_emotion_coherence(
            MentalStateEnum.CALM, EmotionToneEnum.CRITICAL
        )
        self.assertLess(weak_coherence, 0.8)
    
    def test_cognitive_evolution_analysis(self):
        """Test analýzy kognitívnej evolúcie"""
        evolution = self.analyzer.analyze_cognitive_evolution(self.sample_tags)
        
        self.assertIn("cognitive_load_trend", evolution)
        self.assertIn("certainty_trend", evolution)
        self.assertIn("mental_state_stability", evolution)
        self.assertIn("overall_cognitive_evolution", evolution)
    
    def test_introspective_report_generation(self):
        """Test generovania introspektívneho reportu"""
        report = self.analyzer.generate_introspective_report(self.sample_tags)
        
        self.assertIn("consciousness_coherence_rate", report)
        self.assertIn("cognitive_evolution_analysis", report)
        self.assertIn("introspective_insights", report)
        self.assertIn("aethero_constitutional_compliance", report)
        
        # Verify insights are generated
        self.assertIsInstance(report["introspective_insights"], list)
    
    def test_constitutional_compliance_assessment(self):
        """Test hodnotenia ústavného súladu"""
        compliance = self.analyzer._assess_constitutional_compliance(self.sample_tags)
        
        self.assertIn("overall_compliance_score", compliance)
        self.assertIn("compliance_factors", compliance)
        self.assertIn("constitutional_status", compliance)
        
        self.assertIsInstance(compliance["overall_compliance_score"], float)
    
    def test_analyze_metrics(self):
        metrics = {"focus": 0.8, "clarity": 0.9}
        result = self.analyzer.analyze(metrics)
        self.assertIn("focus", result)

class TestAetheroReflectionAgent(unittest.TestCase):
    """Testy pre pokročilý reflexívny agent"""
    
    def setUp(self):
        self.agent = AetheroReflectionAgent()
    
    def test_agent_initialization(self):
        """Test inicializácie agenta"""
        self.assertIsNotNone(self.agent.parser)
        self.assertIsNotNone(self.agent.metrics_analyzer)
        self.assertIsNotNone(self.agent.agent_id)
        self.assertEqual(self.agent.reflection_session_count, 0)
    
    def test_reflection_on_simple_document(self):
        """Test reflexie na jednoduchom dokumente"""
        document = """
        # [ASL] thought_stream: Testing reflection capabilities
        # [ASL] mental_state: focused emotion_tone: analytical cognitive_load: 6
        # [ASL] temporal_context: present certainty_level: 0.8
        # [ASL] aeth_mem_link: test_reflection constitutional_law: transparency_principle
        """
        
        reflection = self.agent.reflect_on_input(document)
        
        self.assertIn("reflection_agent_id", reflection)
        self.assertIn("deep_cognitive_reflections", reflection)
        self.assertIn("actionable_insights", reflection)
        self.assertIn("consciousness_evolution_assessment", reflection)
        self.assertEqual(self.agent.reflection_session_count, 1)
    
    def test_multiple_reflection_sessions(self):
        """Test viacerých reflexívnych sessions"""
        document = "# [ASL] thought_stream: Multi-session test mental_state: focused"
        
        # First session
        self.agent.reflect_on_input(document)
        # Second session
        self.agent.reflect_on_input(document)
        
        self.assertEqual(self.agent.reflection_session_count, 2)
        self.assertEqual(len(self.agent.reflection_memory), 2)
    
    def test_consciousness_evolution_tracking(self):
        """Test sledovania evolúcie vedomia"""
        # Create documents with different consciousness levels
        doc1 = """# [ASL] thought_stream: Low consciousness test mental_state: confused cognitive_load: 3"""
        doc2 = """# [ASL] thought_stream: High consciousness test mental_state: focused cognitive_load: 8"""
        
        self.agent.reflect_on_input(doc1)
        self.agent.reflect_on_input(doc2)
        
        self.assertGreater(len(self.agent.consciousness_evolution_track), 0)
    
    def test_actionable_insights_generation(self):
        """Test generovania actionable insights"""
        # Create document that should trigger insights
        poor_coherence_doc = """
        # [ASL] thought_stream: Incoherent test mental_state: calm cognitive_load: 9
        # [ASL] emotion_tone: critical certainty_level: 0.2
        """
        
        reflection = self.agent.reflect_on_input(poor_coherence_doc)
        insights = reflection.get("actionable_insights", [])
        
        self.assertIsInstance(insights, list)
        self.assertGreater(len(insights), 0)
    
    def test_agent_performance_tracking(self):
        """Test sledovania výkonnosti agenta"""
        document = "# [ASL] thought_stream: Performance test"
        
        self.agent.reflect_on_input(document)
        performance = self.agent._generate_agent_performance_summary()
        
        self.assertIn("total_reflection_sessions", performance)
        self.assertIn("average_reflection_depth", performance)
        self.assertIn("introspective_capability_level", performance)
    
    def test_reflect(self):
        tags = [ASLCognitiveTag(temporal_context=TemporalContextEnum.PRESENT)]
        result = self.agent.reflect(tags)
        self.assertIn("temporal_consciousness_insights", result)

class TestLegacyCompatibility(unittest.TestCase):
    """Testy pre spätná kompatibilitu"""
    
    def test_legacy_reflection_agent(self):
        """Test legacy ReflectionAgent wrappera"""
        agent = ReflectionAgent()
        document = "# [ASL] thought_stream: Legacy test mental_state: focused"
        
        result = agent.reflect_on_input(document)
        
        # Should have legacy structure
        self.assertIn("parsed_data", result)
        self.assertIn("introspection", result)
    
    def test_asl_tag_model_aliasu(self):
        """Test ASLTagModel aliasu"""
        tag_data = {
            "thought_stream": "Alias test",
            "mental_state": MentalStateEnum.FOCUSED,
            "emotion_tone": EmotionToneEnum.NEUTRAL,
            "cognitive_load": 5,
            "temporal_context": TemporalContextEnum.PRESENT,
            "certainty_level": 0.7,
            "aeth_mem_link": "test",
            "constitutional_law": "test"
        }
        
        tag = ASLTagModel(**tag_data)
        self.assertIsInstance(tag, ASLCognitiveTag)

class TestIntegrationScenarios(unittest.TestCase):
    """Integračné testy pre komplexné scenáre"""
    
    def setUp(self):
        self.parser = ASLMetaParser()
        self.analyzer = CognitiveMetricsAnalyzer()
        self.agent = AetheroReflectionAgent()
    
    def test_complete_introspective_workflow(self):
        """Test kompletného introspektívneho workflow"""
        complex_document = """
        # [ASL] thought_stream: Beginning complex analysis mental_state: focused
        # [ASL] emotion_tone: analytical cognitive_load: 8 certainty_level: 0.9
        # [ASL] temporal_context: present aeth_mem_link: complex_analysis_001
        # [ASL] constitutional_law: comprehensive_analysis_principle
        
        # [ASL] thought_stream: Deepening understanding mental_state: contemplative
        # [ASL] emotion_tone: neutral cognitive_load: 6 certainty_level: 0.7
        # [ASL] temporal_context: present aeth_mem_link: complex_analysis_002
        # [ASL] constitutional_law: depth_principle
        
        # [ASL] thought_stream: Reaching conclusions mental_state: decisive
        # [ASL] emotion_tone: positive cognitive_load: 7 certainty_level: 0.95
        # [ASL] temporal_context: present aeth_mem_link: complex_analysis_003
        # [ASL] constitutional_law: conclusion_principle
        """
        
        # Full workflow test
        reflection = self.agent.reflect_on_input(complex_document)
        
        # Verify all components worked
        self.assertGreater(len(reflection["validated_cognitive_tags"]), 0)
        self.assertIn("introspective_metrics_report", reflection)
        self.assertIn("deep_cognitive_reflections", reflection)
        self.assertIn("consciousness_evolution_assessment", reflection)
        
        # Verify cognitive evolution was detected
        evolution = reflection["consciousness_evolution_assessment"]
        self.assertIn("consciousness_trend", evolution)
        self.assertIn("introspective_depth_trend", evolution)
    
    def test_error_handling_and_recovery(self):
        """Test spracovania chýb a recovery"""
        malformed_document = """
        # [ASL] invalid_format_here
        # [ASL] mental_state: invalid_state cognitive_load: not_a_number
        # Normal text without ASL tags
        # [ASL] thought_stream: Valid tag after errors mental_state: focused
        """
        
        # Should not crash and should process valid parts
        reflection = self.agent.reflect_on_input(malformed_document)
        
        self.assertIn("parsing_analysis", reflection)
        self.assertIn("failed_validations", reflection["parsing_analysis"])
        # Should still have some successful processing
        self.assertIsInstance(reflection, dict)

if __name__ == "__main__":
    # Spustenie všetkých testov s detailným outputom
    unittest.main(verbosity=2)
