![Logo](./public/FFFFFF-1.png)
# Slooze take home challenge data-engineering

# 📌 Problem Statement

## Part A – Data Collection: Crawler/Scraper/Data Collection Implementation

Your task is to design and implement a **data gathering application** capable of extracting relevant information from [IndiaMART](https://www.indiamart.com), [AliBaba](https://www.alibaba.com/), or similar B2B marketplaces. You are expected to:

- Identify and target **a few meaningful product categories** (e.g., industrial machinery, electronics, textiles, etc.).
- Build a custom web crawler, use a third-party scraping tool, or integrate AI-powered data extraction — **you are free to choose the best approach** for your solution.
- Ensure that the application respects target site structures and avoids being blocked or rate-limited.

### ✅ Evaluation Criteria:
- **Effectiveness and robustness** of the crawler/data collector
- **Code quality**, modularity, and maintainability
- **Clean, structured, and relevant** data output (JSON/CSV/etc.)


---

## Part B – Exploratory Data Analysis (EDA)

After collecting the data, perform an **exploratory data analysis** to uncover meaningful insights. This may include:

- Summary statistics of the dataset (counts, distributions, trends)
- Identification of common attributes (e.g., top product types, price ranges, frequent keywords)
- Regional insights (e.g., location-based supplier patterns)
- Any anomalies, inconsistencies, or quality gaps in the scraped data
to name a few

### ✅ Evaluation Criteria:
- 📊 Visualizations and charts (where useful)
- 🧠 Insights or hypotheses based on your findings

---
data-engineering-challenge/
│
├── crawler/
│   ├── __init__.py
│   ├── indiamart_scraper.py
│   └── alibaba_scraper.py     (optional)
│
├── etl/
│   ├── __init__.py
│   └── etl_process.py         (cleaning, transformation)
│
├── eda/
│   ├── __init__.py
│   ├── eda_analysis.ipynb     (your notebook)
│   └── run_eda.py             (script version of EDA)
│
├── data/
│   ├── raw/                   (scraped output)
│   │    ├── indiamart_*.csv
│   │    └── alibaba_*.csv
│   └── processed/             (cleaned CSV)
│        └── cleaned_data.csv
│
├── output/
│   ├── charts/                (plots saved by EDA)
│   │    ├── price_hist.png
│   │    ├── bar_plot.png
│   │    └── top_companies.png
│   ├── tables/
│   │    └── summary.csv
│   └── report.pptx            (auto-generated PPT)
│
├── tests/
│   ├── __init__.py
│   └── test_price_parser.py
│
├── main.py                    (pipeline runner)
├── make_report.py             (generate PPT)
├── requirements.txt
├── README.md
└── .gitignore
