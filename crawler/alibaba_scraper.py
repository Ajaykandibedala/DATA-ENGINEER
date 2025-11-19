# crawler/alibaba_scraper.py
import os, time
from urllib.parse import quote_plus, urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText={query}"

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=15); r.raise_for_status()
    return r.text

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    cards = soup.select(".J-offer-wrapper, .organic-gallery-offer")
    out = []
    for c in cards:
        title = c.select_one(".elements-title-normal") or c.select_one(".offer-title")
        price = c.select_one(".price")
        company = c.select_one(".company")
        link = c.select_one("a[href]")
        out.append({
            "product_name": (title.get_text(strip=True) if title else None),
            "price": (price.get_text(strip=True) if price else None),
            "company": (company.get_text(strip=True) if company else None),
            "product_url": (urljoin('https://www.alibaba.com', link['href']) if link and link.has_attr('href') else None)
        })
    return out

def scrape_alibaba(query, pages=1):
    allrows=[]
    for p in range(1, pages+1):
        url = BASE.format(query=quote_plus(query)) + f"&page={p}"
        html = get_html(url)
        allrows += parse(html)
        time.sleep(1)
    df = pd.DataFrame(allrows)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/alibaba_{query.replace(' ','_')}.csv", index=False)
    return df
