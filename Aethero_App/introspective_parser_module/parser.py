from typing import Dict, Any, List, Tuple, Optional, Union
import re
import logging
import os
import json
from datetime import datetime
from .models import ASLTagModel, ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, TemporalContextEnum

# Graceful pydantic import with fallback
try:
    from pydantic import ValidationError
    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False
    # Define a basic ValidationError fallback
    class ValidationError(Exception):
        pass

# Configure introspective logging for cognitive transparency
class IntrospectiveLogger:
    """Introspective logging system for cognitive flow tracking"""
    
    def __init__(self, module_name: str = "ASLMetaParser"):
        self.module_name = module_name
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.INFO)
        
        # Create introspective formatter
        formatter = logging.Formatter(
            "%(asctime)s - COGNITIVE_FLOW [%(name)s] - %(levelname)s - %(message)s"
        )
        
        # File handler for persistent introspection
        file_handler = logging.FileHandler("aethero_cognitive_flow.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def log_cognitive_state(self, operation: str, mental_context: Dict[str, Any]):
        """Log cognitive state during operations"""
        self.logger.info(f"COGNITIVE_OP: {operation} | CONTEXT: {json.dumps(mental_context)}")
    
    def log_introspective_reflection(self, reflection: str, certainty: float):
        """Log introspective reflections with certainty levels"""
        self.logger.info(f"REFLECTION: {reflection} | CERTAINTY: {certainty}")


class ASLMetaParser:
    """
    Introspective Meta-Parser for Aethero Syntax Language (ASL)
    
    This parser embodies the cognitive architecture of Aethero's consciousness,
    processing ASL tags as introspective thoughts and validating them through
    transparent cognitive flows.
    """
    
    def __init__(self):
        self.introspective_logger = IntrospectiveLogger("ASLMetaParser")
        self.cognitive_patterns = {
            'asl_comment': re.compile(r'#\s*\[ASL\]\s*(.+)', re.IGNORECASE),
            'key_value': re.compile(r'(\w+):\s*(.+?)(?=\s*\w+:|$)'),
            'mental_state_keywords': [state.value for state in MentalStateEnum],
            'emotion_tone_keywords': [tone.value for tone in EmotionToneEnum],
            'temporal_context_keywords': [context.value for context in TemporalContextEnum]
        }
        self.parsing_session_id = datetime.now().isoformat()
        
        # Introspective state tracking
        self.current_cognitive_load = 0
        self.parsing_certainty = 1.0
        self.validated_blocks = []
        self.failed_validations = []
    
    def _reflect_on_parsing_state(self) -> Dict[str, Any]:
        """Internal introspective reflection on current parsing state"""
        reflection = {
            "cognitive_load": self.current_cognitive_load,
            "parsing_certainty": self.parsing_certainty,
            "session_id": self.parsing_session_id,
            "validated_count": len(self.validated_blocks),
            "failed_count": len(self.failed_validations)
        }
        
        self.introspective_logger.log_cognitive_state(
            "INTROSPECTIVE_REFLECTION", reflection
        )
        return reflection
    
    def parse_line(self, line: str) -> Dict[str, Any]:
        """
        Parse a single line for ASL tags with introspective awareness
        
        Args:
            line: Single line of text potentially containing ASL tags
            
        Returns:
            Dictionary of parsed ASL components or empty dict if no valid ASL found
        """
        self.current_cognitive_load += 1
        
        # Cognitive pattern matching for ASL comments
        asl_match = self.cognitive_patterns['asl_comment'].match(line.strip())
        if not asl_match:
            self.introspective_logger.log_cognitive_state(
                "NO_ASL_PATTERN_DETECTED", {"line": line[:50]}
            )
            return {}
        
        # Extract and process ASL content
        asl_content = asl_match.group(1).strip()
        parsed_components = {}
        
        # Introspective key-value extraction
        kv_matches = self.cognitive_patterns['key_value'].findall(asl_content)
        
        for key, value in kv_matches:
            # Cognitive value processing
            processed_value = self._process_cognitive_value(key, value.strip())
            parsed_components[key] = processed_value
            
            self.introspective_logger.log_cognitive_state(
                "ASL_COMPONENT_EXTRACTED", 
                {"key": key, "value": processed_value, "certainty": self.parsing_certainty}
            )
        
        return parsed_components
    
    def _process_cognitive_value(self, key: str, raw_value: str) -> Union[str, int, float]:
        """
        Process values with cognitive awareness based on key context
        
        Args:
            key: The ASL tag key
            raw_value: Raw string value to process
            
        Returns:
            Appropriately typed and processed value
        """
        # Remove quotes if present
        value = raw_value.strip('\'"')
        
        # Cognitive type inference based on key semantics
        if key == 'cognitive_load':
            try:
                return int(value)
            except ValueError:
                self.parsing_certainty *= 0.9  # Reduce certainty on type mismatch
                return 1  # Default minimum cognitive load
        
        elif key == 'certainty_level':
            try:
                cert_value = float(value)
                return max(0.0, min(1.0, cert_value))  # Clamp to [0,1]
            except ValueError:
                self.parsing_certainty *= 0.8
                return 0.5
        
        elif key in ['mental_state', 'emotion_tone', 'temporal_context']:
            # Map old field names to new ones if needed
            if key == 'mental_state':
                # Validate against MentalStateEnum
                try:
                    return MentalStateEnum(value).value
                except ValueError:
                    self.introspective_logger.log_introspective_reflection(
                        f"Unknown mental_state: {value}, using REFLECTIVE as default", 0.7
                    )
                    return MentalStateEnum.REFLECTIVE.value
            
            elif key == 'emotion_tone':
                # Validate against EmotionToneEnum
                try:
                    return EmotionToneEnum(value).value
                except ValueError:
                    self.introspective_logger.log_introspective_reflection(
                        f"Unknown emotion_tone: {value}, using NEUTRAL as default", 0.7
                    )
                    return EmotionToneEnum.NEUTRAL.value
            
            elif key == 'temporal_context':
                # Validate against TemporalContextEnum
                try:
                    return TemporalContextEnum(value).value
                except ValueError:
                    self.introspective_logger.log_introspective_reflection(
                        f"Unknown temporal_context: {value}, using PRESENT as default", 0.7
                    )
                    return TemporalContextEnum.PRESENT.value
        
        # Handle field name mapping for compatibility
        elif key == 'statement':
            # Map to new field name
            return value
        
        elif key == 'law':
            # Map to new field name 'constitutional_law'
            return value
        
        return value
    
    def validate_asl_block(self, asl_components: Dict[str, Any]) -> Tuple[bool, Optional[Any]]:
        """
        Validate ASL components against Pydantic model with introspective checks
        
        Args:
            asl_components: Dictionary of parsed ASL components
            
        Returns:
            Tuple of (is_valid, validated_model_or_none)
        """
        try:
            # Map old field names to new ones for compatibility
            mapped_components = self._map_legacy_fields(asl_components)
            
            if PYDANTIC_AVAILABLE:
                # Attempt Pydantic validation with the new ASLCognitiveTag model
                validated_model = ASLCognitiveTag(**mapped_components)
                
                # Introspective validation success
                self.introspective_logger.log_cognitive_state(
                    "PYDANTIC_VALIDATION_SUCCESS",
                    {"components": mapped_components, "certainty": self.parsing_certainty}
                )
                
                self.validated_blocks.append(validated_model.dict())
                return True, validated_model
            else:
                # Fallback validation without Pydantic
                if self._basic_validate_components(mapped_components):
                    self.introspective_logger.log_cognitive_state(
                        "BASIC_VALIDATION_SUCCESS",
                        {"components": mapped_components, "certainty": self.parsing_certainty}
                    )
                    
                    self.validated_blocks.append(mapped_components)
                    return True, mapped_components
                else:
                    raise ValidationError("Basic validation failed")
            
        except ValidationError as e:
            # Introspective error analysis
            self.introspective_logger.log_cognitive_state(
                "VALIDATION_FAILURE",
                {
                    "components": asl_components,
                    "errors": str(e),
                    "certainty": self.parsing_certainty,
                    "pydantic_available": PYDANTIC_AVAILABLE
                }
            )
            
            self.failed_validations.append({
                "components": asl_components,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
            
            return False, None
    
    def _map_legacy_fields(self, components: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map legacy field names to new ASLCognitiveTag field names
        
        Args:
            components: Original parsed components
            
        Returns:
            Mapped components compatible with ASLCognitiveTag
        """
        mapped = components.copy()
        
        # Field name mappings
        field_mappings = {
            'statement': 'thought_stream',
            'law': 'constitutional_law'
        }
        
        for old_field, new_field in field_mappings.items():
            if old_field in mapped:
                mapped[new_field] = mapped.pop(old_field)
        
        # Ensure required fields have defaults if missing
        defaults = {
            'thought_stream': 'Introspective parsing process',
            'mental_state': MentalStateEnum.REFLECTIVE.value,
            'emotion_tone': EmotionToneEnum.NEUTRAL.value,
            'cognitive_load': 5,
            'temporal_context': TemporalContextEnum.PRESENT.value,
            'certainty_level': 0.5,
            'aeth_mem_link': 'introspective_parsing_session',
            'constitutional_law': 'transparency_principle'
        }
        
        for field, default_value in defaults.items():
            if field not in mapped:
                mapped[field] = default_value
                self.introspective_logger.log_cognitive_state(
                    "DEFAULT_VALUE_APPLIED",
                    {"field": field, "default": default_value}
                )
        
        return mapped
    
    def _basic_validate_components(self, components: Dict[str, Any]) -> bool:
        """
        Basic validation without Pydantic (fallback mechanism)
        
        Args:
            components: Components to validate
            
        Returns:
            True if components pass basic validation
        """
        required_fields = ['thought_stream', 'mental_state', 'emotion_tone']
        
        # Check required fields
        for field in required_fields:
            if field not in components or not components[field]:
                return False
        
        # Validate enum values
        if components.get('mental_state') not in [state.value for state in MentalStateEnum]:
            return False
            
        if components.get('emotion_tone') not in [tone.value for tone in EmotionToneEnum]:
            return False
            
        if components.get('temporal_context') not in [context.value for context in TemporalContextEnum]:
            return False
        
        # Validate numeric ranges
        cognitive_load = components.get('cognitive_load', 5)
        if not isinstance(cognitive_load, int) or cognitive_load < 1 or cognitive_load > 10:
            return False
            
        certainty_level = components.get('certainty_level', 0.5)
        if not isinstance(certainty_level, (int, float)) or certainty_level < 0.0 or certainty_level > 1.0:
            return False
        
        return True
    
    def parse_and_validate(self, document: str) -> Dict[str, Any]:
        """
        Parse entire document and validate all ASL blocks with introspective reporting
        
        Args:
            document: Multi-line document potentially containing ASL tags
            
        Returns:
            Comprehensive parsing and validation report
        """
        self.introspective_logger.log_cognitive_state(
            "DOCUMENT_PARSING_INITIATED",
            {"document_length": len(document), "session_id": self.parsing_session_id}
        )
        
        lines = document.split('\n')
        parsing_results = []
        
        for line_num, line in enumerate(lines, 1):
            asl_components = self.parse_line(line)
            
            if asl_components:
                is_valid, validated_model = self.validate_asl_block(asl_components)
                
                parsing_results.append({
                    "line_number": line_num,
                    "line_content": line,
                    "parsed_components": asl_components,
                    "is_valid": is_valid,
                    "validated_model": validated_model.dict() if (validated_model and hasattr(validated_model, 'dict')) else validated_model
                })
        
        # Final introspective reflection
        final_reflection = self._reflect_on_parsing_state()
        
        return {
            "session_id": self.parsing_session_id,
            "total_lines_processed": len(lines),
            "asl_blocks_found": len(parsing_results),
            "validated_blocks": self.validated_blocks,
            "failed_validations": self.failed_validations,
            "parsing_results": parsing_results,
            "introspective_reflection": final_reflection,
            "cognitive_transparency_report": self._generate_transparency_report()
        }
    
    def _generate_transparency_report(self) -> Dict[str, Any]:
        """Generate transparency report for cognitive accountability"""
        return {
            "parsing_methodology": "Introspective ASL Meta-Parsing with Cognitive Flow Tracking",
            "validation_system": "Pydantic + Fallback" if PYDANTIC_AVAILABLE else "Basic Fallback Only",
            "certainty_degradation_factors": [
                "Type mismatches in cognitive_load and certainty_level",
                "Unknown mental_state or emotion_tone keywords", 
                "Validation failures",
                "Missing Pydantic dependency" if not PYDANTIC_AVAILABLE else None
            ],
            "cognitive_patterns_used": list(self.cognitive_patterns.keys()),
            "introspective_logging_active": True,
            "dependency_status": {
                "pydantic_available": PYDANTIC_AVAILABLE,
                "fallback_validation": True
            },
            "aethero_constitutional_alignment": "Full transparency and introspective accountability"
        }
