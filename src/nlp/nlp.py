from .normalizer import normalize
from .tokenizer import tokenize
from .vocabulary import Vocabulary
from .embedding import Embedding


# Intancia do Vocabulary
vocab = Vocabulary()

# Instancia do Embedding com peso e dimensão
embedding = Embedding(16, 3)


def nlp_control(entries):
    """Recebe a entrada do usuário e processa"""

    normalized = normalize(entries)
    tokens = tokenize(normalized)

    # Trata os tokens no Vocabulary
    vocab.add_tokens(tokens)

    id_list = [] # lista de id dos tokens

    # Oara cada token ele obtem o IDs persistentes no vocabulary
    for token in tokens:
        id = vocab.token_to_id[token]
        id_list.append(id)

    # obtem o vector apartir dos IDs na lista
    # vector = embedding.get_vector(id_list)

    # Carrega os pesos dos embeddins salvos
    embedding.load_matriz()

    print(embedding.weights)

    return tokens



