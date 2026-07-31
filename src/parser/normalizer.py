import unicodedata
import string


def normalize(tokens: list[str]) -> list[str]:
    normalized = []

    for token in tokens:
        token = token.lower()

        token = unicodedata.normalize('NFD', token)
        
        token = "".join(c for c in token if unicodedata.category(c) != 'Mn')

        normalized.append(token)

    return normalized
