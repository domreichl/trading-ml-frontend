import streamlit as st
from st_pages import add_page_title

from utils.file_handling import read_csv_file, read_json_file


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

performance = read_csv_file("performance_regression")
performance = performance[
    performance["Target"].isin(["Price", "Log Return"])
    & performance["Metric"].isin(metrics_available)
]

if metric_selected == "all":
    st.dataframe(performance)
else:
    st.dataframe(performance[performance["Metric"] == metric_selected])


mp = read_json_file("model_performance")
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
