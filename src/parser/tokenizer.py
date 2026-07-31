from schemas.parsed_input import ParsedInput


def tokenize(text: str) -> list[str]:
    tokens = text.split()

    return ParsedInput(
        original=text,
        tokens=tokens
    )
