
# utils
from utils.console import entry, clear


# nlp
from nlp import normalize, tokenize, Vocabulary, Embedding


# cria a instância do Vocabulary
vocab = Vocabulary()

# instancia do Embedding
embedding = Embedding(12, 3)


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        while self.running:
            try:
                entries = entry()

                if 'clear' in entries:
                    clear()

                # normaliza o texto
                normalized = normalize(entries)

                # transforma o texto normalizado em tokens
                tokens = tokenize(normalized)

                # gera o vocabulário dos tokens
                vocab.add_tokens(tokens)

                # testando o embedding
                id_list = []

                for token in tokens:
                    id = vocab.token_to_id[token]
                    id_list.append(id)

                vector = embedding.get_vector(id_list)

                print(vector)


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
