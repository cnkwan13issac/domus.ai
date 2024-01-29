from os import environ as env
from dotenv import find_dotenv, load_dotenv
import requests

# Fetch data from the Google Maps Distance Matrix API
origin = input("Enter the location of the house: ")  
destination = input("Enter the location of your workplace or school: ")
mode = input("Which traveling mode do you prefer: ")  # Options: driving, walking, bicycling, transit

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
api_key = env.get("MAPS_API_KEY")

distanceMatrixAPI = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={destination}&origins={origin}&units=imperial&mode={mode}&key={api_key}"
distanceMatrixAPI_response = requests.get(distanceMatrixAPI)
result_DistanceMatrixAPI = distanceMatrixAPI_response.json()

distance = result_DistanceMatrixAPI["rows"][0]["elements"][0]["distance"]["text"]
duration = result_DistanceMatrixAPI["rows"][0]["elements"][0]["duration"]["text"]

print(f"Distance: {distance}")
print(f"Duration: {duration}")