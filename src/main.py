
# utils
from utils.console import entry, clear


# nlp
from nlp import normalize
from nlp import tokenize
from nlp import Vocabulary


# cria a instância do Vocabulary
vocab = Vocabulary()


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

                vocab.add_tokens(tokens)

            except ValueError as e:
                print(str(e))

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.startup()

    except KeyboardInterrupt:
        # salva o vocabulário no json
        vocab.save_vocabulary("vocabulary.json")

        print("\nFinalizando...")
