def assign_speaker(speaker_id: int) -> str:
    return f"Speaker {speaker_id + 1}"


def format_speaker_line(speaker: str, text: str):
    return f"{speaker}: {text}"
