# AETH-TASK-004 :: ROLE: Primus :: GOAL: Vercel-ready FastAPI application
# app_vercel.py
# Main FastAPI application optimized for Vercel deployment

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from datetime import datetime
import os
from contextlib import asynccontextmanager

# Setup logging for Vercel
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown"""
    # Startup
    logger.info("🚀 AetheroOS startup initiated")
    try:
        from reflection_agent_vercel import router as reflection_router
        app.include_router(reflection_router)
        logger.info("✅ Reflection router loaded successfully")
    except ImportError as e:
        logger.warning(f"⚠️ Reflection router not available: {e}")
        # Create fallback router
        from fastapi import APIRouter
        fallback_router = APIRouter(prefix="/reflection", tags=["reflection"])
        
        @fallback_router.get("/health")
        async def fallback_health():
            return {"status": "healthy", "mode": "fallback", "timestamp": datetime.now().isoformat()}
        
        app.include_router(fallback_router)
    
    yield
    
    # Shutdown
    logger.info("🔄 AetheroOS shutdown initiated")

# Create FastAPI app with optimized settings for Vercel
app = FastAPI(
    title="AetheroOS Introspective API",
    description="Introspective reflection and cognitive analysis system for AetheroOS",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware for web frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "message": "🧠 AetheroOS Introspective System",
        "version": "1.0.0",
        "deployment": "vercel",
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
            "deployment": "vercel",
            "timestamp": datetime.now().isoformat(),
            "environment": {
                "python_version": os.sys.version,
                "vercel_region": os.environ.get("VERCEL_REGION", "unknown")
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
        "deployment": "vercel",
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

# Global exception handler for better error reporting
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for better error reporting"""
    logger.error(f"Global exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc),
            "timestamp": datetime.now().isoformat(),
            "deployment": "vercel"
        }
    )

# Export for Vercel
handler = app

# Local development runner
if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting AetheroOS Introspective API locally")
    uvicorn.run(
        "app_vercel:app",
        host="0.0.0.0",
        port=7860,
        reload=True,
        log_level="info"
    )
