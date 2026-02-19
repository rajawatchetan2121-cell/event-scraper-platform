import gspread
import openpyxl
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def sync_to_sheets():
    try:
        print("Starting Google Sheets sync...")

        # Load credentials from local JSON (for VS Code run)
        creds = Credentials.from_service_account_file(
            "service_account.json",
            scopes=SCOPES
        )

        client = gspread.authorize(creds)

        # Open sheet by URL (SAFER than name)
        sheet = client.open_by_url(
            "PASTE_YOUR_FULL_GOOGLE_SHEET_URL_HERE"
        ).sheet1

        # Load Excel
        wb = openpyxl.load_workbook("events.xlsx")
        ws = wb.active

        data = []
        for row in ws.iter_rows(values_only=True):
            data.append(list(row))

        # Clear existing data
        sheet.clear()

        # Insert new data
        sheet.append_rows(data)

        print("Google Sheet updated successfully!")

    except Exception as e:
        print("ERROR updating sheet:", e)
