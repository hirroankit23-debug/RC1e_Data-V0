import streamlit as st

from modules.excel_reader import RC1Reader
from modules.conversion import ConversionCalculator
from modules.concentration import ConcentrationCalculator
from modules.rate_calculator import RateCalculator
from modules.kinetics import KineticsCalculator
import modules.plots
print("Loaded plots.py from:", modules.plots.__file__)

PlotGenerator = modules.plots.PlotGenerator

from modules.plots import PlotGenerator
from modules.reactor import ReactorCalculator

st.set_page_config(
    page_title="RC1e Kinetics Software",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 RC1e Kinetics & Reactor Design Software")

uploaded_file = st.file_uploader(
    "Upload RC1e Excel File",
    type=["xlsx"]
)

if uploaded_file:

    with open("temp.xlsx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    reader = RC1Reader("temp.xlsx")

    experiment, rc1_data = reader.read_excel()

    reader.validate()

    parameters = reader.get_parameters()

    conversion = ConversionCalculator(rc1_data)

    rc1_data = conversion.calculate_cumulative_heat()

    rc1_data = conversion.calculate_conversion(parameters)

    concentration = ConcentrationCalculator(
        rc1_data,
        parameters
    )

    rc1_data = concentration.calculate()

    rate = RateCalculator(rc1_data)

    rc1_data = rate.calculate()

    kinetics = KineticsCalculator(rc1_data)

    reaction_order, k = kinetics.estimate()

    reactor = ReactorCalculator(
    k,
    reaction_order
)

    plots = PlotGenerator(rc1_data)

    st.success("Analysis Completed Successfully")

    st.header("Experiment Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Reaction",
        parameters["Reaction Name"]
    )

    c2.metric(
        "Initial Volume",
        parameters["Initial Volume"]
    )

    c3.metric(
        "Heat of Reaction",
        parameters["Heat of Reaction"]
    )

    st.header("Kinetic Parameters")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Reaction Order",
        f"{reaction_order:.3f}"
    )

    c2.metric(
        "Rate Constant",
        f"{k:.5f}"
    )

    c3.metric(
        "Maximum Conversion",
        f"{rc1_data['Conversion'].max()*100:.2f}%"
    )

    st.header("Processed Data")

    st.dataframe(rc1_data)


    st.header("Conversion")

    st.plotly_chart(
        plots.conversion_plot(),
        use_container_width=True
    )

    st.header("Concentration")

    st.plotly_chart(
        plots.concentration_plot(),
        use_container_width=True
    )

    st.header("Reaction Rate")

    st.plotly_chart(
        plots.rate_plot(),
        use_container_width=True
    )

    st.header("🏭 Reactor Design")

residence_time = st.number_input(
    "Residence Time (minutes)",
    min_value=0.1,
    value=30.0,
    step=1.0
)

if st.button("Predict Conversion"):

    predicted = reactor.predict_conversion(residence_time)

    st.success(
        f"Predicted Conversion = {predicted*100:.2f}%"
    )