import json
from datetime import datetime
import random
import os

CONFIG_PATH = "config/templates.json"

def load_templates():
    if not os.path.exists(CONFIG_PATH):
        return {"templates": []}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def render_text():
    data = load_templates()
    if not data["templates"]:
        return "Kein Text definiert."

    template = random.choice(data["templates"])

    now = datetime.now()
    text = template.replace("{datum}", now.strftime(data["placeholders"]["datum_format"]))
    text = text.replace("{uhrzeit}", now.strftime(data["placeholders"]["uhrzeit_format"]))
    text = text.replace("{link}", data["default_link"])

    return text
