import pandas as pd


class RC1Reader:

    def __init__(self, filename):
        self.filename = filename
        self.experiment = None
        self.data = None

    def read_excel(self):

        self.experiment = pd.read_excel(
            self.filename,
            sheet_name="Experiment"
        )

        self.data = pd.read_excel(
            self.filename,
            sheet_name="RC1_Data"
        )

        return self.experiment, self.data

    def validate(self):

        required_columns = [
            "Time(min)",
            "Reactor_Temperature(C)",
            "Jacket_Temperature(C)",
            "HeatFlow(W)",
            "Pressure(bar)",
            "FeedRate(g/min)"
        ]

        for column in required_columns:

            if column not in self.data.columns:
                raise Exception(f"Missing column: {column}")

        print("RC1 Excel Validation Successful")

    def get_parameters(self):

        parameters = dict(
            zip(
                self.experiment["Parameter"],
                self.experiment["Value"]
            )
        )

        return parameters