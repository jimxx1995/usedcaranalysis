
import numpy as np
import re

def clean_location(location_list):
    """ clean the location column, extract the location from messy string

    arguments: location_list(list)

    return: location_list (list)
    """
    for i, item in enumerate(location_list):
        location_list[i] = re.sub(r'[()]', "", location_list[i])
        if ">" in location_list[i]:
            location_list[i] = re.search(r'\w+\s\>\s(\w+[\s]*[\w+]*)', location_list[i]).group(1)
            location_list[i] = location_list[i].strip(' ')
        elif "," in location_list[i]:
            location_list[i] = re.split( r'[\,]', location_list[i])[0]
            location_list[i] = location_list[i].strip(' ')
        if 'sac' in location_list[i] or 'Sac' in location_list[i]:
            location_list[i] = 'Sacramento'
        location_list[i] = location_list[i].strip(' ')
        
    location_list = location_list.str.strip(' ')
    location_list = location_list.str.capitalize()

    return location_list
    
def clean_price(price_list):
    """ clean the price column, remove the "$" 

    arguments: price_list(list)

    return: price_list(list)
    """
    for i, item in enumerate(price_list):
        price_list[i] = price_list[i].replace("$","")
    price_list = price_list.astype(int)
    return price_list

