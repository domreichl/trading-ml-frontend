import pandas as pd
import streamlit as st
import plotly.express as px
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file

add_page_title()

trades = read_csv_file("trades")
trades.drop(columns=['ID'], inplace=True)
tp = read_json_file("trading_performance")

st.subheader("Statistics")

st.plotly_chart(
    px.pie(
        names=["Winning Trades", "Losing Trades"],
        values=[tp["N_TRADES_WIN"], tp["N_TRADES_LOSS"]],
        title=f"Total Trades: {tp['N_TRADES']}"
    )
)

a1, a2, a3 = st.columns(3)
a1.metric("Trades", f"{round(tp['N_TRADES'])}")
a2.metric("Volume", f"{round(tp['TOTAL_VOLUME'])}€")
a3.metric("Gross Profit", f"{round(tp['TOTAL_GROSS_PROFIT'])}€")

b1, b2, b3 = st.columns(3)
b1.metric("Winning Trades", f"{round(tp['N_TRADES_WIN'])}")
b2.metric("Highest Win", f"{round(tp['MAX_WIN'])}€")
b3.metric("Fees", f"{round(tp['TOTAL_FEES'])}€")

c1, c2, c3 = st.columns(3)
c1.metric("Losing Trades", f"{round(tp['N_TRADES_LOSS'])}")
c2.metric("Highest Loss", f"{round(tp['MAX_LOSS'])}€")
c3.metric("Net Profit", f"{round(tp['TOTAL_NET_PROFIT'])}€")

d1, d2, d3 = st.columns(3)
d1.metric("Win Rate", f"{round(tp['WIN_RATE']*100)}%")
d2.metric("SQN", f"{round(tp['SQN'])}")
d3.metric("Average Net Profit", f"{round(tp['AVG_PROFIT'])}€")

st.subheader(f"Trades")
st.dataframe(trades)
