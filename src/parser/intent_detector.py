from schemas.intent import Intent
from parser.vocabulary import VOCABULARY



def intent_detect(tokens: list[str]) -> Intent:
    """Detector de intenção"""

    for token in tokens:
        for intent, words in VOCABULARY.items():
            if token in words:
                return intent

    return Intent.UNKNOWN

