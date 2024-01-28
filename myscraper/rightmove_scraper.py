from search_page_url_index_iterator import create_list_of_urls_index
from property_id_scraper import extract_property_ids_from_search_page
from extract_property_data import extract_right_move_data

def main_rmscrape(base_url):

    '''
    Need to take base url as input - BASE URL DETERMINES REGION
    create list of urls for search pages
    creates list of property ids
    iterates extract_right_move_data function across list of property ids and create dictionaries for each property id into list
    returns list of dictionaries for the data for the properties
    '''

    property_id_list = extract_property_ids_from_search_page(base_url)
    list_of_property_data_dicts = [extract_right_move_data(property_id) for property_id in property_id_list]

    return list_of_property_data_dicts



