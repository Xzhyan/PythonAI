from .normalizer import normalize
from .tokenizer import tokenize


from .vocabulary import Vocabulary
# from .embedding import Embedding


class NLProcessing:
    def __init__(self):
        self.vocab = Vocabulary(load=True)

    def manage(self, entries):
        """Recebe as entradas e faz o tratamento"""

        normalized = normalize(entries)
        tokens = tokenize(normalized)

        print(self.vocab.id_to_token)



# class NLPControl:
#     def __init__(self):
#         self.vocab = Vocabulary()
#         self.embedding = Embedding(16, 3)


#     def load_embedding(self):
#         """Carrega o arquivo embedding.npy de matrizes"""

#         # self.embedding.load_matriz()

#         return self.embedding.weights

#     def save_embedding(self):
#         """Salva a matriz de todos os tokens do vocabulary"""

#         id_list = []

#         for id in self.vocab.id_to_token:
#             id_list.append(id)

#         self.embedding.get_vector(id_list)
#         self.embedding.save_matriz()

#     def control(self):
#         # self.save_embedding()

#         test = self.load_embedding()

#         print(test)


# def nlp_control(entries):
#     """Recebe a entrada do usuário e processa"""

#     normalized = normalize(entries)
#     tokens = tokenize(normalized)

#     # Trata os tokens no Vocabulary
#     vocab.add_tokens(tokens)

#     id_list = [] # lista de id dos tokens

#     # Para cada token ele obtem o IDs persistentes no vocabulary
#     for token in tokens:
#         id = vocab.token_to_id[token]
#         id_list.append(id)


#     # obtem o vector apartir dos IDs na lista
#     # vector = embedding.get_vector(id_list)

#     # Carrega os pesos dos embeddins salvos
#     # embedding.load_matriz()

#     # print('salvando a matriz')
#     # embedding.save_matriz()

#     # print(embedding.weights)

#     return tokens
