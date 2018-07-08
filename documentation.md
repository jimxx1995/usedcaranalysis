# Packages for get_all_search function:

import requests
import requests_cache
import pandas as pd
import itertools
from bs4 import BeautifulSoup

%matplotlib inline

import pandas as pd

import math

# parameters:

arguments:
      seller_type (str) - owner:cto, dealer:cto, all:cta
      search_key (str) - key word
      min_year (int) - minimum year
      max_year (int) - maximim year

returns: df (pd dataframe) - dataframe with title, price, location
