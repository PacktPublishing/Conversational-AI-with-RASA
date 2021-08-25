from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher

from service.weather import get_text_weather_date
from service.normalization import text_to_date, text_to_coordinate


class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"

    def run(
        self, dispatch: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        city = tracker.get_slot("address")
        date_text = tracker.get_slot("date-time")

        date_object = text_to_date(date_text)

        if not date_object:  # parse date_time failed
            msg = "Not support weather query for {}".format([city, date_text])
            dispatch.utter_message(msg)
        else:
            dispatch.utter_message(templete="utter_working_on_it")
            try:
                lat, lon = text_to_coordinate(city)
                weather_data = get_text_weather_date(lat, lon, date_object, date_text, city)
            except Exception as e:
                exec_msg = str(e)
                dispatch.utter_message(exec_msg)
            else:
                dispatch.utter_message(weather_data)

        return []