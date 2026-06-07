import json
import yaml
import pandas as pd

from validation.validation_runner import (
    run_all_validations
)


def load_config():

    with open(
        "configs/validation_config.yaml"
    ) as file:
        return yaml.safe_load(file)


def main():

    config = load_config()

    df = pd.read_csv(
        "data/raw/customer_orders.csv"
    )

    report = run_all_validations(
        df,
        config
    )

    with open(
        config["report_path"],
        "w"
    ) as file:
        json.dump(
            report,
            file,
            indent=4
        )

    print(
        "Validation report generated."
    )


if __name__ == "__main__":
    main()