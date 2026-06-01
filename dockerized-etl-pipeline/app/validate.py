import great_expectations as gx

def validate_dataframe(df):

    context = gx.get_context()

    gx_df = gx.from_pandas(df)

    gx_df.expect_column_values_to_not_be_null(
        "temperature"
    )

    gx_df.expect_table_row_count_to_be_between(
        min_value=1,
        max_value=10000
    )

    return True