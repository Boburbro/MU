import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
CREDS_PATH = "bot/credentials.json"

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))
SHEET_URL = os.getenv("GOOGLE_SHEET_URL")


def extract_sheet_id(sheet_url):
    # Example: https://docs.google.com/spreadsheets/d/<ID>/edit?gid=0
    try:
        return sheet_url.split("/d/")[1].split("/")[0]
    except Exception:
        return None


# Sheetga yozish funksiyasi
def write_user_to_sheet(user_dict):
    sheet_id = extract_sheet_id(SHEET_URL)
    if not sheet_id:
        return
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_PATH, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).sheet1
    sheet.append_row(
        [
            user_dict.get("id", ""),
            user_dict.get("full_name", ""),
            user_dict.get("username", ""),
            user_dict.get("surname", ""),
            user_dict.get("age", ""),
            user_dict.get("email", ""),
        ]
    )
