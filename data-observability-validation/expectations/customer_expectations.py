import pandas as pd
import great_expectations as gx


def run_expectations(df):

    ge_df = gx.from_pandas(df)

    results = []

    # Primary key validation
    results.append(
        ge_df.expect_column_values_to_be_unique(
            "order_id"
        )
    )

    # No nulls
    results.append(
        ge_df.expect_column_values_to_not_be_null(
            "customer_id"
        )
    )

    results.append(
        ge_df.expect_column_values_to_not_be_null(
            "order_amount"
        )
    )

    # Positive order amount
    results.append(
        ge_df.expect_column_values_to_be_between(
            "order_amount",
            min_value=1,
            max_value=100000
        )
    )

    # Date validation
    results.append(
        ge_df.expect_column_values_to_not_be_null(
            "created_at"
        )
    )

    return results