import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Database configuration
DB_URL = os.getenv("DB_URL")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Safety check (very important)
if not DB_URL or not DB_NAME or not COLLECTION_NAME:
    raise EnvironmentError("Environment variables not loaded properly")