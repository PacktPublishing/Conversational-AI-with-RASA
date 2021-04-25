import os
import datetime
from typing import Dict, Optional

import requests
import json
from requests import ConnectionError, HTTPError, TooManyRedirects, Timeout

UNIT = "c"  # 温度单位
LANGUAGE = "zh-Hans"  # 查询结果的返回语言

owm_api_key = os.getenv("OWM_KEY", "")  # API key
assert owm_api_key

from pyowm.owm import OWM

owm = OWM(owm_api_key)
mgr = owm.weather_manager()

one_day_timedelta = datetime.timedelta(days=1)


class WeatherCondition:
    def __init__(self, temp_min, temp_max, status):
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.status = status

    def __repr__(self):
        return f"WeatherCondition(temp_min: {self.temp_min}, temp_max: {self.temp_max}, status: {self.status})"


def convert_weather_to_condition(weather):
    temp = weather.temperature("celsius")
    temp_min = temp.get("min")
    temp_max = temp.get("max")
    status = weather.detailed_status

    return WeatherCondition(temp_min, temp_max, status)


def fetch_weather(lat: float, lon: float) -> Dict[datetime.date, WeatherCondition]:
    one_call = mgr.one_call(lat=lat, lon=lon)

    daily_weather = {}

    # weather_today = one_call.current
    today = datetime.datetime.now()
    # daily_weather[today.date()] = convert_weather_to_condition(weather_today)

    current_date = today
    for daily in one_call.forecast_daily:
        assert current_date.date() == daily.reference_time("date").date()
        daily_weather[current_date.date()] = convert_weather_to_condition(daily)
        current_date = current_date + one_day_timedelta

    return daily_weather


def get_weather_by_date(lat: float, lon: float, day: datetime.date) -> Optional[WeatherCondition]:
    result = fetch_weather(lat, lon)

    return result.get(day)


def get_text_weather_date(lat: float, lon: float, date: datetime.date, text_date: str, text_city: str) -> str:
    try:
        result = get_weather_by_date(lat, lon, date)
    except (ConnectionError, HTTPError, TooManyRedirects, Timeout) as e:
        text_message = "{}".format(e)
    else:
        text_message_tpl = "The weather of {text_city} for {text_date} ({date}) is {status}, it's tempterpure range is：{temp_min}℃-{temp_max}℃."
        text_message = text_message_tpl.format(
            text_city=text_city,
            text_date=text_date,
            date=date,
            status=result.status,
            temp_min=result.temp_min,
            temp_max=result.temp_max
        )

    return text_message
