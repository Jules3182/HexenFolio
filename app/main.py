from fastapi import FastAPI
from app.api.router import api_router
from app.core.lifespan import lifespan
from app.core.config import CONFIG
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(
    title="HexFolio",
    version="0.2.2",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")

# Defaults to dashboard
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html", 
        {
            "request": request,
            "theme": CONFIG.get("theme", "neo")
        }
    )

# Route to holdings page
@app.get("/holdings", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "holdings.html", 
        {
            "request": request,
            "theme": CONFIG.get("theme", "neo")
        }
    )

# Route to settings page
@app.get("/settings", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "settings.html", 
        {
            "request": request,
            "theme": CONFIG.get("theme", "neo")
        }
    )