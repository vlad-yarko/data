import pandas as pd

from extract import extract
from transform import transform
from load import load


def main() -> pd.DataFrame:
    df = extract()
    transform(df)
    load(df)
    return df


if __name__ == '__main__':
    res = main()
    print(res)
