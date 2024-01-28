import re

# POSSIBLE ERROR TO BE ENCOUNTERED : when number of pages < max_pages (set max pages to the displayed number)
def create_list_of_urls_index(base_url):
    urls_list = []
    for page_num in range(42):
        new_url =re.sub(r'index=\d+',f'index={page_num*24:02}', base_url)
        urls_list.append(new_url)
    return(urls_list)







