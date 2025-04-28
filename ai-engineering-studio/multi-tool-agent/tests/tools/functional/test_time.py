import pytest
from tools.functional.time import get_current_time_by_location

def test_get_current_time_by_location_valid():
    result = get_current_time_by_location("New York")
    assert result["status"] == "success"
    assert "current_time" in result
    assert "location" in result

def test_get_current_time_by_location_invalid():
    result = get_current_time_by_location("InvalidLocation123")
    assert result["status"] == "error"
    assert "error_message" in result

def test_get_current_time_by_location_error_handling(monkeypatch):
    def mock_geocode(*args, **kwargs):
        raise Exception("Mocked exception")

    monkeypatch.setattr("geopy.geocoders.Nominatim.geocode", mock_geocode)

    result = get_current_time_by_location("New York")
    assert result["status"] == "error"
    assert result["error_message"] == "Mocked exception"