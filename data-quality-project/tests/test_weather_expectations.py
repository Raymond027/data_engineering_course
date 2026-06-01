import pandas as pd
from validation.validation_utils import check_freshness

def test_freshness():
    df = pd.DataFrame({
        "timestamp": ["2026-06-01T10:00:00Z"]
    })

    assert check_freshness(df, "timestamp", 24)