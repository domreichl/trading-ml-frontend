import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_json_file

add_page_title()

trading_performance = read_json_file("trading_performance")
model_performance = read_json_file("model_performance")

a1, a2, a3 = st.columns(3)
a1.metric("Total Gross Profit", trading_performance["TOTAL_GROSS_PROFIT"])
a2.metric("Total Net Profit", trading_performance["TOTAL_NET_PROFIT"])
a3.metric("Total Fees", trading_performance["TOTAL_FEES"])
