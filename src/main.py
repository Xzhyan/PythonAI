
# utils
from utils.console import entry, clear


# nlp
from nlp import normalize
from nlp import tokenize
from nlp import Vocabulary


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        while self.running:
            try:
                entries = entry()

                if 'clear' in entries:
                    clear()

                normalized = normalize(entries)
                tokens = tokenize(normalized)

                vocab = Vocabulary()

                vocab.read_vocabulary()

            except ValueError as e:
                print(str(e))

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.startup()

    except KeyboardInterrupt:
        print("\nFinalizando...")
