
def entry():
    """Recebe as entradas do usuário"""

    entries = input(" PythonIA > ")

    if not entries:
        raise ValueError("você precisa digitar alguma coisa...")

    return entries
