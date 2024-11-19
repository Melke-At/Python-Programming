import requests


def fetch_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)
        response.raise_for_status()

        joke_data = response.json()
        joke = joke_data.get("value")

        if joke:
            print("Here's a Chuck Norris joke for you:")
            print(joke)
        else:
            print("No joke found.")

    except requests.exceptions.RequestException as e:
        print("Error fetching joke:", e)


fetch_random_chuck_norris_joke()
