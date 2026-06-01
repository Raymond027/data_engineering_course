from pathlib import Path


def load_data(df):

    output_dir = Path("data/processed")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_dir / "crypto_prices.csv",
        index=False
    )