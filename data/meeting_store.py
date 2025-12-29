# data/meeting_store.py

import os
from typing import Dict
from data.storage import DataStorage
from config.settings import AppSettings


class MeetingStore(DataStorage):
    def __init__(self, meeting_id: str):
        super().__init__()
        self.meeting_id = meeting_id
        self.meeting_path = os.path.join(
            AppSettings.MEETINGS_DIR,
            f"{meeting_id}.json"
        )

        if not os.path.exists(self.meeting_path):
            self._initialize()

    def _initialize(self):
        self.write_json(
            self.meeting_path,
            {
                "meeting_id": self.meeting_id,
                "created_at": self._timestamp(),
                "transcript": [],
                "actions": [],
                "conflicts": [],
                "summary": "",
                "languages": {}
            }
        )

    def append_transcript(self, speaker: str, text: str, language: str):
        data = self.read_json(self.meeting_path)
        data["transcript"].append({
            "time": self._timestamp(),
            "speaker": speaker,
            "text": text,
            "language": language
        })
        self.write_json(self.meeting_path, data)

    def save_actions(self, actions: list):
        data = self.read_json(self.meeting_path)
        data["actions"] = actions
        self.write_json(self.meeting_path, data)

    def save_conflicts(self, conflicts: list):
        data = self.read_json(self.meeting_path)
        data["conflicts"] = conflicts
        self.write_json(self.meeting_path, data)

    def save_summary(self, summary: str):
        data = self.read_json(self.meeting_path)
        data["summary"] = summary
        self.write_json(self.meeting_path, data)

    def load(self) -> Dict:
        return self.read_json(self.meeting_path)
