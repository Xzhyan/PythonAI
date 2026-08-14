# utils
from utils.console import entry


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        while self.running:            
            try:
                entries = entry()

            except ValueError as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.startup()

    except KeyboardInterrupt:
        print("\nfinalizando...")
