import requests
from bs4 import BeautifulSoup as BS
import re
from scraper.rightmove.searchpage.search_page_url_index_iterator import create_list_of_urls_index

def extract_property_ids_from_search_page(base_url, iterate=True):
    if iterate:
        property_ids_set = set()
        list_of_urls = create_list_of_urls_index(base_url)
        for url in list_of_urls:
            response = requests.get(url, headers={
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', })

            if response.status_code == 200:
                # Parse the content with BeautifulSoup
                soup = BS(response.content, 'html.parser')

                # Find all the div elements that have an id starting with 'property-'
                property_divs = soup.find_all('div', id=re.compile('^property-\d{9}$'))

                # Extract the numeric part of the ids and append to the list of property ids
                property_ids = [div['id'].split('-')[1] for div in property_divs]
                property_ids_set.update(property_ids)
            else:
                print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        property_ids_unique = list(property_ids_set)
        return property_ids_unique #return list(property_ids_set)
    else:
        response = requests.get(base_url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', })

        if response.status_code == 200:
            # Parse the content with BeautifulSoup
            soup = BS(response.content, 'html.parser')

            # Find all the div elements that have an id starting with 'property-'
            property_divs = soup.find_all('div', id=re.compile('^property-\d{9}$'))

            # Extract the numeric part of the ids and append to the property id lists
            property_ids = [div['id'].split('-')[1] for div in property_divs]
            return property_ids

        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")



