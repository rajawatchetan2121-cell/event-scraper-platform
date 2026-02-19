    
import streamlit as st
import pandas as pd
import openpyxl
from scraper import fetch_events
from storage import upsert_events
from collections import Counter

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


st.title("🎉 Event Scraper & Analytics Dashboard")

# Use dropdown instead of free text
city = st.selectbox(
    "Select City",
    ["mumbai", "jaipur", "delhi", "bangalore", "pune"]
)

scrape_btn = st.button("Scrape Events")

if scrape_btn:
    with st.spinner("Scraping events... Please wait..."):
        events = fetch_events(city)

        if len(events) == 0:
            st.warning("No events found for this city.")
        else:
            upsert_events(events)
            st.success(f"✅ {len(events)} events scraped successfully!")


# -------------------------
# LOAD DATA
# -------------------------
def load_data():
    try:
        wb = openpyxl.load_workbook("events.xlsx")
        ws = wb.active

        data = []
        headers = [cell.value for cell in ws[1]]

        for row in ws.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return pd.DataFrame(data, columns=headers)

    except:
        return pd.DataFrame()

df = load_data()

# -------------------------
# ANALYTICS SECTION
# -------------------------
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

