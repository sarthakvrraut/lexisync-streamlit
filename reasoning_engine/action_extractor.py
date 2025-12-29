# reasoning_engine/action_extractor.py

import re
from typing import List, Dict


class ActionExtractor:
    """
    Extracts action items from transcript text.
    """

    ACTION_PATTERNS = [
        r"(?P<owner>\w+)\s+will\s+(?P<task>.+?)\s+by\s+(?P<deadline>.+)",
        r"(?P<task>.+?)\s+assigned\s+to\s+(?P<owner>\w+)",
    ]

    def extract(self, transcript: List[Dict]) -> List[Dict]:
        actions = []

        for entry in transcript:
            text = entry["text"]

            for pattern in self.ACTION_PATTERNS:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    actions.append({
                        "owner": match.groupdict().get("owner", "Unassigned"),
                        "task": match.groupdict().get("task", text),
                        "deadline": match.groupdict().get("deadline", "Not specified"),
                        "source": text
                    })

        return actions
