# audio_pipeline/audio_buffer.py

import queue
import numpy as np

class AudioBuffer:
    def __init__(self, max_chunks: int = 200):
        self.buffer = queue.Queue(maxsize=max_chunks)

    def put(self, audio_chunk: np.ndarray):
        if not self.buffer.full():
            self.buffer.put(audio_chunk)

    def get(self):
        if not self.buffer.empty():
            return self.buffer.get()
        return None

    def clear(self):
        with self.buffer.mutex:
            self.buffer.queue.clear()

    def is_empty(self):
        return self.buffer.empty()
