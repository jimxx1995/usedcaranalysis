import requests
import requests_cache
import pandas as pd
import itertools
from bs4 import BeautifulSoup

import pandas as pd

import math
import time

def get_all_search(seller_type, search_key, min_year, max_year):
    """ get info for all search

    arguments:
        seller_type (str) - owner:cto, dealer:cto, all:cta
        search_key (str) - key word
        min_year (int) - minimum year (optional) if not means all
        max_year (int) - maximim year (optional) if not means all

    returns: df (pd dataframe) - dataframe with title, price, location
    """

    def get_each_page(seller_type, page, search_key, min_year, max_year):
        """ get info for each page

        arguments: seller_type (str) - owner:cto, dealer:cto, all:cta
                    page (int) - page number

        return: title_list (list), price_list (list), location_list (list), page_num (int)
        """

        url = 'https://sfbay.craigslist.org/search/' + seller_type + '?s=' + str(page) + '&query=' + search_key + \
        '&min_auto_year=' + str(min_year) + '&max_auto_year=' + str(max_year)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('div', class_ = 'content')
        car_list = content[0].find_all('ul', class_ = 'rows')
        detail_list = car_list[0].find_all('li', class_ = 'result-row')

        #title
        title_list = [detail_list[i].find_all('a', class_ = "result-title hdrlnk")[0].text for i in range(len(detail_list))]

        #price
        price_text_list = [detail_list[i].find('span', class_ = 'result-price') for i in range(len(detail_list))]
        price_list = [i.text if i is not None else '' for i in price_text_list]

        #location
        location_text_list = [detail_list[i].find('span', class_ = 'result-hood') for i in range(len(detail_list))]
        location_list = []
        for i in range(len(location_text_list)):
            if location_text_list[i] is not None:
                location_list.append(location_text_list[i].text)
            elif detail_list[i].find('span', class_ = 'nearby') is not None:
                location_list.append(detail_list[i].find('span', class_ = 'nearby').text)
            else:
                location_list.append('')

        #page number
        posts_num = soup.find_all('span', class_ = 'totalcount')[0].text
        page_total = math.ceil(int(posts_num)/120)
        page_num = [i*120 for i in range(0,page_total)]

        return title_list, price_list, location_list, page_num

    page_num = get_each_page(seller_type, 0,search_key, min_year, max_year)[3]

    title_list = [get_each_page(seller_type, page, search_key, min_year, max_year)[0] for page in page_num]
    title_unlist = [j for i in title_list for j in i]

    price_list = [get_each_page(seller_type, page, search_key, min_year, max_year)[1] for page in page_num]
    price_unlist = [j for i in price_list for j in i]

    location_list = [get_each_page(seller_type, page, search_key, min_year, max_year)[2] for page in page_num]
    location_unlist = [j for i in location_list for j in i]

    df = pd.DataFrame({'title':title_unlist, 'price':price_unlist, 'location':location_unlist})

    return df
