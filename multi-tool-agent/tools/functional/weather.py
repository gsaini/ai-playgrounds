import aiohttp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def get_weather(location: str) -> dict:
    """
    Fetches the current weather for a specified location.

    This function uses a weather API to retrieve real-time weather data for a given location.
    It returns details such as temperature, weather condition, humidity, and wind information.

    Args:
        location (str): The name of the location (city, region, or country) for which to fetch the weather.

    Returns:
        dict: A dictionary containing the following keys:
            - location (str): The name of the location.
            - region (str): The region of the location.
            - country (str): The country of the location.
            - temperature (str): The current temperature in Celsius and Fahrenheit.
            - condition (str): A brief description of the current weather condition.
            - humidity (str): The current humidity percentage.
            - wind (str): The wind speed and direction.

        If the API call fails, the dictionary contains:
            - error (str): An error message indicating the failure reason.
    """
    weather_api = os.getenv("WEATHER_API_URL")
    api_key = os.getenv("WEATHER_API_KEY")
    
    # Use a real weather API (replace with your preferred provider)
    url = f"{weather_api}?key={api_key}&q={location}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                
                weather_data = {
                    "location": data["location"]["name"],
                    "region": data["location"]["region"],
                    "country": data["location"]["country"],
                    "temperature": f"{data['current']['temp_c']}°C / {data['current']['temp_f']}°F",
                    "condition": data["current"]["condition"]["text"],
                    "humidity": f"{data['current']['humidity']}%",
                    "wind": f"{data['current']['wind_mph']} mph {data['current']['wind_dir']}"
                }
                
                return weather_data
            else:
                return {"error": f"Failed to get weather data: {response.status}"}

async def get_weather_forecast(location: str, days: int) -> dict:
    """
    Fetches the weather forecast for a specified location and number of days.

    Args:
        location (str): The location for which to fetch the weather forecast.
        days (int): The number of days for the forecast.

    Returns:
        dict: A dictionary containing the forecast data or an error message.
    """
    weather_api = os.getenv("WEATHER_API_URL")
    api_key = os.getenv("WEATHER_API_KEY")

    # Use a real weather API (replace with your preferred provider)
    url = f"{weather_api}/forecast.json?key={api_key}&q={location}&days={days}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()

                forecast_data = {
                    "location": data["location"]["name"],
                    "region": data["location"]["region"],
                    "country": data["location"]["country"],
                    "forecast": []
                }

                for day in data["forecast"]["forecastday"]:
                    forecast_data["forecast"].append({
                        "date": day["date"],
                        "temperature": f"{day['day']['avgtemp_c']}°C / {day['day']['avgtemp_f']}°F",
                        "condition": day["day"]["condition"]["text"],
                        "humidity": f"{day['day']['avghumidity']}%",
                        "wind": f"{day['day']['maxwind_mph']} mph"
                    })

                return forecast_data
            else:
                return {"error": f"Failed to get weather forecast data: {response.status}"}