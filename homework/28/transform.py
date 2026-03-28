import pandas as pd


def transform(dataframe: pd.DataFrame) -> None:
    dataframe["Double_Salary"] = dataframe["Salary"] * 2
