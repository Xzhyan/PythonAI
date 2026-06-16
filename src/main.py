# core
from core import settings

# utils
from utils.console import get_entry, clear

# machine learn
from machine_learn.salary_predictor import SalaryPredictor



class PythonAI():
    def __init__(self):
        self.running = True
        
        self.predictor = SalaryPredictor()

    def startup(self):
        self.predictor.train()

        self.dispatch()

    def dispatch(self):
        while self.running:
            try:
                args = get_entry()

                if args[0] == 'clear':
                    clear()

                else:
                    age = int(args[0])
                    salary = self.predictor.predict(age)
                    print(f"salario previsto: {salary:.2f}")

            except Exception as e:
                print(str(e))



if __name__ == '__main__':
    try:
        app = PythonAI()
        app.startup()

    except KeyboardInterrupt:
        print('Finalizando...')