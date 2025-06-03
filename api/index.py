# AETH-TASK-005 :: ROLE: Lucius :: GOAL: Vercel FastAPI Entry Point
# api/index.py
# Main entry point for Vercel deployment

import sys
import os

# Add Aethero_App to Python path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Aethero_App'))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from datetime import datetime

# Setup logging for Vercel
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app optimized for Vercel serverless
app = FastAPI(
    title="🧠 AetheroOS Production API",
    description="Introspective AI system for productivity analysis - Vercel Production",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "message": "🧠 AetheroOS Production API",
        "version": "1.0.0",
        "deployment": "vercel-production",
        "timestamp": datetime.now().isoformat(),
        "status": "operational",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "reflection": "/reflection",
            "system": "/system/info"
        }
    }

@app.get("/health")
async def health_check():
    """Production health check"""
    try:
        return {
            "status": "healthy",
            "system": "AetheroOS Production",
            "deployment": "vercel",
            "timestamp": datetime.now().isoformat(),
            "environment": {
                "python_version": sys.version,
                "vercel_region": os.environ.get("VERCEL_REGION", "unknown"),
                "function_name": os.environ.get("AWS_LAMBDA_FUNCTION_NAME", "api-index")
            }
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="System unhealthy")

@app.get("/system/info")
async def system_info():
    """Get system information and capabilities"""
    return {
        "system": "AetheroOS",
        "component": "Production API",
        "version": "1.0.0",
        "deployment": "vercel",
        "capabilities": [
            "emotion_analysis",
            "introspective_reflection", 
            "cognitive_metrics",
            "productivity_analysis",
            "constitutional_alignment"
        ],
        "ministers": {
            "primus": "strategic_logic_parser",
            "lucius": "implementation_execution", 
            "archivus": "memory_introspection",
            "frontinus": "ui_visualizations"
        }
    }

# Try to import reflection agent
try:
    from reflection_agent_vercel import router as reflection_router
    app.include_router(reflection_router, prefix="/reflection", tags=["reflection"])
    logger.info("✅ Reflection agent router loaded successfully")
except ImportError as e:
    logger.warning(f"⚠️ Reflection router not available: {e}")
    
    # Create fallback reflection endpoints
    @app.get("/reflection/health")
    async def reflection_fallback_health():
        return {
            "status": "healthy", 
            "mode": "fallback", 
            "timestamp": datetime.now().isoformat()
        }
    
    @app.post("/reflection/analyze")
    async def reflection_fallback_analyze():
        return {
            "analysis": "Fallback mode - full reflection agent not loaded",
            "timestamp": datetime.now().isoformat(),
            "mode": "minimal"
        }

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for production"""
    logger.error(f"Global exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc),
            "timestamp": datetime.now().isoformat(),
            "deployment": "vercel-production"
        }
    )

# Export for Vercel
app = app  # Make sure app is available at module level
