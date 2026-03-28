import pandas as pd


def extract() -> pd.DataFrame:
    df = pd.read_csv("data.csv")
    return df
