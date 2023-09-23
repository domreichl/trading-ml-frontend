import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file

add_page_title()

trades = read_csv_file("trades")
tp = read_json_file("trading_performance")
mp = read_json_file("model_performance")

st.subheader("Statistics")
a1, a2, a3 = st.columns(3)
a1.metric("Trades", f"{round(tp['N_TRADES'])}")
a2.metric("Volume", f"{round(tp['TOTAL_VOLUME'])}€")
a3.metric("Gross Profit", f"{round(tp['TOTAL_GROSS_PROFIT'])}€")
b1, b2, b3 = st.columns(3)
b1.metric("Winning Trades", f"{round(tp['N_TRADES_WIN'])}")
b2.metric("Losing Trades", f"{round(tp['N_TRADES_LOSS'])}")
b3.metric("Fees", f"{round(tp['TOTAL_FEES'])}€")
c1, c2, c3 = st.columns(3)
c1.metric("Win Rate", f"{round(tp['WIN_RATE']*100)}%")
c2.metric("SQN", f"{round(tp['SQN'])}")
c3.metric("Net Profit", f"{round(tp['TOTAL_NET_PROFIT'])}€")
d1, d2, d3 = st.columns(3)
d1.metric("Highest Win", f"{round(tp['MAX_WIN'])}€")
d2.metric("Highest Loss", f"{round(tp['MAX_LOSS'])}€")
d3.metric("Average Net Profit", f"{round(tp['AVG_PROFIT'])}€")

st.subheader(f"Trades")
if st.checkbox("Show dataframe"):
    st.dataframe(trades)

# TODO: model-specific trading performance
# for model in df["MODEL"].unique():
#     model_performance[model] = {
#         "RETURN_MAE": np.mean(df_model["RETURN_AE"]),
#         "PRICE_SMAPE": compute_SMAPE(sell_price_pr, sell_price_gt),
#         "ACCURACY": accuracy_score(win_gt, win_pr),
#         "PRECISION": precision,
#         "RECALL": recall,
#         "F1": f1_score,
#     }