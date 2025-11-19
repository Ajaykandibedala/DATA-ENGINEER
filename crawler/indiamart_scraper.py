import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Try to use fake_useragent if available, otherwise fall back to a stable UA string
try:
    import importlib
    _fu = importlib.import_module("fake_useragent")
    UserAgent = getattr(_fu, "UserAgent", None)
    _FAKE_UA_AVAILABLE = UserAgent is not None
except Exception:
    UserAgent = None
    _FAKE_UA_AVAILABLE = False

BASE_URL = "https://dir.indiamart.com/search.mp?ss={}"

if _FAKE_UA_AVAILABLE:
    try:
        ua = UserAgent()
    except Exception:
        ua = None
else:
    ua = None

def get_html(url):
    # Use fake_useragent when available, otherwise use a common browser UA
    if ua:
        try:
            ua_value = ua.random
        except Exception:
            ua_value = (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
            )
    else:
        ua_value = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        )

    headers = {"User-Agent": ua_value}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_products(html):
    soup = BeautifulSoup(html, "lxml")
    products = soup.select(".lst.cl")

    data = []
    for p in products:
        try:
            name = p.select_one(".prd-name").get_text(strip=True)
        except:
            name = None

        try:
            price = p.select_one(".r-price").get_text(strip=True)
        except:
            price = None

        try:
            company = p.select_one(".cmpny").get_text(strip=True)
        except:
            company = None

        try:
            location = p.select_one(".loc").get_text(strip=True)
        except:
            location = None

        try:
            link = p.select_one("a")["href"]
        except:
            link = None

        data.append({
            "product_name": name,
            "price": price,
            "company": company,
            "location": location,
            "product_url": link
        })

    return data


def scrape_indiamart(query, pages=2):
    final_data = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page} for {query}...")
        url = BASE_URL.format(query) + f"&pg={page}"
        
        html = get_html(url)
        data = parse_products(html)
        final_data.extend(data)

        time.sleep(1)  # avoid blocking

    df = pd.DataFrame(final_data)
    output_path = f"data/raw/indiamart_{query}.csv"
    # Ensure output directory exists
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

    return df
