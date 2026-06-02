import great_expectations as gx

context = gx.get_context()

validator = context.sources.pandas_default.read_dataframe(
    dataframe=df
)

validator.expect_column_values_to_not_be_null(
    "current_price"
)

validator.expect_column_values_to_be_between(
    "current_price",
    min_value=0
)

validator.save_expectation_suite()