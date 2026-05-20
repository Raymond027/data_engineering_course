from weather_client import WeatherClient
from config import CITY_LIST
from logger import get_logger

logger = get_logger()


def run_pipeline():
    client = WeatherClient()
    results = []

    logger.info("Weather pipeline started")

    for city in CITY_LIST:
        try:
            result = client.fetch_weather(city)

            if result:
                results.append(result)
                logger.info(f"Processed: {result}")

        except Exception as e:
            logger.error(f"Critical failure for {city}: {str(e)}")
            continue  # ensures pipeline keeps running

    logger.info("Pipeline completed")
    logger.info(f"Final results: {results}")

    return results


if __name__ == "__main__":
    run_pipeline()