import zipfile
from datetime import datetime
import os

FILES = [
    "config/profiles.json",
    "config/templates.json",
    "config/settings.json"
]

def create_backup():
    if not os.path.exists("backups"):
        os.makedirs("backups")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"backups/config_backup_{timestamp}.zip"

    with zipfile.ZipFile(filename, "w") as zipf:
        for file in FILES:
            if os.path.exists(file):
                zipf.write(file)
