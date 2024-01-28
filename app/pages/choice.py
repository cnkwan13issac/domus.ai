import json
from dotenv import find_dotenv, load_dotenv
import pyperclip
import requests
from taipy.gui import notify, Markdown
from firebase_admin import firestore
import random
from os import environ as env

properties = None
formatted_places = "Default"

def on_init(state):
    print("on init (choice)")

    db = firestore.client()
    ref = db.collection("properties")
    state.properties = ref.get()
    print(len(state.properties), "properties loaded")


def on_navigate(state, page_name):
    # if page_name == "results" and not state.results_ready:
    #     return "no_results"
    # return page_name
    print("on_navigate")

myProperty = {
    "property_address": "Press any button to start!",
    "place_distance": "?",
    "place_duration": " ",
    "supermarket_distance": "?",
    "supermarket_duration": " ",
    "train_station_distance": "?",
    "train_station_duration": " ",
    "gym_distance": "?",
    "gym_duration": " ",
    "img_url_0": "app/static/img/royalhackerway.png",
    "property_id": None,
}

# <|Gym: {myProperty.gym}|>

# <|Supermarket: {myProperty.supermarket}|>

# <|Train Station: {myProperty.trainStation}|>

# <|Restaurant: {myProperty.restaurant}|>                           


# Definition of the page
choice_md = Markdown("""
<|container|

<br />

<|layout|class_name=d-flex top_layout|

<|app/static/img/logo-transparent.png|image|label=this is an image|width=30px|height=30px|> <|Domus.ai|text|class_name=big_font|>

[<|Logout|button|hover_text=View/Edit profile|class_name=secondary|>](/logout)

|>
                     
<br />



<|layout|columns=6 6|columns[mobile]=1|class_name=buttons_layout|

<|{myProperty.img_url_0}|image|label=this is an image|height=350px|width=500px|>

<second|
<|{myProperty.property_address}|text|class_name=big_font|>
                     
### Distance to your... 

Workplace: 
                     
<|{myProperty.place_distance}|text|> 
<|{myProperty.place_duration}|text|>

Supermarket:                 
<|{myProperty.supermarket_distance}|text|> 
<|{myProperty.supermarket_duration}|text|>
                     
Train Station:                 
<|{myProperty.train_station_distance}|text|> 
<|{myProperty.train_station_duration}|text|>

Gym:                 
<|{myProperty.gym_distance}|text|> 
<|{myProperty.gym_duration}|text|>                
|second>
                     
|>

<br />
                     
<|layout|columns=1 1|columns[mobile]=1 1|class_name=buttons_layout|

<|✗|button|hover_text=I hate this|on_action=add_to_dislikes|class_name=error bigbtn|>

<|✓|button|hover_text=I like this|on_action=add_to_likes|class_name=success bigbtn|>

|>

<br />
|>
""")


# <|+|button|hover_text=Add to saved|on_action=add_to_saved|class_name=secondary bigbtn|>

# My text: <|{text}|>

# <|{text}|input|>

# <|Run local|button|on_action=on_button_action|>
def generate_property(state,isLike):
    db = firestore.client()
    collection_ref = db.collection('users')
    if state.user == None: 
        token = json.loads(pyperclip.paste())
        
        query = collection_ref.where('email', '==', token["userinfo"]["email"])
        # Execute the query and retrieve the matching documents
        doc = query.get()[0]

        state.user = doc.to_dict()
    
    # query = collection_ref.where('email', '==', state.user.email)
    # doc = query.get()[0]
    # if state.myProperty.property_id != None:
    #     state.user.choices[state.myProperty.property_id] = isLike

    # doc.update({"choices": state.user.choices})

    myProperty =state.properties[random.randint(0,len(state.properties)-1)]

    state.myProperty = myProperty.to_dict()

    travellingModeTrans = {
        "Driving": "driving",
        "Walking": "walking",
        "Cycling": "bicycling",
        "Public Transport": "transit"
    }

    # Fetch data from the Google Maps Distance Matrix API
    origin = state.myProperty.property_address
    mode = travellingModeTrans[state.user.travellingMode]  # Options: driving, walking, bicycling, transit

    (place_distance, place_duration) = get_distance(origin,state.user.place,mode)
    (supermarket_distance, supermarket_duration) = nearest(origin,mode,"supermarket")
    (train_station_distance, train_station_duration) = nearest(origin,mode,"train_station")
    (gym_distance, gym_duration) = nearest(origin,mode,"gym")
    state.myProperty.place_distance = place_distance
    state.myProperty.place_duration = place_duration
    state.myProperty.supermarket_distance = supermarket_distance
    state.myProperty.supermarket_duration = supermarket_duration
    state.myProperty.train_station_distance = train_station_distance
    state.myProperty.train_station_duration = train_station_duration
    state.myProperty.gym_distance = gym_distance
    state.myProperty.gym_duration = gym_duration

   

def add_to_likes(state):
    generate_property(state,1)


def add_to_dislikes(state):
    generate_property(state,0)

def display_abouts(state):
    pass

def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"


def get_distance(destination, origin, mode):
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
        
    api_key = env.get("MAPS_API_KEY")

    distanceMatrixAPI = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={destination}&origins={origin}&units=imperial&mode={mode}&key={api_key}"

    # Make the API request
    distanceMatrixAPI_response = requests.get(distanceMatrixAPI)

    # Check if the request was successful
    # if distanceMatrixAPI.status_code == 200:
    result_DistanceMatrixAPI = distanceMatrixAPI_response.json()

    print(result_DistanceMatrixAPI)
        # Extract distance and duration
    distance = result_DistanceMatrixAPI["rows"][0]["elements"][0]["distance"]["text"]
    duration = result_DistanceMatrixAPI["rows"][0]["elements"][0]["duration"]["text"]

    return (distance, duration)

def nearest(origin, mode, types):
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
        
    api_key = env.get("MAPS_API_KEY")

    geocodeAPI = f"https://maps.googleapis.com/maps/api/geocode/json?address={origin}&key={api_key}"
    geocodeAPI_response = requests.get(geocodeAPI)
    geocodeAPI_dict = geocodeAPI_response.json() 

    if geocodeAPI_dict['status'] == 'OK':
        lat = float(geocodeAPI_dict['results'][0]['geometry']['location']['lat'])
        lng = float(geocodeAPI_dict['results'][0]['geometry']['location']['lng'])
    else:
        print(f"Error: {geocodeAPI_dict['status']}") 

    nearbySearchAPI = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type={types}&key={api_key}"
    nearbySearchAPI_response = requests.get(nearbySearchAPI)
    nearbySearchAPI_dict = nearbySearchAPI_response.json()

    first_result = nearbySearchAPI_dict["results"][0]
    first_lat = first_result["geometry"]["location"]["lat"]
    first_lng = first_result["geometry"]["location"]["lng"]

    distanceMatrixAPI = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={first_lat},{first_lng}&origins={origin}&units=imperial&mode={mode}&key={api_key}"
    distanceMatrixAPI_response = requests.get(distanceMatrixAPI)
    distanceMatrixAPI_dict = distanceMatrixAPI_response.json()
        
    distance = distanceMatrixAPI_dict["rows"][0]["elements"][0]["distance"]["text"]
    duration = distanceMatrixAPI_dict["rows"][0]["elements"][0]["duration"]["text"]
        
    return (distance, duration)