import os
import numpy as np
import pandas as pd
import streamlit as st
from st_pages import add_page_title
from pathlib import Path


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

performance = pd.read_csv(os.path.join("data", "performance_regression.csv"))
performance = performance[
    performance["Target"].isin(["Price", "Log Return"])
    & performance["Metric"].isin(metrics_available)
]

if metric_selected == "all":
    st.dataframe(performance)
else:
    st.dataframe(performance[performance["Metric"] == metric_selected])
