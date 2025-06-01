"""
Introspective Parser Module for Aethero Consciousness System

This module provides advanced introspective parsing capabilities for ASL (Aethero Syntax Language)
with cognitive coherence analysis, consciousness tracking, and constitutional compliance validation.

Core Components:
- ASLMetaParser: Advanced introspective parser with cognitive flow tracking
- ASLCognitiveTag: Sophisticated cognitive tag model with built-in validation
- CognitiveMetricsAnalyzer: Deep cognitive analysis and coherence metrics
- AetheroReflectionAgent: Full introspective reflection and analysis agent

Legacy Components (for backward compatibility):
- ASLTagModel: Alias for ASLCognitiveTag
- ReflectionAgent: Simplified wrapper for AetheroReflectionAgent
"""

from .parser import ASLMetaParser, IntrospectiveLogger
from .models import (
    ASLCognitiveTag, 
    ASLTagModel,  # Alias for backward compatibility
    AetheroIntrospectiveEntity,
    MentalStateEnum,
    EmotionToneEnum, 
    TemporalContextEnum
)
from .metrics import (
    CognitiveMetricsAnalyzer,
    # Legacy functions for backward compatibility
    calculate_success_rate,
    analyze_cognitive_load,
    generate_introspection_report
)
from .reflection_agent import AetheroReflectionAgent, ReflectionAgent

# Version and module metadata
__version__ = "2.0.0-introspective"
__author__ = "Aethero Introspective Systems Ministry"
__description__ = "Advanced introspective parsing system for Aethero consciousness architecture"

# Export all public API components
__all__ = [
    # Core Introspective Components
    "ASLMetaParser",
    "ASLCognitiveTag", 
    "CognitiveMetricsAnalyzer",
    "AetheroReflectionAgent",
    "IntrospectiveLogger",
    "AetheroIntrospectiveEntity",
    
    # Enums for structured cognitive states
    "MentalStateEnum",
    "EmotionToneEnum",
    "TemporalContextEnum",
    
    # Legacy compatibility exports
    "ASLTagModel",
    "ReflectionAgent",
    "calculate_success_rate",
    "analyze_cognitive_load", 
    "generate_introspection_report",
    
    # Module metadata
    "__version__",
    "__author__",
    "__description__"
]

# Module initialization message for introspective transparency
import logging
_module_logger = logging.getLogger(__name__)
_module_logger.info(
    f"Aethero Introspective Parser Module v{__version__} initialized - "
    "Full cognitive transparency and constitutional compliance active"
)
