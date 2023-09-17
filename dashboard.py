import os, json
import numpy as np
import pandas as pd
import datetime as dt
import streamlit as st
import plotly.express as pe
import plotly.graph_objects as go
from st_pages import show_pages_from_config, add_page_title
from pathlib import Path


show_pages_from_config()
add_page_title()
st.sidebar.markdown(
    "Warning: The predictions you see here are generated by dummy models used solely for showcasing purposes."
)

model_selected = st.radio(
    "Choose prediction model",
    options=["LSTM", "LightGBM", "ARIMA"],
    captions=["LSTM Regressor", "to be added", "to be added"],
    horizontal=True,
)
# TODO: filter results by selected model


def set_date_index(df: pd.DataFrame, future=False) -> pd.DataFrame:
    # TODO: get index from predictions file and remove this function
    today = dt.datetime.today()
    if future:
        df.index = [(today + dt.timedelta(days=i)).date() for i in range(len(df))]
    else:
        df.index = [
            (today - dt.timedelta(days=i)).date() for i in range(len(df), 0, -1)
        ]
    return df


def get_naive_forecast(df):
    for col in df.columns:
        df[col] = np.broadcast_to(df[col].iloc[-1], np.array(df[col].shape))
    df = set_date_index(df, future=True)
    return df


df_dict = {
    fn: set_date_index(
        pd.DataFrame(json.load(open(os.path.join("data", fn + ".json"))))
    )
    for fn in [
        "prices_actual",
        "prices_predicted",
        "returns_actual",
        "returns_predicted",
    ]
}
isins = list(df_dict["prices_actual"].keys())
isin_default = isins.index("AT0000922554")
isin_selected = st.selectbox("Select ISIN", isins, index=isin_default)
prices_gt = df_dict["prices_actual"][[isin_selected]]
prices_pr = df_dict["prices_predicted"][[isin_selected]]
returns_gt = df_dict["returns_actual"][[isin_selected]]
returns_pr = df_dict["returns_predicted"][[isin_selected]]
prices_naive = get_naive_forecast(prices_gt.copy())
returns_naive = get_naive_forecast(returns_gt.copy())


# TODO: replace the following with real data and predictions
def dummify(df):
    for col in df.columns:
        df[col] = np.random.normal(df[col].iloc[-1], df[col].std())
    df = set_date_index(df, future=True)
    return df


prices_pr = pd.concat([prices_pr, dummify(prices_pr.copy())])
returns_pr = pd.concat([returns_pr, dummify(returns_pr.copy())])

st.subheader(f"Closing Prices for {isin_selected}")
fig_prices = go.Figure()
fig_prices.add_trace(
    go.Scatter(
        x=prices_gt.index,
        y=prices_gt[isin_selected],
        name="actual",
        line=dict(color="navy", width=4),
    )
)
fig_prices.add_trace(
    go.Scatter(
        x=prices_pr.index,
        y=prices_pr[isin_selected],
        name="predicted",
        line=dict(color="blueviolet", width=4),
    )
)
fig_prices.add_trace(
    go.Scatter(
        x=prices_naive.index,
        y=prices_naive[isin_selected],
        name="naive",
        line=dict(color="navy", width=4, dash="dot"),
    )
)
fig_prices.update_layout(
    xaxis_title="Date",
    yaxis_title="Price [€]",
)
st.plotly_chart(fig_prices)

st.subheader(f"Daily Returns for {isin_selected}")
fig_returns = go.Figure()
fig_returns.add_trace(
    go.Scatter(
        x=returns_gt.index,
        y=returns_gt[isin_selected],
        name="actual",
        line=dict(color="navy", width=4),
    )
)
fig_returns.add_trace(
    go.Scatter(
        x=returns_pr.index,
        y=returns_pr[isin_selected],
        name="predicted",
        line=dict(color="blueviolet", width=4),
    )
)
fig_returns.add_trace(
    go.Scatter(
        x=returns_naive.index,
        y=returns_naive[isin_selected],
        name="naive",
        line=dict(color="navy", width=4, dash="dot"),
    )
)
fig_returns.update_layout(
    xaxis_title="Date",
    yaxis_title="Return",
)
st.plotly_chart(fig_returns)

st.markdown(f"Last updated: {prices_naive.index[0]}")
