"""
A Simple Current Weather Application:

This Python script retrieves and prints the current weather for a given city using the OpenWeatherMap API.
The user is prompted to enter the city name, and the script fetches the weather information from the API.
The temperature is displayed in Celsius.

Usage:
- Run the script.
- Enter the name of the city when prompted.
- The script will print the current weather for the specified city.
"""

import requests

API_KEY = "Put your key here"  # Replace this with your actual API key


def current_weather():
    """Obtains and prints the current weather for a given city."""
    # Get the city name from the user
    city_name = input("Enter the city name: ")

    # Construct the API URL using the city name and API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

    # Make a GET request to the OpenWeatherMap API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        # If successful, parse the JSON response
        data = response.json()

        # Extract the weather description and temperature from the response
        description_weather = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15

        # Print the weather information for the city
        print(f"In {city_name}, {description_weather.title()}, with {temperature:.2f}°C")
    else:
        # If the request was not successful, print an error message
        print("Error in the request.")


if __name__ == "__main__":
    current_weather()
