import subprocess


def clear():
    """Limpa a tela do command line"""

    subprocess.run('cls', shell=True)


def entry():
    """Recebe entras de texto do usuário"""

    entries = input(" PythonIA > ")

    if not entries:
        raise ValueError("Nenhuma entrada foi informada")

    return entries
