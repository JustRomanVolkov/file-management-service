import os


class Settings:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


settings = Settings()
