# data/storage.py

import os
import json
from datetime import datetime
from config.settings import AppSettings


class DataStorage:
    def __init__(self):
        AppSettings.ensure_directories()

    @staticmethod
    def _timestamp():
        return datetime.utcnow().isoformat()

    @staticmethod
    def write_json(path: str, data: dict):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def read_json(path: str):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
