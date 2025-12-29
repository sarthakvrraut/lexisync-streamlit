# audio_pipeline/browser_audio.py

import av
import numpy as np
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
from audio_pipeline.audio_buffer import AudioBuffer


class AudioProcessor(AudioProcessorBase):
    def __init__(self, audio_buffer: AudioBuffer):
        self.audio_buffer = audio_buffer

    def recv_audio(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        audio = audio.astype(np.int16)

        # Convert stereo → mono
        if audio.ndim > 1:
            audio = np.mean(audio, axis=0).astype(np.int16)

        self.audio_buffer.put(audio)
        return frame


class AudioReceiver:
    def __init__(self, key: str = "lexisync-audio"):
        self.audio_buffer = AudioBuffer()
        self.key = key

    def start(self):
        webrtc_streamer(
            key=self.key,
            audio_processor_factory=lambda: AudioProcessor(self.audio_buffer),
            media_stream_constraints={
                "audio": True,
                "video": False,
            },
            async_processing=True,
        )

    def get_audio_chunk(self):
        return self.audio_buffer.get()

    def clear(self):
        self.audio_buffer.clear()
