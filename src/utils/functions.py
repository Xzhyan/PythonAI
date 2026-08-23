import json


def write_json(path, data):
    """Escreve dados em um arquivo json"""

    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError as e:
        print(str(e))


def read_json(path):
    """Lê os dados de um arquivo json"""

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
