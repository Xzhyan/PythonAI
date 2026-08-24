import numpy as np


class Embedding:
    def __init__(self, vocab_size, embedding_dim):
        """Configurações inicias de tamanho e dimensão do embedding"""

        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim

        self.weights = np.random.randn(
            self.vocab_size,
            self.embedding_dim
        )

    def get_vector(self, token_id):
        """Pega o vector do token_id"""

        return self.weights[token_id]

