from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import time

TRENDS_KEYWORDS = ["food", "makeup", "travel"]
TRENDS_GEO = "US"

TIME_WINDOWS = [
    ("2026-01-01", "2026-01-31"),
    ("2026-02-01", "2026-02-28"),
    ("2026-03-01", "2026-03-31"),
]

RESULT_PATH = "results/google_trends_interest.png"


def fetch_trends_data(keywords=TRENDS_KEYWORDS):
    print("Loading Google Trends data...")
    pytrends = TrendReq(hl="en-US", tz=360)
    all_trend_data = []

    for keyword in keywords:
        for start_date, end_date in TIME_WINDOWS:
            timeframe = f"{start_date} {end_date}"
            print(f"Fetching '{keyword}' from {start_date} to {end_date}...")

            try:
                pytrends.build_payload([keyword], timeframe=timeframe, geo=TRENDS_GEO)
                trend_df = pytrends.interest_over_time()

                if trend_df.empty:
                    print(f"No data found for '{keyword}' in {timeframe}.")
                    time.sleep(5)
                    continue

                if "isPartial" in trend_df.columns:
                    trend_df = trend_df.drop(columns=["isPartial"])

                trend_df = trend_df.reset_index()
                trend_df = trend_df[["date", keyword]]
                trend_df = trend_df.rename(columns={keyword: "interest"})
                trend_df["keyword"] = keyword

                all_trend_data.append(trend_df)

            except Exception as e:
                print(f"Failed for '{keyword}' in {timeframe}: {e}")

            time.sleep(5)

    if not all_trend_data:
        print("No trends data collected.")
        return None

    combined_trends = pd.concat(all_trend_data, ignore_index=True)

    print("\nGoogle Trends data:")
    print(combined_trends.head())

    print("\nAverage popularity by keyword:")
    print(combined_trends.groupby("keyword")["interest"].mean().sort_values(ascending=False))

    return combined_trends


def get_trends_data():
    return fetch_trends_data()


def plot_trends_summary(df):
    summary = df.groupby("keyword")["interest"].mean().sort_values(ascending=False)

    summary.plot(kind="bar")
    plt.title("Average Google Trends Interest by Keyword")
    plt.xlabel("Keyword")
    plt.ylabel("Average Interest")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(RESULT_PATH)
    plt.close()


if __name__ == "__main__":
    trends_df = get_trends_data()
    if trends_df is not None:
        plot_trends_summary(trends_df)