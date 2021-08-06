## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
 

## hello world path
* hello_world
  - action_hello_world

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## search hospital path
* search_hospital
  - action_search_hospital  

## corona tracker  path
* greet
  - utter_greet
* corona_case
  - utter_corona_case
* corona_state
  - action_corona_tracker

## corona path
* greet
  - utter_greet
* corona_intro
  - utter_corona_intro
* corona_spread
  - utter_corona_spread
* corona_food_spread
  - utter_corona_food_spread
* warm_weather
  - utter_warm_weather
* high_risk
  - utter_high_risk

