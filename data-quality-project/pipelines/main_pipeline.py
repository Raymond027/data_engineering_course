import os

def run_pipeline():

    print("1. Extracting data...")
    os.system("python etl/extract_weather.py")

    print("2. Transforming data...")
    os.system("python etl/transform_weather.py")

    print("3. Running validation...")
    os.system("python validation/run_weather_validation.py")

    print("4. Loading to warehouse (mock)")
    print("PIPELINE COMPLETED")

if __name__ == "__main__":
    run_pipeline()