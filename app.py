# app.py
import uvicorn
from app.core.config import CONFIG

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=CONFIG["port"],
        reload=True,
    )
