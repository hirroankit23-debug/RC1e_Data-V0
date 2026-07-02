import os
print("Using plots.py from:", os.path.abspath(__file__))

import plotly.express as px


class PlotGenerator:

    def __init__(self, data):
        self.data = data

    def heat_flow_plot(self):

        fig = px.line(
            self.data,
            x="Time(min)",
            y="HeatFlow(W)",
            title="Heat Flow vs Time",
            markers=True
        )

        fig.update_layout(
            xaxis_title="Time (min)",
            yaxis_title="Heat Flow (W)"
        )

        return fig


    def conversion_plot(self):

        fig = px.line(
            self.data,
            x="Time(min)",
            y="Conversion",
            title="Conversion vs Time",
            markers=True
        )

        fig.update_layout(
            xaxis_title="Time (min)",
            yaxis_title="Conversion"
        )

        return fig


    def concentration_plot(self):

        fig = px.line(
            self.data,
            x="Time(min)",
            y=["CA (mol/L)", "CB (mol/L)"],
            title="Reactant Concentration vs Time",
            markers=True
        )

        fig.update_layout(
            xaxis_title="Time (min)",
            yaxis_title="Concentration (mol/L)"
        )

        return fig


    def rate_plot(self):

        fig = px.line(
            self.data,
            x="Time(min)",
            y="Rate (mol/L/min)",
            title="Reaction Rate vs Time",
            markers=True
        )

        fig.update_layout(
            xaxis_title="Time (min)",
            yaxis_title="Reaction Rate (mol/L/min)"
        )

        return fig