# memory/local_store.py

import os
from typing import List, Dict
from data.storage import DataStorage
from config.settings import AppSettings


class LocalMemoryStore(DataStorage):
    def __init__(self):
        super().__init__()
        self.meetings_dir = AppSettings.MEETINGS_DIR

    def list_meetings(self) -> List[str]:
        return [
            f.replace(".json", "")
            for f in os.listdir(self.meetings_dir)
            if f.endswith(".json")
        ]

    def load_meeting(self, meeting_id: str) -> Dict:
        path = os.path.join(self.meetings_dir, f"{meeting_id}.json")
        return self.read_json(path)

    def load_all_meetings(self) -> List[Dict]:
        meetings = []
        for meeting_id in self.list_meetings():
            data = self.load_meeting(meeting_id)
            if data:
                meetings.append(data)
        return meetings
