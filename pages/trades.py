import pandas as pd
import streamlit as st
import plotly.express as px
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file

add_page_title()

trades = read_csv_file("trades")
trades.drop(columns=["ID"], inplace=True)
tp = read_json_file("trading_performance")

st.subheader("Statistics")

a1, a2, a3 = st.columns(3)
a1.metric("Trades", f"{round(tp['N_TRADES'])}")
a2.metric("Volume", f"{round(tp['TOTAL_VOLUME'])}€")
a3.metric("Gross Profit", f"{round(tp['TOTAL_GROSS_PROFIT'])}€")

b1, b2, b3 = st.columns(3)
b1.metric("Highest Win", f"{round(tp['MAX_WIN'])}€")
b2.metric("Highest Loss", f"{round(tp['MAX_LOSS'])}€")
b3.metric("Net Profit", f"{round(tp['TOTAL_NET_PROFIT'])}€")

c1, c2, c3 = st.columns(3)
c1.metric("SQN", f"{round(tp['SQN'])}")
c2.metric("Fees", f"{round(tp['TOTAL_FEES'])}€")
c3.metric("Average Net Profit", f"{round(tp['AVG_PROFIT'])}€")

chart_colors = {
    "Losing Trades": "darkred",
    "Winning Trades": "darkgreen",
}
st.plotly_chart(
    px.pie(
        color=list(chart_colors.keys()),
        values=[tp["N_TRADES_LOSS"], tp["N_TRADES_WIN"]],
        color_discrete_map=chart_colors,
    )
)

st.subheader(f"Trades")
st.dataframe(trades)
