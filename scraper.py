from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time


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

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    events = []
    seen_links = set()

    for category in CATEGORIES:

        slug = f"{category}-in-{city.lower()}-book-tickets"
        url = f"https://www.district.in/events/{slug}"

        print(f"Opening → {url}")

        try:
            driver.get(url)
            time.sleep(4)

            # Scroll for lazy loading
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            cards = driver.find_elements(
                By.CSS_SELECTOR,
                "div.dds-w-full.dds-h-full.item-cards"
            )

            print(f"{category}: {len(cards)} cards")

            for card in cards:
                try:
                    parent = card.find_element(By.XPATH, "./ancestor::a")
                    link = parent.get_attribute("href")

                    if link in seen_links:
                        continue
                    seen_links.add(link)

                    title = card.find_element(By.TAG_NAME, "h5").text
                    spans = card.find_elements(By.TAG_NAME, "span")

                    date = spans[0].text if len(spans) > 0 else ""
                    venue = spans[1].text if len(spans) > 1 else ""

                    events.append({
                        "event_name": title,
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

        except:
            continue

    driver.quit()

    print(f"\nTotal unique events: {len(events)}")

    return events
