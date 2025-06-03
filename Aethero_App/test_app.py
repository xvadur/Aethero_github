#!/usr/bin/env python3
"""
Simple FastAPI test application
"""

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any

print("Starting simple FastAPI test...")

app = FastAPI(title="AetheroOS Test API")

# Simple test model
class TestInput(BaseModel):
    text: str

class TestOutput(BaseModel):
    text: str
    status: str
    timestamp: str

# Create router
router = APIRouter(prefix="/test", tags=["test"])

@router.post("/echo")
async def echo_text(input_data: TestInput):
    """Simple echo endpoint"""
    from datetime import datetime
    return TestOutput(
        text=input_data.text,
        status="success",
        timestamp=datetime.now().isoformat()
    )

@router.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}

# Include router in app
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AetheroOS Test API"}

if __name__ == "__main__":
    import uvicorn
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=7860)
