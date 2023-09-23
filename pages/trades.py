import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file

add_page_title()

trades = read_csv_file("trades")
tp = read_json_file("trading_performance")
mp = read_json_file("model_performance")

st.subheader(f"Totals")
c1, c2, c3 = st.columns(3)
c1.metric("Volume", "{:.2}€".format(tp["TOTAL_VOLUME"]))
c2.metric("Gross Profit", "{:.2}€".format(tp["GROSS_PROFIT"]))
c3.metric("Fees", "{:.2}€".format(tp["FEES"]))

st.subheader(f"Trades")
if st.checkbox("Show dataframe"):
    st.dataframe(trades)

# trading_performance = {
#     "N_TRADES": len(df),
#     "N_TRADES_WIN": len(trades_win),
#     "N_TRADES_LOSS": len(trades_loss),
#     "WIN_RATE": len(trades_win) / len(df),
#     "TOTAL_VOLUME": (df["BUY_PRICE"] * df["SHARES"]).sum(),
#     "TOTAL_GROSS_PROFIT": df["GROSS_PROFIT"].sum(),
#     "TOTAL_NET_PROFIT": df["NET_PROFIT"].sum(),
#     "TOTAL_FEES": df["FEES"].sum(),
#     "AVG_VOLUME": (df["BUY_PRICE"] * df["SHARES"]).mean(),
#     "AVG_PROFIT": df["NET_PROFIT"].mean(),
#     "STD_PROFIT": df["NET_PROFIT"].std(),
#     "MAX_WIN": df["NET_PROFIT"].max(),
#     "MAX_LOSS": df["NET_PROFIT"].min(),
#     "AVG_WIN": trades_win["NET_PROFIT"].mean(),
#     "AVG_LOSS": trades_loss["NET_PROFIT"].mean(),
#     "SQN": df["REWARD"].mean() / df["REWARD"].std() * np.sqrt(len(df)),
# }
# for model in df["MODEL"].unique():
#     model_performance[model] = {
#         "RETURN_MAE": np.mean(df_model["RETURN_AE"]),
#         "PRICE_SMAPE": compute_SMAPE(sell_price_pr, sell_price_gt),
#         "ACCURACY": accuracy_score(win_gt, win_pr),
#         "PRECISION": precision,
#         "RECALL": recall,
#         "F1": f1_score,
#     }