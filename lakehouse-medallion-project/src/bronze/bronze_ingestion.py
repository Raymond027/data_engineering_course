from pyspark.sql.functions import current_timestamp

def load_to_bronze(
    spark,
    source_file,
    target_path
):

    df = (
        spark.read
        .option("header", True)
        .csv(source_file)
    )

    bronze_df = (
        df.withColumn(
            "ingestion_timestamp",
            current_timestamp()
        )
    )

    (
        bronze_df.write
        .format("delta")
        .mode("overwrite")
        .save(target_path)
    )

    return bronze_df