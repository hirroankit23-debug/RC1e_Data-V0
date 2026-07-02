import numpy as np
from sklearn.linear_model import LinearRegression


class KineticsCalculator:

    def __init__(self, data):

        self.data = data

    def estimate(self):

        df = self.data.copy()

        df = df[df["Rate (mol/L/min)"] > 0]

        X = np.log(
            df["CA (mol/L)"]
        ).values.reshape(-1,1)

        y = np.log(
            df["Rate (mol/L/min)"]
        ).values

        model = LinearRegression()

        model.fit(X,y)

        reaction_order = model.coef_[0]

        k = np.exp(model.intercept_)

        print("\n==============================")

        print("Estimated Kinetics")

        print("==============================")

        print(f"Reaction Order = {reaction_order:.4f}")

        print(f"Rate Constant = {k:.6f}")

        return reaction_order,k