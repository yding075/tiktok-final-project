from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_youtube_data():
    if API_KEY is None:
        raise ValueError("YOUTUBE_API_KEY is missing. Please set it in your environment or .env file.")

    youtube = build("youtube", "v3", developerKey=API_KEY)

    keywords = [
        "food",
        "makeup",
        "travel",
        "fitness",
        "gaming"
    ]

    all_videos = []

    for keyword in keywords:
        search_request = youtube.search().list(
            q=keyword,
            part="snippet",
            maxResults=30,
            type="video"
        )
        search_response = search_request.execute()

        video_ids = [item["id"]["videoId"] for item in search_response["items"]]

        video_request = youtube.videos().list(
            part="statistics,snippet",
            id=",".join(video_ids)
        )
        video_response = video_request.execute()

        for item in video_response["items"]:
            all_videos.append({
                "keyword": keyword,
                "videoId": item["id"],
                "title": item["snippet"]["title"],
                "views": int(item["statistics"].get("viewCount", 0)),
                "likes": int(item["statistics"].get("likeCount", 0)),
                "comments": int(item["statistics"].get("commentCount", 0)),
            })

    df = pd.DataFrame(all_videos)
    return df


if __name__ == "__main__":
    df = get_youtube_data()
    print(df.head())
    print(df.columns.tolist())
    print(df.groupby("keyword").size())