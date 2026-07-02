class ConcentrationCalculator:

    def __init__(self, data, parameters):

        self.data = data
        self.parameters = parameters

    def calculate(self):

        initial_volume = float(
            self.parameters["Initial Volume"]
        )

        initial_moles_A = float(
            self.parameters["Initial Moles A"]
        )

        initial_moles_B = float(
            self.parameters["Initial Moles B"]
        )

        self.data["Moles_A"] = (
            initial_moles_A *
            (1 - self.data["Conversion"])
        )

        self.data["Moles_B"] = (
            initial_moles_B *
            (1 - self.data["Conversion"])
        )

        self.data["CA (mol/L)"] = (
            self.data["Moles_A"] /
            initial_volume
        )

        self.data["CB (mol/L)"] = (
            self.data["Moles_B"] /
            initial_volume
        )

        return self.data