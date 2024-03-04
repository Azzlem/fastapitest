
import os
from dotenv import load_dotenv

load_dotenv()

required_vars = ["DB_USER", "DB_PASS", "DB_HOST", "DB_PORT", "DB_NAME"]

for var in required_vars:
    if os.getenv(var) is None:
        raise ValueError(f"Missing required environment variable: {var}")

DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
