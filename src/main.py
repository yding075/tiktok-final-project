import argparse

from load import get_youtube_data
from analyze import summarize_by_keyword, plot_results
from trends_analysis import get_trends_data, plot_trends_summary


def run_youtube_pipeline():
    print("Running YouTube API pipeline...")

    df = get_youtube_data()
    summarize_by_keyword(df)
    plot_results(df)

    print("YouTube API pipeline completed.\n")


def run_trends_pipeline():
    print("Running Google Trends pipeline...")

    df = get_trends_data()
    if df is not None:
        plot_trends_summary(df)

    print("Google Trends pipeline completed.\n")


def main():
    parser = argparse.ArgumentParser(description="Run project pipelines")
    parser.add_argument("--youtube", action="store_true", help="Run YouTube API pipeline")
    parser.add_argument("--trends", action="store_true", help="Run Google Trends pipeline")
    parser.add_argument("--all", action="store_true", help="Run all available pipelines")

    args = parser.parse_args()

    if args.all:
        run_youtube_pipeline()
        run_trends_pipeline()
    elif args.youtube:
        run_youtube_pipeline()
    elif args.trends:
        run_trends_pipeline()
    else:
        print("No pipeline selected.")
        print("Use one of the following:")
        print("  python src/main.py --youtube")
        print("  python src/main.py --trends")
        print("  python src/main.py --all")


if __name__ == "__main__":
    main()