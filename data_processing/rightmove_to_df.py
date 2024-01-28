from scraper.rightmove.rightmove_scraper import *

base_url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E219&index=24&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords="

def dataframe_from_rightmove(baseurl):
    property_dataframe = main_rmscrape(base_url)



