
# core
from core.config import BASE_DIR

# utils
from utils.console import entry



class Main:
    def __init__(self):
        self.running = True

    def dispatch(self):
        while self.running:
            try:
                args = entry()

            except ValueError as e:
                print(e)

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.dispatch()

    except KeyboardInterrupt:
        print("\nfinalizando...")
