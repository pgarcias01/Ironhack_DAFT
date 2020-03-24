from slugify import slugify
from bs4 import BeautifulSoup
import requests

def index_page(url):
    try:
        content = requests.get(url).content
        soup = BeautifulSoup(content)
        filename = slugify(soup.find('title').text)
        filename += '.html'
        f = open(filename, 'wb')
        f.write(content)
        f.close
    except:
        pass
