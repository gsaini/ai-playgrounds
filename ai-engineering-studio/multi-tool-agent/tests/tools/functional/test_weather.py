import pytest
from tools.functional.weather import get_weather, get_weather_forecast

@pytest.mark.asyncio
async def test_get_weather_valid(monkeypatch):
    async def mock_get(self, url):
        class MockResponse:
            status = 200

            async def json(self):
                return {
                    "location": {"name": "New York", "region": "New York", "country": "USA"},
                    "current": {
                        "temp_c": 20,
                        "temp_f": 68,
                        "condition": {"text": "Sunny"},
                        "humidity": 50,
                        "wind_mph": 10,
                        "wind_dir": "NW"
                    }
                }

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

        return MockResponse()

    monkeypatch.setattr("aiohttp.ClientSession.get", mock_get)

    result = await get_weather("New York")
    assert result["location"] == "New York"
    assert result["temperature"] == "20°C / 68°F"
    assert result["condition"] == "Sunny"

@pytest.mark.asyncio
async def test_get_weather_forecast_valid(monkeypatch):
    async def mock_get(self, url):
        class MockResponse:
            status = 200

            async def json(self):
                return {
                    "location": {"name": "New York", "region": "New York", "country": "USA"},
                    "forecast": {
                        "forecastday": [
                            {
                                "date": "2025-04-23",
                                "day": {
                                    "avgtemp_c": 18,
                                    "avgtemp_f": 64,
                                    "condition": {"text": "Cloudy"},
                                    "avghumidity": 60,
                                    "maxwind_mph": 12
                                }
                            }
                        ]
                    }
                }

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

        return MockResponse()

    monkeypatch.setattr("aiohttp.ClientSession.get", mock_get)

    result = await get_weather_forecast("New York", 1)
    assert result["location"] == "New York"
    assert result["forecast"][0]["temperature"] == "18°C / 64°F"
    assert result["forecast"][0]["condition"] == "Cloudy"

@pytest.mark.asyncio
async def test_get_weather_invalid(monkeypatch):
    async def mock_get(self, url):
        class MockResponse:
            status = 404

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

        return MockResponse()

    monkeypatch.setattr("aiohttp.ClientSession.get", mock_get)

    result = await get_weather("InvalidLocation123")
    assert "error" in result

@pytest.mark.asyncio
async def test_get_weather_forecast_invalid(monkeypatch):
    async def mock_get(self, url):
        class MockResponse:
            status = 404

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

        return MockResponse()

    monkeypatch.setattr("aiohttp.ClientSession.get", mock_get)

    result = await get_weather_forecast("InvalidLocation123", 1)
    assert "error" in result