import numpy as np
from scipy.stats import zscore


def detect_anomalies(df):

    scores = zscore(
        df["order_amount"]
    )

    anomalies = df[
        np.abs(scores) > 3
    ]

    return {
        "anomaly_count": len(anomalies),
        "anomalies": anomalies.to_dict(
            orient="records"
        )
    }