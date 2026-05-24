from app.transform import clean_crypto_data

def test_clean_crypto_data():
    sample_data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 50000,
            "market_cap": 1000000,
            "total_volume": 50000,
            "price_change_percentage_24h": 2.5
        }
    ]

    df = clean_crypto_data(sample_data)

    assert len(df) == 1

    assert "coin_id" in df.columns