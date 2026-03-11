import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

SCRAPE_INTERVAL_MINUTES = 60
TOPICS_PER_DAY = 10
