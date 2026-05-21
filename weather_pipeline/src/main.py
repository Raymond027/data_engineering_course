import requests
from src.database.connection import SessionLocal, engine
from src.database.models import Base, WeatherData
from src.services.weather_service import fetch_weather
from src.utils.logger import logger


city_list = ["New York", "London", "Tokyo"]


def save_weather_data():
    """
    Fetch weather data and store it in PostgreSQL.
    """

    session = SessionLocal()

    try:
        for city in city_list:

            weather = fetch_weather(city)

            if weather:

                weather_record = WeatherData(
                    city=weather["city"],
                    temperature=weather["temperature"],
                    description=weather["description"],
                    timestamp=weather["timestamp"]
                )

                session.add(weather_record)

        session.commit()

        logger.info("Weather data successfully saved to PostgreSQL")

    except Exception as e:
        session.rollback()
        logger.error(f"Database transaction failed: {e}")

    finally:
        session.close()


if __name__ == "__main__":

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Run pipeline
    save_weather_data()