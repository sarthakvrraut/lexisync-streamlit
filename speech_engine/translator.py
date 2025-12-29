# speech_engine/translator.py
from googletrans import Translator
from utils.logger import get_logger

logger = get_logger(__name__)

class LiveTranslator:
    def __init__(self, target_language="en"):
        self.translator = Translator()
        self.target_language = target_language

    def translate_text(self, text):
        if not text:
            return ""
        try:
            result = self.translator.translate(text, dest=self.target_language)
            return result.text
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            return text
