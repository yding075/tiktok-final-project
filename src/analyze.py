import matplotlib.pyplot as plt
from load import get_youtube_data


def load_cached_or_api_data():
    print("Fetching YouTube data from API...")
    df = get_youtube_data()
    return df


def summarize_by_keyword(df):
    summary = df.groupby("keyword")[["views", "likes", "comments"]].mean().round(2)

    print("Average engagement by keyword:")
    print(summary)

    return summary


def plot_results(df):
    summary = df.groupby("keyword")[["views", "likes", "comments"]].mean()

    summary["views"].plot(kind="bar")
    plt.title("Average Views by Keyword")
    plt.ylabel("Views")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/youtube_views.png")
    plt.close()

    summary["likes"].plot(kind="bar")
    plt.title("Average Likes by Keyword")
    plt.ylabel("Likes")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/youtube_likes.png")
    plt.close()

    summary["comments"].plot(kind="bar")
    plt.title("Average Comments by Keyword")
    plt.ylabel("Comments")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/youtube_comments.png")
    plt.close()


if __name__ == "__main__":
    summarize_by_keyword()
    plot_results()