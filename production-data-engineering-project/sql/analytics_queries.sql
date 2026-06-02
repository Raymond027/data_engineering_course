SELECT
    symbol,
    AVG(current_price)
FROM crypto_market_summary
GROUP BY symbol
ORDER BY AVG(current_price) DESC
LIMIT 10;