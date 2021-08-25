import datetime
from service.weather import fetch_weather, get_weather_by_date, get_text_weather_date

today = datetime.datetime.now().date()


def test_fetch_weather():
    weather = fetch_weather(31.222219, 121.458061)

    assert len(weather) == 8


def test_get_weather_by_date():
    weather = get_weather_by_date(31.222219, 121.458061, today)

    assert weather


def test_get_text_weather_date():
    text_weather = get_text_weather_date(31.222219, 121.458061, today, "Shanghai", "today")

    assert text_weather
