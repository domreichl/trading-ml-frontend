import os, json
import pandas as pd


def read_csv_file(filename: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join("data", filename + ".csv"))


def read_json_file(filename: str) -> dict:
    with open(os.path.join("data", filename + ".json"), "r") as file:
        content = json.load(file)
    return content
