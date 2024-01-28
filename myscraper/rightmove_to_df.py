from rightmove_scraper import *
import json

base_url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E219&index=24&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords="

# def dataframe_from_rightmove(baseurl):
property_dataframe = main_rmscrape(base_url)

# Specify the path and filename for the output JSON file
output_file_path = 'output.json'

# Open the file in write mode and write the dictionary as JSON
with open(output_file_path, 'w') as json_file:
    json.dump(property_dataframe, json_file)




