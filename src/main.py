

class PythonAI():
    def __init__(self):
        pass

    def startup(self):
        print('deu bom!')



if __name__ == '__main__':
    try:
        app = PythonAI()
        app.startup()

    except KeyboardInterrupt:
        print('Finalizando...')