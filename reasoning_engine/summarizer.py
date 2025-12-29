# reasoning_engine/summarizer.py

from typing import List, Dict


class MeetingSummarizer:
    """
    Generates a concise meeting summary.
    """

    def summarize(self, transcript: List[Dict], actions: List[Dict]) -> str:
        speakers = set(t["speaker"] for t in transcript)
        key_points = [t["text"] for t in transcript[:5]]

        summary = []
        summary.append(f"Participants: {', '.join(speakers)}")
        summary.append("")

        summary.append("Key discussion points:")
        for point in key_points:
            summary.append(f"- {point}")

        if actions:
            summary.append("")
            summary.append("Action items:")
            for action in actions:
                summary.append(
                    f"- {action['owner']} to {action['task']} ({action['deadline']})"
                )

        return "\n".join(summary)
