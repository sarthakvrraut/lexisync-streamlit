# audio_pipeline/stream_controller.py

import numpy as np

TARGET_SAMPLE_RATE = 16000


class StreamController:
    def __init__(self, audio_receiver):
        self.audio_receiver = audio_receiver
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
        self.audio_receiver.clear()

    def read_pcm_chunk(self):
        """
        Returns 16kHz PCM audio ready for Google STT
        """
        if not self.running:
            return None

        chunk = self.audio_receiver.get_audio_chunk()
        if chunk is None:
            return None

        # Ensure int16 PCM
        pcm = chunk.astype(np.int16)
        return pcm.tobytes()
