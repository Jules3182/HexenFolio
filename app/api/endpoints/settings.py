from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path
import glob

from app.services.settings_service import get_theme, set_theme

router = APIRouter()

THEMES_DIR = Path("../app/static/themes")

class ThemeRequest(BaseModel):
    theme: str


@router.get("/theme")
def read_theme():
    return {"theme": get_theme()}


@router.post("/theme")
def update_theme(req: ThemeRequest):
    theme = set_theme(req.theme)
    return {"theme": theme}


@router.get("/themes")
def list_themes():
    themes = [f.name for f in THEMES_DIR.glob("*.css")]
    return {"themes": themes}