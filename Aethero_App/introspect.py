from fastapi import APIRouter

router = APIRouter()

@router.get("/crew/introspect")
async def introspect():
    return {"status": "Introspection endpoint active", "version": "1.0"}
