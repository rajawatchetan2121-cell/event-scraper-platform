import gspread
from google.oauth2.service_account import Credentials
import openpyxl

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def sync_to_sheets():
    creds = Credentials.from_service_account_file(
        "service_account.json",
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sheet = client.open("Event Dashboard").sheet1

    wb = openpyxl.load_workbook("events.xlsx")
    ws = wb.active

    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(list(row))

    sheet.clear()
    sheet.append_rows(data)
