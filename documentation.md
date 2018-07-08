# Packages for get_all_search function:

import requests<br/>
import requests_cache<br/>
import pandas as pd<br/>
import itertools<br/>
from bs4 import BeautifulSoup<br/>

import pandas as pd<br/>

import math<br/>

# parameters:

arguments:<br/>
      seller_type (str) - owner:cto, dealer:cto, all:cta<br/>
      search_key (str) - key word<br/>
      min_year (int) - minimum year<br/>
      max_year (int) - maximim year<br/>

returns: df (pd dataframe) - dataframe with title, price, location
