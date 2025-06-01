# AetheroOS Memory Ingestion Agent

## Overview

The AetheroOS Memory Ingestion Agent is a specialized module for processing and storing memories within the AetheroOS ecosystem. It handles the ritualized transformation of raw input into properly formatted ministerial reports, complete with metadata, inferred tags, and multiple output formats.

## Features

- **Multiple Input Formats**
  - Direct text input
  - File input (.txt, .md, .json)
  - JSON payload

- **Automated Tag Generation**
  - Intent Vector Analysis
  - Mental State Detection
  - Emotion Tone Assessment

- **Templated Report Generation**
  - Default ministerial template
  - Support for custom templates
  - Jinja2 templating engine

- **Multiple Output Formats**
  - Markdown (.md)
  - JSON metadata
  - PDF (optional, requires pdfkit)

- **Validation Integration**
  - Optional Blackbox validation
  - Extensible validation pipeline

## Installation

```bash
# Install required dependencies
pip install jinja2

# Optional: Install PDF support
pip install pdfkit
```

## Usage

### Basic Usage

```bash
# Ingest text directly
python aeth_ingest.py --text "Memory content to ingest"

# Ingest from file
python aeth_ingest.py --file input.txt

# Ingest JSON
python aeth_ingest.py --json '{"content": "Memory data"}'
```

### Advanced Options

```bash
# Custom reference code
python aeth_ingest.py --text "Content" --ref_code "CUSTOM-2024-001"

# Add custom tags
python aeth_ingest.py --text "Content" --tags "important" "urgent"

# Use custom template
python aeth_ingest.py --text "Content" --template custom_template.md

# Generate PDF output
python aeth_ingest.py --text "Content" --pdf

# Enable Blackbox validation
python aeth_ingest.py --text "Content" --validate

# Debug mode
python aeth_ingest.py --text "Content" --debug
```

### Full Command Reference

```bash
python aeth_ingest.py [OPTIONS]

Options:
  --text TEXT         Input text to ingest
  --file PATH        Input file path (.txt, .md, .json)
  --json JSON        Input JSON payload
  --ref_code CODE    Custom reference code
  --author NAME      Author of the report (default: AetheroGPT)
  --tags [TAGS...]   Custom tags for the report
  --source SOURCE    Source of the content
  --template PATH    Custom Jinja2 template path
  --validate        Trigger Blackbox validation
  --pdf             Generate PDF output
  --debug           Enable debug logging
```

## Output Structure

### Directory Structure

```
aeth_mem_reports/
├── AETH-MEM-2024-0001.md    # Markdown report
├── AETH-MEM-2024-0001.json  # Metadata
└── AETH-MEM-2024-0001.pdf   # PDF (if enabled)
```

### Markdown Report Format

```markdown
### AETHEROOS MINISTERIAL REPORT
**Office of Memory Ingestion**  
**Ref. Code**: AETH-MEM-2024-0001  

---

**Date**: 2024-02-20  
**Author**: AetheroGPT  
**Tags**: important, urgent  
**Source**: user_input  

---

#### **🪶 CONTENT**  
[Memory content here]

---

#### **🪶 INFERRED TAGS**  
- Intent Vector: analysis  
- Mental State: focused  
- Emotion Tone: neutral  

---

**Ministerial Seal**: [ ⚜️ ]  
```

### JSON Metadata Format

```json
{
  "ref_code": "AETH-MEM-2024-0001",
  "date": "2024-02-20",
  "author": "AetheroGPT",
  "tags": ["important", "urgent"],
  "source": "user_input",
  "inferred_tags": {
    "intent_vector": "analysis",
    "mental_state": "focused",
    "emotion_tone": "neutral"
  }
}
```

## Error Handling

The agent includes comprehensive error handling for:
- Invalid input
- Missing files
- Template errors
- File system errors
- PDF generation failures

All errors are logged with appropriate detail level and include specific error messages.

## Testing

Run the test suite:

```bash
pytest tests/test_aeth_ingest.py -v
```

The test suite covers:
- Input parsing
- Tag generation
- Report rendering
- File operations
- Error handling
- Integration tests

## Development

### Adding New Features

1. Tag Generation:
   - Extend `generate_tags()` in `aeth_ingest.py`
   - Add new tag categories or detection logic

2. Custom Templates:
   - Create new template in markdown format
   - Use Jinja2 syntax for dynamic content
   - Place in templates directory

3. Output Formats:
   - Add new format handlers in `save_report()`
   - Update return type annotations
   - Add corresponding tests

### Best Practices

- Always add tests for new features
- Follow type hints and docstrings
- Use logging for debugging
- Handle errors gracefully
- Clean up temporary files

## Integration

### Blackbox Integration

The `trigger_blackbox()` function is a placeholder for integration with the AetheroOS validation system. Implement this function according to your specific Blackbox interface requirements.

Example implementation:

```python
def trigger_blackbox(report_path: str) -> None:
    """
    Trigger Blackbox validation subprocess.
    
    Args:
        report_path: Path to the report file to validate
    """
    try:
        result = subprocess.run(
            ["blackbox", "--analyze", report_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logger.error(f"Validation failed: {result.stderr}")
        else:
            logger.info(f"Validation succeeded: {result.stdout}")
    except Exception as e:
        logger.error(f"Validation error: {str(e)}")
```

## License

This software is part of the AetheroOS ecosystem and is subject to the AetheroOS license terms.
