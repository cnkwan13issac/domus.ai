from bs4 import BeautifulSoup
import re
import requests

rightmove_html_class_id_dictionary = {"property_address":"_2uQQ3SV0eMHL1P6t5ZDo2q",
                                   "price_pcm":"_1gfnqJ3Vtd1z40MlC0MzXu",
                                   "property_description" : "STw8udCxUaBUMfOOZu0iL _3nPVwR0HZYQah5tkVJHFh5",
                                   "building_type":"_1hV1kqpVceE9m-QrX_hWDN",
                                   "count_bedrooms":"_1hV1kqpVceE9m-QrX_hWDN",
                                   "count_bathrooms":"_1hV1kqpVceE9m-QrX_hWDN",
                                   "property_size":"_1hV1kqpVceE9m-QrX_hWDN",
                                   "type_furnished":"_2RnXSVJcWbWv4IpBC1Sng6",
                                   "count_photos":"r62UN7T93Yr5BEGz48YBy"
                                   }
def extract_right_move_data(property_id, headers=None):
    # Instantiate the User Agent Headers for the Request if None Provided

    if headers is None:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
    # Make request to rightmove site @ the url of the property id
    response = requests.get("https://www.rightmove.co.uk/properties/" + str(property_id), headers=headers)
    if response.status_code == 200:

        # Create BeautifulSoup object for html parsing of repsonse from request
        soup = BeautifulSoup(response.content, 'html.parser')

        property_data_dict = {key: None for key in rightmove_html_class_id_dictionary}
        property_data_dict['property_id'] = property_id
        # Property Address Extraction
        address_element = soup.find(itemprop="streetAddress")
        if address_element:
            # Extract the street address
            street_address = address_element.get_text(strip=True)
            property_data_dict["property_address"] = street_address
        else:
            property_data_dict["property_address"] = None

        # Rental Price Extraction
        rental_price_element = soup.find('div', {'class': '_1gfnqJ3Vtd1z40MlC0MzXu'})
        if rental_price_element:

            rental_price_contents = rental_price_element.contents
            rental_price_stripped = rental_price_contents[0].get_text(strip=True)
            rental_price = re.sub(r'\D', '',rental_price_stripped)
            property_data_dict["price_pcm"] = rental_price
        else:
            # Handle cases where the address is not found
            property_data_dict["rentalPrice"] = None

        # Property Description Extraction
        property_description_element = soup.find('div', {'class': 'STw8udCxUaBUMfOOZu0iL _3nPVwR0HZYQah5tkVJHFh5'})

        if property_description_element:
            property_description = property_description_element.get_text(strip=True)
            property_data_dict["property_description"]=property_description
        else:
            property_data_dict["property_description"] = None

        # Building Type Shared ID Extraction (FOR THE SHARED CLASS IDs : THERE ARE NEARBY IDENTIFIERS IN THE TEXT

        # If not all 4 attributes on the list assign all as NONE
        shared_id_elements = soup.find_all('p', {'class': '_1hV1kqpVceE9m-QrX_hWDN'})
        if  len(shared_id_elements) < 4:
            property_data_dict["building_type"] = None
            property_data_dict["count_bedrooms"] = None
            property_data_dict["count_bathrooms"] = None
            property_data_dict["property_size"] = None
        else:
            property_data_dict["building_type"] = shared_id_elements[0].get_text(strip=True)
            property_data_dict["count_bedrooms"] = shared_id_elements[1].get_text(strip=True)
            property_data_dict["count_bathrooms"] = shared_id_elements[2].get_text(strip=True)
            property_data_dict["property_size"] = shared_id_elements[3].get_text(strip=True)


        count_photo_element = soup.find('span', {'class': "r62UN7T93Yr5BEGz48YBy"})

        if count_photo_element:
            property_data_dict["count_photos"] = count_photo_element.get_text(strip=True)
        else:
            property_data_dict["count_photos"] = None

        if property_data_dict.get("count_photos")!= 0:
            img_element = soup.find(attrs={'itemprop': 'contentUrl'})
            if img_element:
                url = img_element['content'] if 'content' in img_element.attrs else None
                #Common Pattern in IMG URL
                pattern = re.compile(r'(IMG_\d+)')
                match = pattern.search(url)
                if not match:
                    return []
                img_part = match.group(1)

                #Extract the number part from 'IMG_XX'
                number = int(img_part.split('_')[1])

                modified_urls = []
                for i in range(int(property_data_dict.get("count_photos"))):
                    new_number = f"{number + i:02}"

                    new_url = pattern.sub(f'IMG_{new_number}', url)
                    modified_urls.append(new_url)

                for n,url in enumerate(modified_urls):
                    property_data_dict[f"img_url_{n}"] = modified_urls[n]
            else:
                pass











        return property_data_dict
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")


'''
test_property_id = 144073706
test_feature_key = "property_description"

test_html_element = extract_html_element_by_key(test_feature_key,test_property_id)
print(test_html_element)


test_property_id = 144088709
property_data = extract_right_move_data(test_property_id)
print(property_data)
print(property_data.keys())
'''
