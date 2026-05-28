def generate_summary(df):

    total_assets = len(df)

    avg_price = round(df["price_usd"].mean(), 2)

    summary = f"""
    Daily Crypto Summary
    --------------------
    Total Assets: {total_assets}
    Average Price: ${avg_price}
    """

    return summary