import pandas as pd

REQUIRED_COLUMNS = [
    "#",
    "Name",
    "Type 1",
    "HP",
    "Attack",
    "Defense",
    "Generation",
    "Legendary"
]


def validate_dataset(file_path: str) -> None:
    df = pd.read_csv(file_path)

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("Dataset validation successful")


if __name__ == "__main__":
    validate_dataset("data/pokemon.csv")