import pandas as pd
import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file


add_page_title()
st.sidebar.markdown(
    "Warning: The measures you see here are of dummy models used solely for showcasing purposes."
)

st.subheader("Test Results")
metrics_available = ["all", "SMAPE", "RMSE", "MASE"]
metrics_captions = [
    "show all metrics",
    "Symmetric Mean Absolute Percentage Error",
    # "SMAPE for the final prediction",
    "Mean Absolute Error",
    "Mean Absolute Scaled Error",
]
metric_selected = st.radio(
    "Select metric",
    options=metrics_available,
    # captions=metrics_captions,
    horizontal=True,
)

rp = read_csv_file("performance_regression")
rp = rp[
    rp["Target"].isin(["Price", "Log Return"]) & rp["Metric"].isin(metrics_available)
]

if metric_selected == "all":
    st.dataframe(rp)
else:
    st.dataframe(rp[rp["Metric"] == metric_selected])

st.subheader("Trading Performance")
mp = pd.DataFrame.from_dict(read_json_file("model_performance"), orient="index")
mp.index.rename("Model", inplace=True)
st.dataframe(mp)
