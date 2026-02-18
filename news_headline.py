import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
FILENAME = "headlines.txt"

def fetch_headlines():
    try:
        # Send GET request
        response = requests.get(URL, headers={
            "User-Agent": "Mozilla/5.0"
        })

        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all h2 tags (commonly used for headlines)
            headlines = soup.find_all("h2")

            extracted_headlines = []

            for tag in headlines:
                text = tag.get_text(strip=True)
                if text and len(text) > 30:  # filter small texts
                    extracted_headlines.append(text)

            return extracted_headlines[:10]  # top 10 headlines
        else:
            print("Failed to retrieve page. Status code:", response.status_code)
            return []

    except Exception as e:
        print("Error occurred:", e)
        return []


def save_headlines(headlines):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for index, headline in enumerate(headlines, start=1):
            file.write(f"{index}. {headline}\n")


def main():
    print("Fetching latest news headlines...")
    headlines = fetch_headlines()

    if headlines:
        save_headlines(headlines)
        print("Headlines saved successfully to headlines.txt")
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()
