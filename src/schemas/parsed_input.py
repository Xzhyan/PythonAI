from dataclasses import dataclass


@dataclass
class ParsedInput:
    original: str
    tokens: list[str]

