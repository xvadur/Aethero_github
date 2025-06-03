#!/usr/bin/env python3

print("Starting minimal test...")

try:
    print("Testing FastAPI import...")
    from fastapi import APIRouter
    print("✅ FastAPI imported")
    
    print("Creating router...")
    router = APIRouter(prefix="/test", tags=["test"])
    print("✅ Router created")
    
    print("Testing Pydantic...")
    from pydantic import BaseModel
    print("✅ Pydantic imported")
    
    class TestModel(BaseModel):
        text: str
    
    print("✅ Model created")
    
    @router.get("/test")
    async def test_endpoint():
        return {"status": "working"}
    
    print("✅ Endpoint created")
    
    print("All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
