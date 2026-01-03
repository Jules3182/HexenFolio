import yaml
from app.core.config import CONFIG_PATH

def get_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def save_config(config: dict):
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f, sort_keys=False)

def get_theme():
    config = get_config()
    return config.get("theme", "neo.css")

def set_theme(theme: str):
    config = get_config()
    config["theme"] = theme
    save_config(config)
    return theme