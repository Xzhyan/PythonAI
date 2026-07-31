
# core
from core.config import BASE_DIR

# utils
from utils.console import entry

# parser
from parser.tokenizer import tokenize
from parser.normalizer import normalize
from parser.intent_detector import intent_detect


class Main:
    def __init__(self):
        self.running = True

    def get_entries(self):
        while self.running:
            try:
                text = entry()

                parsed = tokenize(text)

                parsed.tokens = normalize(parsed.tokens)

                intent = intent_detect(parsed.tokens)

                print(intent)


            except ValueError as e:
                print(e)

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.get_entries()

    except KeyboardInterrupt:
        print("\nfinalizando...")
