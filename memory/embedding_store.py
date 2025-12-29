# memory/embedding_store.py

import math
from typing import List, Dict


class EmbeddingStore:
    """
    Very lightweight embedding store.
    Replace with Gemini / Vertex embeddings later.
    """

    def __init__(self):
        self.vectors = []

    def _text_to_vector(self, text: str) -> List[float]:
        """
        Simple deterministic embedding (hash-based).
        """
        vector = [0.0] * 10
        for i, char in enumerate(text):
            vector[i % 10] += ord(char)
        norm = math.sqrt(sum(v * v for v in vector))
        return [v / norm for v in vector] if norm else vector

    def add(self, text: str, metadata: Dict):
        vector = self._text_to_vector(text)
        self.vectors.append({
            "vector": vector,
            "text": text,
            "metadata": metadata
        })

    def similarity(self, v1: List[float], v2: List[float]) -> float:
        return sum(a * b for a, b in zip(v1, v2))

    def search(self, query: str, top_k: int = 3):
        query_vec = self._text_to_vector(query)

        scored = [
            (self.similarity(query_vec, item["vector"]), item)
            for item in self.vectors
        ]

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:top_k]]
