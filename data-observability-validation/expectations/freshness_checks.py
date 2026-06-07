import pandas as pd


def check_duplicates(df):

    duplicates = df[df.duplicated()]

    return {
        "duplicate_count": len(duplicates),
        "duplicate_rows": duplicates.to_dict(
            orient="records"
        )
    }