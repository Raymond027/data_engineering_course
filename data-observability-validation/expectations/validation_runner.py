import json

from expectations.customer_expectations import (
    run_expectations
)

from validation.duplicate_checks import (
    check_duplicates
)

from validation.freshness_checks import (
    check_freshness
)

from validation.anomaly_detection import (
    detect_anomalies
)


def run_all_validations(
        df,
        config
):

    expectation_results = run_expectations(df)

    duplicate_results = check_duplicates(df)

    freshness_results = check_freshness(
        df,
        config["freshness_threshold_hours"]
    )

    anomaly_results = detect_anomalies(df)

    return {
        "expectations": [
            r.success
            for r in expectation_results
        ],
        "duplicates": duplicate_results,
        "freshness": freshness_results,
        "anomalies": anomaly_results
    }