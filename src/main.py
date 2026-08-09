# core
from core import settings

# utils
from utils.console import entry


class PythonIA:
    def __init__(self):
        self.running = True

    def user_entry(self):
        while self.running:
            args = entry()
            print(args)


if __name__ == '__main__':
    try:
        app = PythonIA()
        app.user_entry()

    except KeyboardInterrupt:
        print("finalizando...")
