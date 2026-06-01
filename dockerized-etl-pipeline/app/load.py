import os

def save_csv(df):

    os.makedirs("data/processed", exist_ok=True)

    output_file = "data/processed/weather.csv"

    df.to_csv(output_file, index=False)

    return output_file