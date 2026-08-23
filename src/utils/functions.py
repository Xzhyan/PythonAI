import json


def read_json(path):
    """Lê qualquer json passado no path e retorna os dados"""

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not data:
                raise ValueError("Nenhum dado encontrado no .json")

            return data

    except FileNotFoundError as e:
        print(str(e))

    except ValueError as e:
        print(str(e))
