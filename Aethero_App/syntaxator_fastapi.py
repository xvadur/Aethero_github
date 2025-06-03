from fastapi import FastAPI, WebSocket, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel
from introspective_parser_module.parser import ASLMetaParser
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer
from introspective_parser_module.reflection_agent import AetheroReflectionAgent
from crewai.team_api import router as crewai_router
import asyncio
import logging
import traceback
from datetime import datetime
import time
import uuid

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("aethero_fastapi.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Request tracking
request_stats = {
    "total_requests": 0,
    "parse_requests": 0,
    "metrics_requests": 0,
    "reflect_requests": 0,
    "health_checks": 0,
    "errors": 0,
    "start_time": datetime.now()
}

app = FastAPI(
    title="Aethero Cognitive Flow API",
    description="Advanced cognitive parsing and introspective analysis system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware for security
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # Configure appropriately for production
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Log request
    logger.info(f"REQUEST [{request_id}] {request.method} {request.url.path} - Client: {request.client.host}")
    
    # Update stats
    request_stats["total_requests"] += 1
    
    try:
        response = await call_next(request)
        process_time = time.time() - start_time
        
        # Log response
        logger.info(f"RESPONSE [{request_id}] Status: {response.status_code} - Time: {process_time:.3f}s")
        
        # Add custom headers
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(process_time)
        
        return response
    except Exception as e:
        process_time = time.time() - start_time
        request_stats["errors"] += 1
        logger.error(f"ERROR [{request_id}] {str(e)} - Time: {process_time:.3f}s")
        raise

# Pydantic models for request validation
class ParseRequest(BaseModel):
    text: str
    
    class Config:
        schema_extra = {
            "example": {
                "text": "[@cognitive_load:7 @certainty:0.85 @mental_state:focused @emotion:analytical] This is a test of ASL parsing."
            }
        }

class MetricsRequest(BaseModel):
    data: str
    
    class Config:
        schema_extra = {
            "example": {
                "data": "[@cognitive_load:8 @certainty:0.9 @mental_state:contemplative @emotion:empathetic] Deep cognitive analysis test."
            }
        }

class ReflectRequest(BaseModel):
    text: str
    context: str = "general"
    
    class Config:
        schema_extra = {
            "example": {
                "text": "[@cognitive_load:9 @certainty:0.95 @mental_state:focused @emotion:analytical] Reflecting on cognitive patterns.",
                "context": "system_analysis"
            }
        }

# Response models
class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str
    service: str
    uptime_seconds: float
    stats: dict

class ParseResponse(BaseModel):
    parsed_data: dict
    status: str

class MetricsResponse(BaseModel):
    analysis_report: dict
    status: str

class ReflectResponse(BaseModel):
    reflection_result: dict
    context: str
    timestamp: str
    status: str

@app.get("/", 
         summary="Root Endpoint", 
         description="Welcome message and API information",
         tags=["General"])
def read_root():
    return {"message": "Welcome to AetheroOS Syntaxator API!", "version": "1.0.0"}

@app.post("/parse", 
          summary="Parse ASL Text", 
          description="Parse and validate ASL (Aethero Semantic Language) text with cognitive pattern recognition",
          response_model=ParseResponse,
          tags=["Cognitive Processing"])
def parse_asl(request: ParseRequest):
    try:
        request_stats["parse_requests"] += 1
        logger.info(f"Parsing request received: {len(request.text)} characters")
        parser = ASLMetaParser()
        result = parser.parse_and_validate(request.text)
        logger.info("Parse completed successfully")
        return {"parsed_data": result, "status": "success"}
    except Exception as e:
        request_stats["errors"] += 1
        logger.error(f"Parse error: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Parse error: {str(e)}")

@app.post("/metrics", 
          summary="Analyze Cognitive Metrics", 
          description="Generate comprehensive introspective cognitive analysis and consciousness coherence metrics",
          response_model=MetricsResponse,
          tags=["Cognitive Processing"])
def analyze_metrics(request: MetricsRequest):
    try:
        request_stats["metrics_requests"] += 1
        logger.info(f"Metrics analysis request received: {len(request.data)} characters")
        
        # First parse the text to get cognitive tags
        parser = ASLMetaParser()
        parsed_result = parser.parse_and_validate(request.data)
        
        # Extract cognitive tags from parsed result
        cognitive_tags = []
        if parsed_result and 'parsing_results' in parsed_result:
            for result in parsed_result['parsing_results']:
                if result.get('is_valid') and result.get('validated_model'):
                    cognitive_tags.append(result['validated_model'])
        
        # If no valid tags found, create a basic analysis
        if not cognitive_tags:
            logger.warning("No valid cognitive tags found, creating basic analysis")
            return {
                "analysis_report": {
                    "message": "No cognitive tags detected in input text",
                    "basic_analysis": {
                        "text_length": len(request.data),
                        "timestamp": datetime.now().isoformat()
                    }
                },
                "status": "basic_analysis"
            }
        
        # Generate analysis with cognitive tags
        analyzer = CognitiveMetricsAnalyzer()
        report = analyzer.generate_introspective_report(cognitive_tags)
        logger.info("Metrics analysis completed successfully")
        
        return {"analysis_report": report, "status": "success"}
    except Exception as e:
        request_stats["errors"] += 1
        logger.error(f"Metrics analysis error: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Metrics analysis error: {str(e)}")

@app.post("/reflect", 
          summary="Introspective Reflection", 
          description="Generate deep introspective analysis using AetheroReflectionAgent for consciousness evolution tracking",
          response_model=ReflectResponse,
          tags=["Cognitive Processing"])
def reflect_analysis(request: ReflectRequest):
    try:
        request_stats["reflect_requests"] += 1
        logger.info(f"Reflection request received: {len(request.text)} characters, context: {request.context}")
        
        # Initialize reflection agent
        reflection_agent = AetheroReflectionAgent()
        
        # Perform introspective analysis using the correct method signature
        reflection_result = reflection_agent.reflect_on_input(request.text)
        
        logger.info("Reflection analysis completed successfully")
        return {
            "reflection_result": reflection_result,
            "context": request.context,
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        }
    except Exception as e:
        request_stats["errors"] += 1
        logger.error(f"Reflection error: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Reflection error: {str(e)}")

@app.get("/health", 
         summary="Health Check", 
         description="Check API health status with comprehensive system metrics and uptime information",
         response_model=HealthResponse,
         tags=["Monitoring"])
def health_check():
    request_stats["health_checks"] += 1
    uptime = datetime.now() - request_stats["start_time"]
    
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "service": "Aethero Cognitive Flow API",
        "uptime_seconds": uptime.total_seconds(),
        "stats": request_stats
    }

@app.get("/metrics", 
         summary="System Metrics", 
         description="Get comprehensive system performance metrics and request statistics",
         tags=["Monitoring"])
def get_system_metrics():
    uptime = datetime.now() - request_stats["start_time"]
    
    return {
        "system_metrics": {
            "uptime_seconds": uptime.total_seconds(),
            "total_requests": request_stats["total_requests"],
            "requests_per_endpoint": {
                "parse": request_stats["parse_requests"],
                "metrics": request_stats["metrics_requests"],
                "reflect": request_stats["reflect_requests"],
                "health": request_stats["health_checks"]
            },
            "error_rate": request_stats["errors"] / max(request_stats["total_requests"], 1),
            "average_requests_per_minute": request_stats["total_requests"] / max(uptime.total_seconds() / 60, 1)
        },
        "timestamp": datetime.now().isoformat()
    }

@app.get("/logs",
         summary="Get Application Logs",
         description="Retrieve application logs and system information",
         tags=["Monitoring"])
def get_logs():
    return {"logs": "This is a placeholder for logs.", "timestamp": datetime.now().isoformat()}

@app.websocket("/logs/stream")
async def stream_logs(websocket: WebSocket):
    """WebSocket endpoint for real-time log streaming"""
    await websocket.accept()
    logger.info("WebSocket connection established for log streaming")
    
    try:
        for i in range(5):
            log_message = {
                "timestamp": datetime.now().isoformat(),
                "level": "INFO",
                "message": f"Real-time log message {i+1}",
                "source": "aethero_fastapi"
            }
            await websocket.send_json(log_message)
            await asyncio.sleep(1)
        
        await websocket.send_json({
            "timestamp": datetime.now().isoformat(),
            "level": "INFO",
            "message": "Log streaming completed",
            "source": "aethero_fastapi"
        })
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
    finally:
        await websocket.close()
        logger.info("WebSocket connection closed")

# Include CrewAI router
app.include_router(crewai_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
