# speech_engine/stt_client.py
import whisper
from utils.logger import get_logger

logger = get_logger(__name__)

class SpeechToTextClient:
    def __init__(self, model_name="base"):
        try:
            self.model = whisper.load_model(model_name)
            logger.info(f"Whisper model '{model_name}' loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load Whisper model '{model_name}': {e}")
            self.model = None

    def transcribe(self, audio_file_path):
        if not self.model:
            return ""
        try:
            result = self.model.transcribe(audio_file_path)
            return result["text"]
        except Exception as e:
            logger.error(f"Whisper transcription error: {e}")
            return ""
