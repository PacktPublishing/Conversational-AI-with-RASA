## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## form
* weather OR weather{"address": "Shanghai"} OR weather{"date-time": "tomorrow"} OR weather{"date-time": "tomorrow", "address": "Shanghai"}
  - weather_form
  - form{"name": "weather_form"}
  - form{"name": null}

## chitchat
* chitchat
  - respond_chitchat

## form with unhappy path
* weather OR weather{"address": "Shanghai"} OR weather{"date-time": "tomorrow"} OR weather{"date-time": "tomorrow", "address": "Shanghai"}
  - weather_form
  - form{"name": "weather_form"}
* chitchat
  - respond_chitchat
  - weather_form
  - form{"name": null}
  
## form with stop then deny
* weather OR weather{"address": "Shanghai"} OR weather{"date-time": "tomorrow"} OR weather{"date-time": "tomorrow", "address": "Shanghai"}
  - weather_form
  - form{"name": "weather_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    
## form with stop then affirm
* weather OR weather{"address": "Shanghai"} OR weather{"date-time": "tomorrow"} OR weather{"date-time": "tomorrow", "address": "Shanghai"}
  - weather_form
  - form{"name": "weather_form"}
* stop
    - utter_ask_continue
* affirm
    - weather_form
    - form{"name": null}