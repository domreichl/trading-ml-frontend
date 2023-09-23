import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file


add_page_title()
st.sidebar.markdown(
    "Warning: The measures you see here are of dummy models used solely for showcasing purposes."
)

metrics_available = ["all", "SMAPE", "SMAPE_last", "MAE", "MASE"]
metrics_captions = [
    "show all metrics",
    "Symmetric Mean Absolute Percentage Error",
    "SMAPE for the final prediction",
    "Mean Absolute Error",
    "Mean Absolute Scaled Error",
]
metric_selected = st.radio(
    "Select performance metric",
    options=metrics_available,
    captions=metrics_captions,
)

performance = read_csv_file("performance_regression")
performance = performance[
    performance["Target"].isin(["Price", "Log Return"])
    & performance["Metric"].isin(metrics_available)
]

if metric_selected == "all":
    st.dataframe(performance)
else:
    st.dataframe(performance[performance["Metric"] == metric_selected])
