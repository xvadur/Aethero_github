# AetheroOS Semantic Layer (ASL) Tags Reference

## Overview
ASL tags provide semantic metadata for tracking and organizing outputs throughout the research pipeline. This document defines standard tag structures and conventions for use across all agents.

## Common Tag Structure
```json
{
  "agent_role": string,      // The role of the agent generating the output
  "stage": string,          // Pipeline stage identifier
  "timestamp": string,      // ISO 8601 format
  "version": string,        // Format: "v1.0"
  "project_id": string      // Unique project identifier
}
```

## Agent-Specific Tags

### PlannerAgent
```json
{
  "agent_role": "planner",
  "stage": "planning",
  "stream_id": string,
  "stream_type": "research/development/analysis",
  "priority_level": "high/medium/low",
  "complexity": "high/medium/low",
  "estimated_duration": string
}
```

### ScoutAgent
```json
{
  "agent_role": "scout",
  "stage": "discovery",
  "content_type": "tool/dataset/paper",
  "relevance_to_stream": "high/medium/low",
  "source_type": "academic/technical/documentation",
  "accessibility": "open/restricted/commercial",
  "last_updated": string,
  "reliability_score": number
}
```

### AnalystAgent
```json
{
  "agent_role": "analyst",
  "stage": "analysis",
  "validation_status": "validated/rejected/pending",
  "utility_score": number,
  "confidence_level": "high/medium/low",
  "analysis_depth": "detailed/overview",
  "critical_findings": string[],
  "limitations": string[]
}
```

### GeneratorAgent
```json
{
  "agent_role": "generator",
  "stage": "generation",
  "artifact_type": "code/documentation/schema/config",
  "language": string,
  "generation_status": "complete/draft/prototype",
  "complexity_level": "basic/intermediate/advanced",
  "dependencies": string[],
  "intended_use": "production/testing/demonstration"
}
```

### SynthesisAgent
```json
{
  "agent_role": "synthesizer",
  "stage": "synthesis",
  "report_status": "finalized/draft",
  "synthesis_scope": "comprehensive/focused",
  "confidence_level": "high/medium/low",
  "completion_status": "complete/partial",
  "key_findings": string[],
  "recommendations": string[]
}
```

## Usage Guidelines

### 1. Tag Application
- Include all relevant common tags
- Add agent-specific tags as needed
- Maintain consistent formatting
- Use predefined values where specified

### 2. Value Conventions
- Use lowercase for keys
- Use predefined enums where specified
- Use ISO 8601 for dates/times
- Use semantic versioning

### 3. Validation Rules
- All common tags are required
- Agent-specific tags are required for respective agents
- Arrays should not be empty when included
- Scores should be 1-10 when applicable

### 4. Examples

#### Research Plan Tag
```json
{
  "agent_role": "planner",
  "stage": "planning",
  "timestamp": "2025-05-28T22:30:49Z",
  "version": "v1.0",
  "project_id": "AETH-2025-001",
  "stream_id": "stream_1",
  "stream_type": "research",
  "priority_level": "high",
  "complexity": "medium",
  "estimated_duration": "2 weeks"
}
```

#### Source Analysis Tag
```json
{
  "agent_role": "analyst",
  "stage": "analysis",
  "timestamp": "2025-05-28T23:15:22Z",
  "version": "v1.0",
  "project_id": "AETH-2025-001",
  "validation_status": "validated",
  "utility_score": 8,
  "confidence_level": "high",
  "analysis_depth": "detailed",
  "critical_findings": [
    "Strong empirical evidence",
    "Recent publication",
    "Active maintenance"
  ]
}
```

## Best Practices

1. **Consistency**
   - Use consistent terminology
   - Maintain standard formats
   - Follow naming conventions
   - Apply tags systematically

2. **Completeness**
   - Include all required tags
   - Provide meaningful values
   - Document special cases
   - Explain deviations

3. **Clarity**
   - Use clear descriptions
   - Avoid ambiguity
   - Document assumptions
   - Explain complex values

4. **Maintenance**
   - Update tags as needed
   - Track version changes
   - Document modifications
   - Maintain backwards compatibility
