import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from analyze import summarize_by_keyword
from trends_analysis import plot_trends_summary


def test_summarize_by_keyword():
    test_df = pd.DataFrame({
        "keyword": ["food", "food", "makeup"],
        "views": [100, 300, 500],
        "likes": [10, 30, 50],
        "comments": [1, 3, 5]
    })

    result = summarize_by_keyword(test_df)

    assert result.loc["food", "views"] == 200
    assert result.loc["food", "likes"] == 20
    assert result.loc["food", "comments"] == 2
    assert result.loc["makeup", "views"] == 500


def test_trends_summary_plot():
    os.makedirs("results", exist_ok=True)

    test_df = pd.DataFrame({
        "keyword": ["food", "food", "makeup"],
        "interest": [20, 40, 60]
    })

    plot_trends_summary(test_df)

    assert os.path.exists("results/google_trends_interest.png")


if __name__ == "__main__":
    test_summarize_by_keyword()
    test_trends_summary_plot()
    print("All tests passed!")