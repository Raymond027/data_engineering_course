CREATE TABLE IF NOT EXISTS raw_crypto (
    id SERIAL PRIMARY KEY,
    coin_id VARCHAR(100),
    symbol VARCHAR(20),
    name VARCHAR(100),
    current_price NUMERIC,
    market_cap BIGINT,
    total_volume BIGINT,
    price_change_percentage_24h NUMERIC,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS crypto_summary (
    id SERIAL PRIMARY KEY,
    total_market_cap NUMERIC,
    avg_price NUMERIC,
    top_coin VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);