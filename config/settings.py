# config/settings.py

import os


class AppSettings:
    """
    Central configuration for LexiSync (Streamlit)
    """

    APP_NAME = "LexiSync"
    APP_VERSION = "0.1.0"

    # Audio
    AUDIO_SAMPLE_RATE = 16000
    AUDIO_CHANNELS = 1

    # Streamlit
    STREAMLIT_PAGE_TITLE = "LexiSync – Multilingual Meeting Assistant"
    STREAMLIT_LAYOUT = "wide"

    # Reasoning
    GEMINI_MODEL = "models/gemini-1.5-pro"

    # Storage (local for Streamlit)
    DATA_DIR = os.getenv("LEXISYNC_DATA_DIR", "data")
    MEETINGS_DIR = os.path.join(DATA_DIR, "meetings")
    LOGS_DIR = os.path.join(DATA_DIR, "logs")

    @staticmethod
    def ensure_directories():
        """
        Ensure required local directories exist
        """
        os.makedirs(AppSettings.MEETINGS_DIR, exist_ok=True)
        os.makedirs(AppSettings.LOGS_DIR, exist_ok=True)
