from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT


class TicketFormAction(FormAction):
    def name(self) -> Text:
        return "action_ticket_form_submit"

    def run(
        self, dispatch: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        # don't using template alone,
        # since the system tracker is not updated yet when render the template,
        # using current tracker instead
        dispatch.utter_message(template="utter_ask_confirm", **tracker.slots)
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
