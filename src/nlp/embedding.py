




# import numpy as np


# # core
# from core.config import EMBEDDING_FILE


# class Embedding:
#     def __init__(self, vocab_size, embedding_dim):
#         """Configurações inicias de tamanho e dimensão do embedding"""

#         self.vocab_size = vocab_size
#         self.embedding_dim = embedding_dim

#         self.weights = np.random.randn(
#             self.vocab_size,
#             self.embedding_dim
#         )


#     def save_matriz(self):
#         try:
#             np.save(EMBEDDING_FILE, self.weights)

#         except Exception as e:
#             print(str(e))


#     def load_matriz(self):
#         try:
#             self.weights = np.load(EMBEDDING_FILE)

#         except Exception as e:
#             print(str(e))


#     def get_vector(self, token_id):
#         """Pega o vector do token_id"""

#         return self.weights[token_id]

