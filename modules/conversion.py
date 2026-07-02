import numpy as np


class ConversionCalculator:

    def __init__(self, data):
        self.data = data

    def calculate_cumulative_heat(self):

        time_seconds = self.data["Time(min)"] * 60

        heat_flow = self.data["HeatFlow(W)"]

        cumulative_heat = np.zeros(len(self.data))

        for i in range(1, len(self.data)):

            dt = time_seconds.iloc[i] - time_seconds.iloc[i - 1]

            average_heat = (
                heat_flow.iloc[i] +
                heat_flow.iloc[i - 1]
            ) / 2

            cumulative_heat[i] = (
                cumulative_heat[i - 1] +
                average_heat * dt
            )

        self.data["Cumulative_Heat(J)"] = cumulative_heat

        return self.data

    def calculate_conversion(self, parameters):

        delta_h = abs(float(parameters["Heat of Reaction"])) * 1000

        initial_moles = min(
            float(parameters["Initial Moles A"]),
            float(parameters["Initial Moles B"])
        )

        total_heat = delta_h * initial_moles

        self.data["Conversion"] = (
            self.data["Cumulative_Heat(J)"] / total_heat
        )

        self.data["Conversion"] = self.data["Conversion"].clip(upper=1)

        return self.data    