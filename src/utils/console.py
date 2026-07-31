

def entry():
    """Recebe entradas do usuário"""

    entries = input(" PythonAI > ")

    if not entries:
        raise ValueError("você precisa digitar algo")

    return entries.split()
