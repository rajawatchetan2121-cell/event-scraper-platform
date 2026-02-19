import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URLS = [
    "music-in-{}-book-tickets",
    "nightlife-in-{}-book-tickets",
    "comedy-shows-in-{}-book-tickets",
    "sports-events-in-{}-book-tickets",
    "performances-in-{}-book-tickets",
    "food-drinks-in-{}-book-tickets",
    "fests-fairs-in-{}-book-tickets",
    "social-mixers-in-{}-book-tickets",
    "openmics-in-{}-book-tickets"
]

def fetch_events(city):
    events = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for slug in BASE_URLS:
        url = f"https://www.district.in/events/{slug.format(city.lower())}"
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            cards = soup.select("div.dds-w-full.dds-h-full.item-cards")

            for card in cards:
                parent = card.find_parent("a")
                link = parent["href"] if parent else ""

                title = card.find("h5")
                spans = card.find_all("span")

                date = spans[0].text.strip() if len(spans) > 0 else ""
                venue = spans[1].text.strip() if len(spans) > 1 else ""

                events.append({
                    "event_name": title.text.strip() if title else "",
                    "date": date,
                    "venue": venue,
                    "city": city,
                    "category": "Event",
                    "url": link,
                    "status": "Active",
                    "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M")
                })

        except:
            continue

    return events
