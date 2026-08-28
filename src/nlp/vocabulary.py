

# core
from core.config import VOCAB_JSON

# utils
from utils.functions import write_json, read_json


class Vocabulary:
    def __init__(self, load=False):
        self.token_to_id = {}
        self.id_to_token = {}

        self.token_count = 0 # contagem de tokens do vocabulary

        self.updated = False # status de atualização do vocabulary

        # Se a instancia tiver load=True ele já carrega o vocabulary.json
        if load:
            self.load_vocab()

    def add_token_id(self, token):
        """Verifica se o token possuí ID, se não, adiciona"""

        if not token in self.token_to_id:
            token_id = len(self.token_to_id)

            # adiciona o token/id na lista
            self.token_to_id[token] = token_id
            self.id_to_token[token_id] = token

            self.updated = True

    def add_tokens(self, tokens):
        """Separa token por token para adicionar ao vocabulary"""

        for token in tokens:
            self.add_token_id(token)

        # verifica se tokens novos foram adicionados e atualiza o vocabulary
        if self.updated:
            self.save_vocab()

    def save_vocab(self):
        """Salva os dados no vocabulary.json"""

        write_json(VOCAB_JSON, self.token_to_id)

    def load_vocab(self):
        """Carrega os dados do vocabulary.json"""

        data = read_json(VOCAB_JSON)

        for token, id in data.items():
            self.token_to_id[token] = token
            self.id_to_token[id] = id

        self.token_count = len(self.token_to_id)



# import json

# # core
# from core.config import VOCAB_JSON

# # utils
# from utils.functions import read_json, write_json


# class Vocabulary:
#     def __init__(self):
#         self.token_to_id = {}
#         self.id_to_token = {}

#         # Logo que inicia já recupera o vocabulário do json
#         self.load_vocabulary()

#         # Identificar novos tokens e salvar .json
#         self.update = False


#     def add_token_id(self, token):
#         """Adicionar id ao token"""

#         if not token in self.token_to_id:
#             token_id = len(self.token_to_id)

#             self.token_to_id[token] = token_id
#             self.id_to_token[token_id] = token

#             self.update = True

#         return self.token_to_id[token]


#     def add_tokens(self, tokens):
#         """Adiciona id a vários tokens"""

#         for token in tokens:
#             self.add_token_id(token)

#         # Se novos tokens forem adicionados o vocabulary.json é salvo e recarregado
#         if self.update:
#             self.save_vocabulary()

#             print("Atualizando o vocabulary.json")
#             self.load_vocabulary()

#             self.update = False # Depois de atualizar volta o valor de update para Falso


#     def save_vocabulary(self):
#         """Salva todos os dados do vocabulário no json"""

#         print("\nSalvando o vocabulário")

#         write_json(VOCAB_JSON, self.token_to_id)


#     def load_vocabulary(self):
#         """Carrega todo o vocabulário do arquivo .json"""

#         data = read_json(VOCAB_JSON)

#         for token in data.items():
#             # cada token presente no 'data' do json já é salvo em token_to_id/id_to_token

#             self.token_to_id[token[0]] = token[1]
#             self.id_to_token[token[1]] = token[0]

#         # contagem de tokens
#         self.token_count = len(self.token_to_id)

