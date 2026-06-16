from sklearn.linear_model import LinearRegression


class SalaryPredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self):
        ages = [[20], [25], [30], [35], [40]]

        salaries = [2000, 3000, 4000, 5000, 6000]

        self.model.fit(ages, salaries)

    def predict(self, age):
        return self.model.predict([[age]])[0]


