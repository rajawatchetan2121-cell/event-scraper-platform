import requests
from bs4 import BeautifulSoup
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
        "User-Agent": "Mozilla/5.0"
    }

    for category in CATEGORIES:

        slug = f"{category}-in-{city.lower()}-book-tickets"
        url = f"https://www.district.in/events/{slug}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            cards = soup.select("div.dds-w-full.dds-h-full.item-cards")

            for card in cards:

                parent = card.find_parent("a")
                if not parent:
                    continue

                link = parent.get("href")

                if link in seen_links:
                    continue
                seen_links.add(link)

                title = card.find("h5")
                spans = card.find_all("span")

                date = spans[0].text.strip() if len(spans) > 0 else ""
                venue = spans[1].text.strip() if len(spans) > 1 else ""

                events.append({
                    "event_name": title.text.strip() if title else "",
                    "date": date,
                    "venue": venue,
                    "city": city,
                    "category": category,
                    "url": link,
                    "status": "Active",
                    "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M")
                })

        except:
            continue

    return events
