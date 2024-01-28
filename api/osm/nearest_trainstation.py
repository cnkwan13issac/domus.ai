from os import environ as env
from dotenv import find_dotenv, load_dotenv
import requests

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
api_key = env.get("MAPS_API_KEY")

origin = input("Enter the location of the house: ")  
mode = input("Which traveling mode do you prefer: ")  # Options: driving, walking, bicycling, transit

types = "train_station" 

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
    
print(distance) 
print(duration) 