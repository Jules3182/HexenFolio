from fastapi import APIRouter
from app.services.history_service import get_history

router = APIRouter()

@router.get("/")
def history():
    return get_history()