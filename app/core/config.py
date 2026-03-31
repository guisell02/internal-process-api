from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "Internal Process API")

DATABASE_URL: str = os.getenv("DATABASE_URL")
