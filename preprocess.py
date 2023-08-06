import argparse
import pandas as pd

from app.const import DEFAULT_CSV_RAW_PATH

def preprocess(df: pd.DataFrame):
    # TODO: remove duplicates

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-crp", "--csv-raw-path", default=DEFAULT_CSV_RAW_PATH)
    args = parser.parse_args()

    df = pd.read_csv(args.csv_raw_path)
    preprocess(df)
