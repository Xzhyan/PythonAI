import json

# core
from core.config import VOCAB_JSON

# utils
from utils.functions import read_json, write_json

# arquivo json do vocabulario



class Vocabulary:
    def __init__(self):
        self.token_to_id = {}
        self.id_to_token = {}

        # Logo que inicia já recupera o vocabulário do json
        self.load_vocabulary(VOCAB_JSON)


    def add_token_id(self, token):
        """Adicionar id ao token"""

        if not token in self.token_to_id:
            token_id = len(self.token_to_id)

            self.token_to_id[token] = token_id
            self.id_to_token[token_id] = token

        return self.token_to_id[token]


    def add_tokens(self, tokens):
        """Adiciona id a vários tokens"""

        for token in tokens:
            self.add_token_id(token)


    def save_vocabulary(self):
        """Salva todos os dados do vocabulário no json"""

        print("\nSalvando o vocabulário antes de finalizar.")

        write_json(VOCAB_JSON, self.token_to_id)


    def load_vocabulary(self, json_file):
        """Carrega todo o vocabulário do arquivo .json"""

        data = read_json(VOCAB_JSON)

        for token in data.items():
            # cada token presente no 'data' do json já é salvo em token_to_id/id_to_token

            self.token_to_id[token[0]] = token[1]
            self.id_to_token[token[1]] = token[0]

