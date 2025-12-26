import uvicorn
from app.core.config import CONFIG

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=CONFIG["host_ip"],
        port=CONFIG["port"],
        reload=CONFIG["reload_on"],
    )
