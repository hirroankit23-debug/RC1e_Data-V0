import numpy as np


class RateCalculator:

    def __init__(self, data):

        self.data = data

    def calculate(self):

        time = self.data["Time(min)"].values

        CA = self.data["CA (mol/L)"].values

        rate = np.zeros(len(time))

        for i in range(1, len(time)):

            dt = time[i] - time[i - 1]

            dCA = CA[i] - CA[i - 1]

            rate[i] = -dCA / dt

        rate[0] = rate[1]

        self.data["Rate (mol/L/min)"] = rate

        return self.data
        