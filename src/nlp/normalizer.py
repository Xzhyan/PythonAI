import unicodedata


def text_lower(text):
    """Transforma o texto de entrada todo em minúsculo"""

    return text.lower()



def remove_accents(text):
    """Remove acentos como ex: ~^"""

    no_accents = unicodedata.normalize("NFD", text)
    no_accents = "".join(
        char for char in no_accents if unicodedata.category(char) != "Mn"
    )

    return no_accents


def whitespace(text):
    """Remove espaços em branco"""

    return " ".join(text.split())


def normalize(text):
    """Normaliza o texto para melhor tratamento"""

    normalized = text_lower(text)
    normalized = remove_accents(normalized)
    normalized = whitespace(normalized)

    return normalized

