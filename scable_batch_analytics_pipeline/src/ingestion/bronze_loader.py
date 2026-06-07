from pyspark.sql.functions import current_timestamp


def load_bronze(spark, source_path):

    df = spark.read.csv(
        source_path,
        header=True,
        inferSchema=True
    )

    bronze_df = (
        df.withColumn(
            "ingestion_time",
            current_timestamp()
        )
    )

    return bronze_df