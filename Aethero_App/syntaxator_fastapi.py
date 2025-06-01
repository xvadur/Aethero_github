from fastapi import FastAPI
from introspective_parser_module.parser import ASLMetaParser
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer
from introspective_parser_module.reflection_agent import AetheroReflectionAgent

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AetheroOS Syntaxator API!"}

@app.post("/parse")
def parse_asl(data: dict):
    parser = ASLMetaParser()
    result = parser.parse_and_validate(data)
    return {"parsed_data": result}

@app.post("/analyze")
def analyze_metrics(data: dict):
    analyzer = CognitiveMetricsAnalyzer()
    report = analyzer.generate_introspective_report(data)
    return {"analysis_report": report}

@app.post("/reflect")
def reflect(data: dict):
    agent = AetheroReflectionAgent()
    reflection = agent.reflect(data)
    return {"reflection": reflection}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
