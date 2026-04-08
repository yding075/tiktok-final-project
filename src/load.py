import requests
import pandas as pd

def get_api_data():
    url =  "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = get_api_data()
    print(df.head())