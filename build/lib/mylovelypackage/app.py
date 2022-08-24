import requests

def get_characters():
    base_url = "https://www.breakingbadapi.com/api/characters"
    with requests.Session() as session:
        response = session.get(base_url)
    response = response.json()
    return [r.get("name") for r in response][0]


if __name__ == "__main__":
    characters = get_characters()
    print(characters)
