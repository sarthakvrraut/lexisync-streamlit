import re


def clean_transcript(text: str) -> str:
    if not text:
        return ""

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = text.replace(" uh ", " ").replace(" um ", " ")

    return text


def is_meaningful(text: str) -> bool:
    if not text:
        return False

    return len(text.split()) >= 3
