import subprocess, platform


def get_entry():
    """Recebe entradas do usuário"""

    entry = input(" > ")
    
    if not entry:
        raise ValueError('Nenhuma entrada foi informada')
    
    return entry.split()


def clear():
    """Limpa a tela da ferramenta"""

    cmd = 'clear' if platform.system() == 'Linux' else 'cls'
    subprocess.run(cmd)


