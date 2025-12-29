# memory/query_engine.py

from typing import List, Dict
from memory.local_store import LocalMemoryStore
from memory.embedding_store import EmbeddingStore


class MemoryQueryEngine:
    def __init__(self):
        self.store = LocalMemoryStore()
        self.embeddings = EmbeddingStore()
        self._index_memory()

    def _index_memory(self):
        meetings = self.store.load_all_meetings()

        for meeting in meetings:
            meeting_id = meeting["meeting_id"]

            # Index summaries
            if meeting.get("summary"):
                self.embeddings.add(
                    meeting["summary"],
                    {"meeting_id": meeting_id, "type": "summary"}
                )

            # Index actions
            for action in meeting.get("actions", []):
                text = f'{action.get("owner")} {action.get("task")} {action.get("deadline")}'
                self.embeddings.add(
                    text,
                    {"meeting_id": meeting_id, "type": "action"}
                )

            # Index transcript chunks
            for t in meeting.get("transcript", []):
                self.embeddings.add(
                    t["text"],
                    {
                        "meeting_id": meeting_id,
                        "speaker": t["speaker"],
                        "type": "transcript"
                    }
                )

    def ask(self, question: str) -> List[Dict]:
        """
        Returns most relevant memory items
        """
        return self.embeddings.search(question)
