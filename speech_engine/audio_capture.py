import queue
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
CHANNELS = 1
DTYPE = "int16"


class MicrophoneStream:
    def __init__(self):
        self.q = queue.Queue()
        self.stream = None

    def _callback(self, indata, frames, time, status):
        if status:
            print("Audio status:", status)
        self.q.put(bytes(indata))

    def start(self):
        self.stream = sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=3200,
            dtype=DTYPE,
            channels=CHANNELS,
            callback=self._callback,
        )
        self.stream.start()

    def generator(self):
        while True:
            chunk = self.q.get()
            if chunk is None:
                return
            yield chunk

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.q.put(None)
