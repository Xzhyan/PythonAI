import re


def tokenize(text):
    """Separa cada palavra, número, ponto em um token"""

    return re.findall(r"\w+|[^\w\s]", text)
