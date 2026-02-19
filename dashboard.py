import streamlit as st
import pandas as pd
import openpyxl
from scraper import fetch_events
from storage import upsert_events
from collections import Counter
import gspread
from google.oauth2.service_account import Credentials


# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Event Scraper & Analytics Platform",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------
st.title("🎉 Event Scraper & Analytics Platform")
st.markdown("Scrape, Store, Sync & Analyze Events Data")

st.divider()

# -------------------------
# SCRAPE SECTION
# -------------------------
st.subheader("🔍 Scrape Events")

col1, col2 = st.columns([3, 1])

with col1:
    city = st.text_input("Enter City Name", "mumbai")

with col2:
    scrape_btn = st.button("Scrape")

if scrape_btn:
    with st.spinner("Scraping events..."):
        events = fetch_events(city)
        upsert_events(events)
    st.success(f"✅ {len(events)} events scraped and stored successfully!")

st.divider()

# -------------------------
# LOAD DATA
# -------------------------
def load_data_from_google():
    try:
        creds_dict = st.secrets["gcp_service_account"]

        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
        )

        client = gspread.authorize(creds)

        sheet = client.open("Event Dashboard").sheet1

        data = sheet.get_all_records()

        return pd.DataFrame(data)

    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()
df = load_data_from_google()

# -------------------------
# ANALYTICS SECTION
# -------------------------

if not df.empty:
    selected_city = st.selectbox(
        "Filter by City",
        df["city"].unique()
    )

    df = df[df["city"] == selected_city]

if not df.empty:

    st.subheader("📊 Dashboard Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Events", len(df))

    with col2:
        active_count = len(df[df["status"] == "Active"])
        st.metric("Active Events", active_count)

    with col3:
        expired_count = len(df[df["status"] == "Expired"])
        st.metric("Expired Events", expired_count)

    st.divider()

    col4, col5 = st.columns(2)

    with col4:
        st.subheader("📍 Events per City")
        st.bar_chart(df["city"].value_counts())

    with col5:
        st.subheader("🏷 Events per Category")
        st.bar_chart(df["category"].value_counts())

    st.divider()

    st.subheader("📄 Events Data")
    st.dataframe(df, use_container_width=True)

else:
    st.info("No data found. Please scrape events first.")

