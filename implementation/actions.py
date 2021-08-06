# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World from my first action python code!")

         return []

class Actionsearchhospital(Action):

     def name(self) -> Text:
         return "action_search_hospital"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities = tracker.latest_message['entities']
         print (entities)
         for e in entities:
             if e['entity'] == "hospital":
                name = e['value']
             if name == "indian":
                message = "indian1,indian2,indian3,indian4,indian5"
             if name == "chinese":
                message = "chinese1,chinese2,chinese3,chinese4,chinese5"
             if name == "italian":
                message = "italian1,italian2,italian3,italian4,iltalian5"			
         dispatcher.utter_message(message)

         return []
		 
class Actioncoronatracker(Action):

     def name(self) -> Text:
         return "action_corona_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response = requests.get("https://api.covid19india.org/data.json").json()
         entities = tracker.latest_message['entities']
         print("last message now",entities)
         state = None
         for e in entities:
             if e['entity']	== "state":	
                state = e['value']
         message = "please enter correct state name"				
         for data in response["statewise"]:
             if data["state"] == state.title():
                print(data)
                message = "Active:"+data["active"] +"confirmed:" +data["confirmed"] +"recovered:" +data["recovered"] +"on:" +data["lastupdatedtime"]
                print(message)											 		 				 							  		 		 		 
         dispatcher.utter_message(message)

         return []