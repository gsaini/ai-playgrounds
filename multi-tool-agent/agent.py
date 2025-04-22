from google.adk.agents import Agent

from .tools.functional.weather import get_weather, get_weather_forecast
from .tools.functional.time import get_current_time_by_location

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="An intelligent agent capable of answering questions about weather, including current conditions, forecasts, and time for any location, and providing recommendations based on the data.",
    instruction="You are a helpful agent that can answer user questions about the weather, including current conditions, forecasts for multiple days, and the current time for any location. Use the tools available to fetch accurate data and provide meaningful recommendations based on the information.",
    tools=[
        get_weather, 
        get_weather_forecast, 
        get_current_time_by_location
    ],
)
