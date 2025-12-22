from multiprocessing import Process
from app.core.config import CONFIG

def run_tui():
    import tui_app
    tui_app.run_tui()

def run_api():
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=CONFIG["port"], reload=True)

if __name__ == "__main__":
    p1 = Process(target=run_api)
    p2 = Process(target=run_tui)
    p1.start()
    p2.start()
    p1.join()
    p2.join()