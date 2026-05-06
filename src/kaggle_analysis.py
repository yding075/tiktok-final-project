import matplotlib.pyplot as plt
import pandas as pd


def analyze_kaggle_data(df):
    print("Columns:")
    print(df.columns)

    df = df[["views", "likes", "comment_count", "category_id"]].copy()

    df["views"] = pd.to_numeric(df["views"], errors="coerce")
    df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
    df["comment_count"] = pd.to_numeric(df["comment_count"], errors="coerce")

    print("\nAverage values:")
    print(df[["views", "likes", "comment_count"]].mean())

    print("\nSummary:")
    print(df[["views", "likes", "comment_count"]].describe())

    plt.hist(df["views"].dropna(), bins=50)
    plt.title("Distribution of Views (Kaggle Dataset)")
    plt.xlabel("Views")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("results/kaggle_views_distribution.png")
    plt.close()

    plt.scatter(df["views"], df["likes"], alpha=0.3)
    plt.title("Views vs Likes")
    plt.xlabel("Views")
    plt.ylabel("Likes")
    plt.tight_layout()
    plt.savefig("results/kaggle_views_vs_likes.png")
    plt.close()

    df["category_id"].value_counts().head(10).plot(kind="bar")
    plt.title("Top Video Categories")
    plt.xlabel("Category ID")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("results/kaggle_top_categories.png")
    plt.close()