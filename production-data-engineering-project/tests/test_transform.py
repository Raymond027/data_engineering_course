from etl.transform import transform_crypto

def test_transform():

    sample = [{
        "id":"bitcoin",
        "symbol":"btc",
        "current_price":50000,
        "market_cap":1000,
        "total_volume":100
    }]

    df = transform_crypto(sample)

    assert len(df) == 1