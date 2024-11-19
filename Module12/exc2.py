import requests

def get_weather(api_key, municipality):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": municipality,
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature_kelvin = data['main']['temp']

            temperature_celsius = temperature_kelvin - 273.15

            print(f"Weather in {municipality}: {weather_description.capitalize()}")
            print(f"Temperature: {temperature_celsius:.2f}°C")
        else:
            print(f"Error: {data['message'].capitalize()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    municipality_name = input("Enter the name of the municipality: ")

    api_key = "your_api_key_here"

    get_weather(api_key, municipality_name)
