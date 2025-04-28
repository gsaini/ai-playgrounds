from datetime import datetime
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder

from geopy.geocoders import Nominatim

def get_current_time_by_location(location: str) -> dict:
    """
    Returns the current time for a given location by determining its timezone.

    Args:
        location (str): The name of the location (city, region, or country).

    Returns:
        dict: A dictionary containing the status and the current time or an error message.
    """
    try:
        # Use geopy to get the latitude and longitude of the location
        geolocator = Nominatim(user_agent="timezone_locator")
        location_data = geolocator.geocode(location)

        if not location_data:
            return {
                "status": "error",
                "error_message": f"Could not find location: {location}"
            }

        # Use timezonefinder to get the timezone from latitude and longitude
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location_data.longitude, lat=location_data.latitude)

        if not timezone_str:
            return {
                "status": "error",
                "error_message": f"Could not determine timezone for location: {location}"
            }

        # Get the current time in the determined timezone
        timezone = ZoneInfo(timezone_str)
        current_time = datetime.now(timezone)

        return {
            "status": "success",
            "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
            "location": location_data.address
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }