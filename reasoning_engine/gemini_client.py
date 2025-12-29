# reasoning_engine/gemini_client.py
import os
import openai
from utils.logger import get_logger

logger = get_logger(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

class GeminiReasoningEngine:
    """
    Replacement for deprecated Gemini API.
    Uses OpenAI GPT for reasoning / summarization.
    """
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def analyze_transcript(self, transcript):
        """
        Returns summarized action items or insights
        """
        if not transcript:
            return "No transcript provided"

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Extract action items and insights from the meeting transcript."},
                    {"role": "user", "content": transcript},
                ],
                temperature=0
            )
            summary = response.choices[0].message.content.strip()
            return summary
        except Exception as e:
            logger.error(f"GeminiReasoningEngine error: {e}")
            return "Error generating summary"
