from sqlalchemy import create_engine
from app.config import Config

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{Config.DB_USER}:{Config.DB_PASSWORD}"
    f"@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)