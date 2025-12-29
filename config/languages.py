# config/languages.py

SUPPORTED_LANGUAGES = {
    "English": {
        "code": "en-US",
        "label": "English"
    },
    "Hindi": {
        "code": "hi-IN",
        "label": "हिन्दी"
    },
    "Spanish": {
        "code": "es-ES",
        "label": "Español"
    },
    "French": {
        "code": "fr-FR",
        "label": "Français"
    },
    "German": {
        "code": "de-DE",
        "label": "Deutsch"
    },
    "Tamil": {
        "code": "ta-IN",
        "label": "தமிழ்"
    },
    "Telugu": {
        "code": "te-IN",
        "label": "తెలుగు"
    },
    "Marathi": {
        "code": "mr-IN",
        "label": "मराठी"
    }
}


def get_language_code(language_name: str) -> str:
    """
    Returns language code for given language name
    """
    return SUPPORTED_LANGUAGES.get(language_name, {}).get("code", "en-US")
