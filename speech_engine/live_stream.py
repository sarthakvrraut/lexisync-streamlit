from speech_engine.audio_capture import MicrophoneStream
from speech_engine.stt_client import SpeechToTextClient
from speech_engine.translator import LiveTranslator
from utils.text_utils import clean_transcript, is_meaningful

class LiveSpeechEngine:
    def __init__(self, input_languages, output_language):
        self.mic = MicrophoneStream()
        self.stt = SpeechToTextClient()
        self.translator = LiveTranslator(output_language)

    def start(self):
        self.mic.start()
        audio_gen = self.mic.generator()
        responses = self.stt.streaming_recognize(audio_gen)
        return responses

    def stop(self):
        self.mic.stop()

    def process_responses(self, responses):
        for response in responses:
            transcript = clean_transcript(response.get("text", response.get("transcription", "")))
            if not is_meaningful(transcript):
                continue

            translated = self.translator.translate_text(transcript)

            yield {
                "original": transcript,
                "translated": translated,
                "is_final": True,  # Whisper doesn't give partial by default
            }
