# reasoning_engine/conflict_detector.py

from typing import List, Dict


class ConflictDetector:
    """
    Detects potential conflicts in meeting discussion.
    """

    CONFLICT_KEYWORDS = [
        "but",
        "however",
        "not possible",
        "delay",
        "conflict",
        "disagree",
        "concern"
    ]

    def detect(self, transcript: List[Dict]) -> List[Dict]:
        conflicts = []

        for entry in transcript:
            text = entry["text"].lower()

            if any(keyword in text for keyword in self.CONFLICT_KEYWORDS):
                conflicts.append({
                    "speaker": entry["speaker"],
                    "text": entry["text"],
                    "time": entry["time"],
                    "type": "potential_conflict"
                })

        return conflicts
