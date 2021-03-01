"""Main"""

from analytic.metrics.country_metrics import get_country_dataframe

if __name__ == "__main__":
    df = get_country_dataframe()
    print(df.head())
