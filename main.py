print("SCRIPT STARTED")

import argparse
import time
from scraper import fetch_events
from storage import upsert_events


def run(city):
    print(f"\nFetching events for {city}...")

    events = fetch_events(city)

    print(f"{len(events)} events found")

    upsert_events(events)

    print("Excel updated ✅")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)

    args = parser.parse_args()

    city = args.city

    # 🔥 run forever every 2 minutes
    while True:
        run(city)

        print("Waiting 2 minutes...\n")
        time.sleep(120)   # 120 seconds = 2 minutes


if __name__ == "__main__":
    main()
