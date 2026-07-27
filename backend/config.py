import os
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORK_BOARD_ID = os.getenv("WORK_BOARD_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")