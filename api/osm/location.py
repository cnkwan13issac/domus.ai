# import requests

# api_key = # API

# # fetch data below from database later
# origin = input("Enter the location of the house: ") 
# destination = input("Enter the location of the school: ")  

# # URL for Nominatim API with the query parameters

# api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
# api_response_dict = api_response.json()


# url = 'https://nominatim.openstreetmap.org/search'
# params = {
#     'q': origin ,
#     'format': 'json',
#     'limit': 1,
# }

# r = requests.get(url, params=params)

# if r.status_code == 200:
#     result = r.json()

#     if result:
#         latitude = float(result[0]['boundingbox'][0])
#         longitude = float(result[0]['boundingbox'][2])


# location_house = input("Enter the location of the house: ") 
# location_destination = input("Enter the location of the destination: ")

# url = 'https://nominatim.openstreetmap.org/search'
# params = {
#     'h': location_house, 
#     'd': location_destination, 
#     'format': 'json',
#     'limit': 1,
# } 
    
# url = https://maps.googleapis.com/maps/api/directions/json?origin=Unity+Street+Bristol&destination=University+of+Bristol&key=AIzaSyBnt8OhlaPEu-Oez2I988OkpsrF9M_T728

#  # later fecth the details of location from database 
# origin = input("Enter the location of the house: ")  
# destination = input("Enter the location of the school: ") 


# url_fixed = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key)"

# url_variable = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={keyword}&location={lat}%{lng}&radius={radius}&type={type}&key={api_key}"

# address = "1600 Amphitheatre Parkway, Mountain View, CA"
# api_key = "<api key copied from google>"
# api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
# api_response_dict = api_response.json()

# if api_response_dict['status'] == 'OK':
#     latitude = api_response_dict['results'][0]['geometry']['location']['lat']
#     longitude = api_response_dict['results'][0]['geometry']['location']['lng']
#     print 'Latitude:', latitude
#     print 'Longitude:', longitude


# # # get origin and destination from database 
# # origin = input("Enter the location of the house: ") 
# # destination = input("Enter the location of the school: ")  

# # # if destination is specified (e.g. University of Cardiff)

# # # then: Google Directions API (find distance and communiting time) 

# # # else (if destination is unspecified) (e.g. Pub) 

# # # convert origin(house) to geolocation (lat and lng) 

# # # then: Google Places API (find nearby) 


# url = https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}

# import requests

# api_key = "AIzaSyBnt8OhlaPEu-Oez2I988OkpsrF9M_T728"

# origin = input("Enter the location of the house: ") 
# destination = input("Enter the location of the house: ") 
# radius = input("Enter the radius: ")

# url = 

# https://maps.googleapis.com/maps/api/place/nearbysearch/json
#   &location={lan}%{lng}
#   &radius={radius} 
#   &type=restaurant
#   &key=YOUR_API_KEY
###########################





# import requests

# api_key = "AIzaSyBnt8OhlaPEu-Oez2I988OkpsrF9M_T728"

# origin = input("Enter the location of the house: ") 
# destination = input("Enter the location of the house: ") 
# radius = input("Enter the radius: ")

# geocode_api = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(origin, api_key)).json() 

# if geocode_api['status'] == 'OK':
#     lat = geocode_api['results'][0]['geometry']['location']['lat']
#     lng = geocode_api['results'][0]['geometry']['location']['lng']
#     print ("Latitude:", lat)
#     print ("Longitude:", lng)

# nearby_search_api = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=cruise&location={lat}%{lng}&radius={radius}&type{type}=restaurant&key={api_key}"


    
# def check_destination(destination, place_types):
#     destination_words = destination.lower().split()
#     matching_types = [word for word in destination_words if word in place_types]
#     if matching_types:
#         return 
#     else: 
        

# with open("place_types.txt", "r") as file:
#         place_types = [line.strip() for line in file.readlines()]
#         return place_types
    
# # if matching_types:
# #     print(f"Matching place types: {matching_types}")

    
    
        


# # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=cruise&location={lat}%{lng}&radius={radius}&type=restaurant&key={api_key}"

# else:
#     print("Destination does not match any place type.")
    
# url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
 

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

# Make the API request
distanceMatrixAPI_response = requests.get(distanceMatrixAPI)

# Check if the request was successful
# if distanceMatrixAPI.status_code == 200:
result_DistanceMatrixAPI = distanceMatrixAPI_response.json()

    # Extract distance and duration
distance = result_DistanceMatrixAPI["rows"][0]["elements"][0]["distance"]["text"]
duration = result_DistanceMatrixAPI["rows"][0]["elements"][0]["duration"]["text"]

print(f"Distance: {distance}")
print(f"Duration: {duration}")

# else:
#     print(f"Error: {distanceMatrixAPI.status_code}")

# Find the nearest train station, supermarket and gym 
types = "supermarket|gym|train_station"
nearbysSearchAPI = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={origin}&radius=5000&type={types}&key={api_key}"
nearbysSearchAPI_response = requests.get(nearbysSearchAPI)
nearbysSearchAPI_results = nearbysSearchAPI_response.json()
places = nearbysSearchAPI_results.get('results', [])

places_coordinates = [(place['geometry']['location']['lat'], place['geometry']['location']['lng']) for place in places]

for coordinate in places_coordinates:
    near_destination = f"{coordinate[0]},{coordinate[1]}"
    distanceMatrixAPI = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={destination}&origins={origin}&units=imperial&mode={mode}&key={api_key}"
    distanceMatrixAPI_response = requests.get(distanceMatrixAPI)
    result_DistanceMatrixAPI = distanceMatrixAPI.json()
    
    distance = result_DistanceMatrixAPI["rows"][0]["elements"][0]["distance"]["text"]
    duration = result_DistanceMatrixAPI["rows"][0]["elements"][0]["duration"]["text"]
    
    place_type = ', '.join(place['types'])
    
    print(f"{place_type} at {destination}: Distance: {distance}, Duration: {duration}")

# geocodeAPI = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(origin, api_key))
# geocodeAPI_dict = geocodeAPI.json()

# if geocodeAPI ['status'] == 'OK':
#     lat = geocodeAPI ['results'][0]['geometry']['location']['lat']
#     lng = geocodeAPI ['results'][0]['geometry']['location']['lng']

# nearbySearchAPI_supermarket = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json&location={lat}%{lng}&radius=1500&type=supermarket&key={api_key}".json() 
# nearbySearchAPI_trainstation = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json&location={lat}%{lng}&radius=1500&type=train_station&key={api_key}".json() 
# nearbySearchAPI_gym = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json&location={lat}%{lng}&radius=1500&type=gym&key={api_key}".json() 

# nearbySearchAPI_supermarket_response = requests.get(nearbySearchAPI_supermarket)
# nearbySearchAPI_trainstation_response = requests.get(nearbySearchAPI_trainstation)
# nearbySearchAPI_gym_response = requests.get(nearbySearchAPI_gym)

# if distanceMatrixAPI.status_code == 200:
#     result_DistanceMatrixAPI = distanceMatrixAPI.json()

# # Closest train statin 

# # Closest gym 

 
# # Extract distance and duration
# distance = result_nearbySearchAPI_supermarket["rows"][0]["elements"][0]["distance"]["text"]
# duration = result_nearbySearchAPI_supermarket["rows"][0]["elements"][0]["duration"]["text"]

# print(f"Distance: {distance}")
# print(f"Duration: {duration}")
