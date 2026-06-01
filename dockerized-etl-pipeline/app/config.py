from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")