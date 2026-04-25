from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "Internal Process API")

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")
