# data/log_store.py

import os
from datetime import datetime
from config.settings import AppSettings


class LogStore:
    def __init__(self, filename: str = "lexisync.log"):
        self.log_path = os.path.join(
            AppSettings.LOGS_DIR,
            filename
        )

    def log(self, level: str, message: str):
        timestamp = datetime.utcnow().isoformat()
        entry = f"[{timestamp}] [{level.upper()}] {message}\n"

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(entry)

    def info(self, message: str):
        self.log("info", message)

    def warning(self, message: str):
        self.log("warning", message)

    def error(self, message: str):
        self.log("error", message)
