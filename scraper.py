import requests
from datetime import datetime

CATEGORIES = [
    "music",
    "nightlife",
    "comedy-shows",
    "sports-events",
    "performances",
    "food-drinks",
    "fests-fairs",
    "social-mixers",
    "openmics"
]

def fetch_events(city: str):

    events = []
    seen_links = set()

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    for category in CATEGORIES:

        slug = f"{category}-in-{city.lower()}-book-tickets"
        url = f"https://www.district.in/events/{slug}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            # Look for embedded JSON data
            if "application/json" not in response.headers.get("Content-Type", ""):
                continue

            data = response.json()

            if "events" not in data:
                continue

            for item in data["events"]:

                link = item.get("eventUrl")

                if link in seen_links:
                    continue
                seen_links.add(link)

                events.append({
                    "event_name": item.get("title", ""),
                    "date": item.get("eventDate", ""),
                    "venue": item.get("venueName", ""),
                    "city": city,
                    "category": category,
                    "url": link,
                    "status": "Active",
                    "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M")
                })

        except:
            continue

    return events
