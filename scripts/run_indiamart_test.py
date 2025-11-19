import os
import sys

# Ensure project root is on sys.path so `crawler` can be imported
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from crawler.indiamart_scraper import scrape_indiamart


if __name__ == "__main__":
    # Single-page smoke test
    df = scrape_indiamart("cotton", pages=1)
    print("Rows scraped:", len(df))
    if not df.empty:
        print(df.head().to_string(index=False))
