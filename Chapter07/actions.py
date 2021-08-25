from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class TicketFormAction(FormAction):
    def name(self) -> Text:
        return "action_ticket_form_submit"

    def run(
            self, dispatch: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict]:
        # print out all entities
        dispatch.utter_message("Entities: " + tracker.latest_message[
            'entities'] + "\n" + "Slots: " + tracker.slots)
        return []


class TicketQueryAction(Action):
    def name(self) -> Text:
        return "action_ticket_response"

    def run(self, dispatch, tracker, domain):
        entities = []
        for entity in tracker.latest_message['entities']:
            entities.append(
                {"entity": entity["entity"], "value": entity["value"],
                 "role": entity.get("role")})
        msg = str(entities) + "\n"

        dispatch.utter_message(msg)
        return []


class DrinkQueryAction(Action):
    def name(self) -> Text:
        return "action_drink_response"

    def run(self, dispatch, tracker,domain):
        # print out entities by group
        msg = ""

        entities = []
        for entity in tracker.latest_message['entities']:
            if entity.get("group") == "1":
                entities.append(
                    {"entity": entity["entity"], "value": entity["value"],
                     "group": entity["group"]})
        msg += "group #1: " + str(entities) + "\n"

        entities = []
        for entity in tracker.latest_message['entities']:
            if entity.get("group") == "2":
                entities.append(
                    {"entity": entity["entity"], "value": entity["value"],
                     "group": entity["group"]})
        msg += "group #2: " + str(entities)

        dispatch.utter_message(msg)
        return []


class ActionBuyTicket(Action):
    def name(self) -> Text:
        return "action_buy_ticket"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        arrive = tracker.get_slot("city_arrive")

        api_succeed = arrive == "北京"

        return [SlotSet("api_succeed", api_succeed)]
