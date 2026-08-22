

class Vocabulary:
    def __init__(self):
        self.token_to_id = {}
        self.id_to_token = {}

    def add_id_token(self, token):
        """Adicionar id ao token"""

        if not token in self.token_to_id:
            token_id = len(self.token_to_id)

            self.token_to_id[token] = token_id
            self.id_to_token[token_id] = token

        return self.token_to_id[token]

    def add_tokens(self, tokens):
        """Adiciona id a vários tokens"""

        for token in tokens:
            self.add_id_token(token)

