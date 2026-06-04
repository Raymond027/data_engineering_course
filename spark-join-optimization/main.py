from src.session import create_spark
from src.data_loader import load_data
from src.transformations import clean_data
from src.optimizations import (
    baseline_join,
    broadcast_join,
    repartition_before_join,
    coalesce_after_join
)
from src.analysis import analyze_plan

def main():
    spark = create_spark()

    # Step 1: Load Data
    customers, orders, products = load_data(spark)

    # Step 2: Clean
    customers, orders, products = clean_data(customers, orders, products)

    # Step 3: Baseline Join
    baseline_df = baseline_join(customers, orders)
    analyze_plan(baseline_df, "Baseline Join")

    # Step 4: Broadcast Join
    broadcast_df = broadcast_join(customers, orders)
    analyze_plan(broadcast_df, "Broadcast Join")

    # Step 5: Repartition Join
    repartitioned_df = repartition_before_join(customers, orders)
    analyze_plan(repartitioned_df, "Repartition Join")

    # Step 6: Cache Optimization
    cached_df = repartitioned_df.cache()
    cached_df.count()

    # Step 7: Coalesce Optimization
    final_df = coalesce_after_join(cached_df)
    analyze_plan(final_df, "Final Coalesced Output")

    # Step 8: Save Output
    final_df.write.mode("overwrite").parquet("data/processed/final_output")

    spark.stop()

if __name__ == "__main__":
    main()