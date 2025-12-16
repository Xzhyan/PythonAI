import csv

def run_read_csv(csv_path):
    # Abrir o CSV e carregar as linhas
    dates = []
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        read_csv = csv.reader(csv_file)
        for i in read_csv:
            dates.append(i)
    return dates

class MachineLearning():
    def __init__(self):
        # Método que chama os dados
        self.get_dates()

    def get_dates(self):
        csv_path = 'csv.csv'
        csv_dates = run_read_csv(csv_path)
        
        if not csv_dates:
            print('Erro ao ler CSV')
        else:
            # Se o CSV for lido corretamente
            print(f"Dados lidos: {csv_dates}")

            # Dividir cabeçalho (X) e dados (y)
            X, y = self.split_data(csv_dates)
            print(f"X (características): {X}")
            print(f"y (rótulo): {y}")

    def split_data(self, data):
        # Cabeçalho como X (características)
        X = [row[:-1] for row in data[1:]]  # Ignora a última coluna
        # Última coluna como y (rótulo)
        y = [row[-1] for row in data[1:]]  # Pega a última coluna
        return X, y

if __name__ == '__main__':
    try:
        MachineLearning()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
