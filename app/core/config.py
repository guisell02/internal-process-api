from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAMES = os.getenv("PROJECT_NAME", "Internal Process API")