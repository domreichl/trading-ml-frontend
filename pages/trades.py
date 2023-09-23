import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file

add_page_title()

trades = read_csv_file("trades")
trading_performance = read_json_file("trading_performance")
model_performance = read_json_file("model_performance")

st.dataframe(trades)

st.subheader(f"Totals")
c1, c2, c3 = st.columns(4)
c1.metric("Volume", trading_performance["TOTAL_VOLUME"])
c2.metric("Gross Profit", "{:.2}€".format(trading_performance["TOTAL_GROSS_PROFIT"]))
c3.metric("Fees", round(trading_performance["TOTAL_FEES"], 2))

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
# print(trading_performance)
# write_json_results(trading_performance, "trading_performance")

# model_performance = {}
# for model in df["MODEL"].unique():
#     df_model = df[df["MODEL"] == model]
#     buy_price = df_model["BUY_PRICE"].values
#     sell_price_gt = df_model["SELL_PRICE"].values
#     sell_price_pr = df_model["PREDICTED_PRICE"].values
#     win_gt = sell_price_gt > buy_price
#     win_pr = sell_price_pr > buy_price
#     precision, recall, f1_score, _ = precision_recall_fscore_support(
#         win_gt, win_pr, average="binary"
#     )
#     model_performance[model] = {
#         "RETURN_MAE": np.mean(df_model["RETURN_AE"]),
#         "PRICE_SMAPE": compute_SMAPE(sell_price_pr, sell_price_gt),
#         "ACCURACY": accuracy_score(win_gt, win_pr),
#         "PRECISION": precision,
#         "RECALL": recall,
#         "F1": f1_score,
#     }