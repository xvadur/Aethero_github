# app.py
# Main FastAPI application for AetheroOS Introspective System
# Integrates reflection agent and other Aethero components

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from datetime import datetime

# Import Aethero modules
from reflection_agent import router as reflection_router

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="AetheroOS Introspective API",
    description="Introspective reflection and cognitive analysis system for AetheroOS",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for web frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reflection_router)

@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "message": "🧠 AetheroOS Introspective System",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "docs": "/docs",
            "reflection": "/reflection",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Main system health check"""
    try:
        return {
            "status": "healthy",
            "system": "AetheroOS Introspective API",
            "timestamp": datetime.now().isoformat(),
            "components": {
                "reflection_agent": "active",
                "fastapi": "running"
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
        "component": "Introspective API",
        "version": "1.0.0",
        "capabilities": [
            "emotion_analysis",
            "introspective_reflection",
            "cognitive_metrics",
            "constitutional_alignment"
        ],
        "endpoints": [
            "/reflection/reflect",
            "/reflection/health", 
            "/reflection/capabilities"
        ]
    }

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for better error reporting"""
    logger.error(f"Global exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc),
            "timestamp": datetime.now().isoformat()
        }
    )

if __name__ == "__main__":
    import uvicorn
    
    logger.info("🚀 Starting AetheroOS Introspective API")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=7860,
        reload=True,
        log_level="info"
    )
