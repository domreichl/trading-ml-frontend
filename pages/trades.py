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

a1, a2 = st.columns(2)
#a1.metric("Trades", f"{round(tp['N_TRADES'])}")
a1.metric("Volume", f"{round(tp['TOTAL_VOLUME'])}€")
a2.metric("Gross Profit", f"{round(tp['TOTAL_GROSS_PROFIT'])}€")

b1, b2, b3 = st.columns(3)

#b2.metric("Highest Loss", f"{round(tp['MAX_LOSS'])}€")
b1.metric("Net Profit", f"{round(tp['TOTAL_NET_PROFIT'])}€")
b3.metric("Average Net Profit per Trade", f"{round(tp['AVG_PROFIT'])}€")

c1, c2 = st.columns(2)
c1.metric("Highest Win | Loss", f"{round(tp['MAX_WIN'])}€" | {round(tp['MAX_LOSS'])}€)
c2.metric("SQN", f"{round(tp['SQN'])}")
#c2.metric("Fees", f"{round(tp['TOTAL_FEES'])}€")
#c3.metric("Average Net Profit", f"{round(tp['AVG_PROFIT'])}€")

st.subheader(f"Trades")
counts = pd.DataFrame(
    {
        "trades": [f"{tp['N_TRADES']} Trades"] * 2,
        "count": [
            f"{tp['N_TRADES_WIN']} Wins",
            f"{tp['N_TRADES_LOSS']} Losses",
        ],
        "percentage": [tp["WIN_RATE"] * 100, (1 - tp["WIN_RATE"]) * 100],
    }
)
st.plotly_chart(
    px.sunburst(
        counts,
        path=["trades", "count"],
        values="percentage",
        color="count",
        color_discrete_map={
            "(?)": "black",
            counts["count"][0]: "forestgreen",
            counts["count"][1]: "firebrick",
        },
    )
)
st.dataframe(trades)
