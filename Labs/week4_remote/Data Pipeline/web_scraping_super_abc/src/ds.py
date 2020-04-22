import logging
from src.params import Params
import pandas as pd
import os
import concurrent.futures
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import re
import csv

params=Params()
f = open(params.product_links)
urls = list(csv.reader(f))
urls = [url[0] for url in urls]
urls = [url.split('https://') for url in urls]
URLS = ['https://' + site for url in urls for site in url if site != '']
URLS = list(set(URLS))
print(len(URLS))