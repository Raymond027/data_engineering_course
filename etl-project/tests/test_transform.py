import pandas as pd

from etl.transform import transform_data


def test_transform_data():

    sample_df = pd.DataFrame(
        {
            "id": ["bitcoin"],
            "symbol": ["btc"],
            "current_price": [100000],
            "market_cap": [1000000000],
        }
    )

    result = transform_data(sample_df)

    assert len(result.columns) == 4