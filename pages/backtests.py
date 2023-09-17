import os
import numpy as np
import pandas as pd
import streamlit as st
from st_pages import add_page_title
from pathlib import Path


add_page_title()

yearly_returns = pd.read_csv(os.path.join("data", "mean_log_returns.csv"))
yearly_returns["Average Return"] = np.exp(yearly_returns["Average Log Return"])

st.subheader(f"Mean Yearly Returns for 16 ATX Stocks")
if st.toggle("Log Scale", value=True):
    log = " Log "
else:
    log = " "
st.bar_chart(yearly_returns, x="Year", y=f"Average{log}Return")

st.subheader(f"Naive Buy-and-Hold Investing")
st.markdown("to be added")  # with sliders for parmeters

st.subheader(f"Naive Weekly Trading")
st.markdown("to be added")  # with sliders for parmeters

st.subheader(f"Strategy C")
st.markdown("to be added")
