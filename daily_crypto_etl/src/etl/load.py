import os
from datetime import datetime

def save_to_csv(df, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    filename = f"crypto_prices_{timestamp}.csv"

    full_path = os.path.join(output_dir, filename)

    df.to_csv(full_path, index=False)

    return full_path