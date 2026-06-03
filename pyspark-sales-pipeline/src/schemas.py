from pyspark.sql.types import *

sales_schema = StructType([
    StructField("sale_id", IntegerType()),
    StructField("product", StringType()),
    StructField("category", StringType()),
    StructField("region", StringType()),
    StructField("quantity", IntegerType()),
    StructField("price", DoubleType()),
    StructField("sale_date", StringType())
])