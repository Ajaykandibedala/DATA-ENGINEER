# main.py
import argparse
from crawler.indiamart_scraper import scrape_indiamart
from eda.run_eda import run_eda  # pyright: ignore[reportMissingImports] # we will create this helper
from etl import run_etl         # type: ignore # we will create this helper

def main(args):
    if args.step in ("scrape","all"):
        scrape_indiamart(args.query, pages=args.pages)

    if args.step in ("etl","all"):
        run_etl()   # collects raw CSVs and writes processed CSV

    if args.step in ("eda","all"):
        run_eda()   # loads processed CSV and produces charts + outputs

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--step", default="all", choices=["scrape","etl","eda","all"])
    p.add_argument("--query", default="industrial machinery")
    p.add_argument("--pages", type=int, default=2)
    args = p.parse_args()
    main(args)
