from datetime import datetime, timedelta
import pandas as pd

def check_freshness(df, column="timestamp", max_delay_hours=2):
    df[column] = pd.to_datetime(df[column])

    latest = df[column].max()
    threshold = datetime.utcnow() - timedelta(hours=max_delay_hours)

    if latest < threshold:
        raise Exception(f"DATA STALE: latest={latest}, threshold={threshold}")

    return True