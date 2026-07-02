import numpy as np


class ReactorCalculator:

    def __init__(self, k, order):

        self.k = k
        self.order = order

    def predict_conversion(self, residence_time):

        t = residence_time

        # First-order reaction
        if abs(self.order - 1) < 0.2:

            X = 1 - np.exp(-self.k * t)

        # Zero-order reaction
        elif abs(self.order) < 0.2:

            X = min(self.k * t, 0.999)

        # General nth-order approximation
        else:

            X = 1 - (1 + (self.order - 1) * self.k * t) ** (
                -1 / (self.order - 1)
            )

        X = max(0, min(X, 0.999))

        return X 