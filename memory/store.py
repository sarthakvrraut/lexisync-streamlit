# memory/store.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils.logger import get_logger
from utils.time_utils import utc_now

logger = get_logger(__name__)

class MemoryStore:
    def __init__(self, sheet_name="LexiSyncDemo", json_key="service_account.json"):
        try:
            scope = ["https://spreadsheets.google.com/feeds",
                     "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
            self.client = gspread.authorize(creds)
            self.sheet = self.client.open(sheet_name).sheet1
            logger.info(f"Connected to Google Sheet: {sheet_name}")
        except Exception as e:
            logger.error(f"Failed to connect to Google Sheets: {e}")
            self.sheet = None

    def store_turn(self, text, translated, timestamp=None):
        if not self.sheet:
            return
        if not timestamp:
            timestamp = utc_now().isoformat()
        try:
            self.sheet.append_row([timestamp, text, translated])
        except Exception as e:
            logger.error(f"Failed to store row in Google Sheets: {e}")

    def get_full_transcript(self):
        if not self.sheet:
            return []
        try:
            rows = self.sheet.get_all_values()
            return rows[1:] if len(rows) > 1 else []
        except Exception as e:
            logger.error(f"Failed to fetch transcript from Google Sheets: {e}")
            return []
