from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
BROWSER = int(os.getenv("BROWSER", 1))  # ברירת מחדל ל־1 אם לא מוגדר

USER_DETAILS = {
    "email": os.getenv("EMAIL"),
    "password": os.getenv("PASSWORD"),
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "job": os.getenv("JOB"),
    "phone": os.getenv("PHONE"),
    "company_name": os.getenv("COMPANY_NAME"),
    "address": os.getenv("ADDRESS"),
    "city": os.getenv("CITY"),
    "zip": os.getenv("ZIP")
}

EXIST_USER = os.getenv("EXIST_USER")
EXIST_PASSWORD = os.getenv("EXIST_PASSWORD")

REF_MANUAL_VERSION = os.getenv("REF_MANUAL_VERSION")
RELEASE_NOTE_VERSION = os.getenv("RELEASE_NOTE_VERSION")