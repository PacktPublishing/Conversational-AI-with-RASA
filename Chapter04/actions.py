from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from service.weather import get_text_weather_date
from service.normalization import text_to_date


class ActionReportWeather(Action):
    def __init__(self):
        pass

    def name(self) -> Text:
        return "action_report_weather"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("address")
        date_text = tracker.get_slot("date-time")

        date_object = text_to_date(date_text)

        if not date_object:  # parse date_time failed
            msg = "暂不支持查询 {} 的天气".format([city, date_text])
            return [SlotSet("matches", msg)]
        else:
            try:
                weather_data = get_text_weather_date(city, date_object, date_text)
            except Exception as e:
                raise
                weather_data = str(e)

            return [SlotSet("matches", "{}".format(weather_data))]
