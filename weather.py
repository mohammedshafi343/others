import requests

def get_weather(city, api_key):
    """Fetch weather data for the specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
    else:
        print("City not found.")

def weather_app():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    weather_app()
