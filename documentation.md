# get_all_search fuction

# Packages for get_all_search function:

import requests<br/>
import requests_cache<br/>
import pandas as pd<br/>
import itertools<br/>
from bs4 import BeautifulSoup<br/>

import pandas as pd<br/>

import math<br/>

### parameters:

arguments:<br/>
      seller_type (str) - owner:cto, dealer:cto, all:cta<br/>
      search_key (str) - key word<br/>
      min_year (int) - minimum year<br/>
      max_year (int) - maximim year<br/>
      min_price (int) - minimum price<br/>
      max_price (int) - maximim price<br/>

returns: df (pd dataframe) - dataframe with title, price, location, mileage


# Clean Location Function

clean the location column, extract the location from messy string

### package:

import numpy as np
import re

### parameters:

arguments: location_list(list)

return: location_list (list)
