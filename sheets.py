import gspread
import openpyxl
import streamlit as st
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def sync_to_sheets():
    try:
        # ✅ Read credentials from Streamlit Secrets
        creds_dict = st.secrets["gcp_service_account"]

        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=SCOPES
        )

        client = gspread.authorize(creds)

        # Make sure this name matches your Google Sheet EXACTLY
        sheet = client.open("Event Dashboard").sheet1

        wb = openpyxl.load_workbook("events.xlsx")
        ws = wb.active

        data = []
        for row in ws.iter_rows(values_only=True):
            data.append(list(row))

        sheet.clear()
        sheet.append_rows(data)

    except Exception as e:
        st.error(f"Google Sheets sync failed: {e}")
