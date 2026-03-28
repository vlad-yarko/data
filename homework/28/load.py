import pandas as pd


def load(dataframe: pd.DataFrame) -> None:
    dataframe.to_parquet("updated_data.csv", engine="fastparquet")
