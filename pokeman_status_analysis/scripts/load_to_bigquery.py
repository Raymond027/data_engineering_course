from google.cloud import bigquery
import pandas as pd
from config.settings import PROJECT_ID, DATASET_ID

TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.raw_pokemon"


def load_csv_to_bigquery(file_path: str) -> None:
    client = bigquery.Client(project=PROJECT_ID)

    df = pd.read_csv(file_path)

    df = df.rename(columns={
        "#": "id",
        "Name": "name",
        "Type 1": "type_1",
        "Type 2": "type_2",
        "Sp. Atk": "sp_atk",
        "Sp. Def": "sp_def"
    })

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    job = client.load_table_from_dataframe(
        df,
        TABLE_ID,
        job_config=job_config,
    )

    job.result()

    print(f"Successfully loaded data into {TABLE_ID}")


if __name__ == "__main__":
    load_csv_to_bigquery("data/pokemon.csv")