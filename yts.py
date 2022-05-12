import requests
from bs4 import BeautifulSoup

def yts():
    url = 'https://yts.mx'
    source_code = requests.get(url)
    plaint = source_code.text
    soup = BeautifulSoup(plaint)
    for link in soup.findall('a', {'class': 'item-name'}):
        href = link.get('href')
        print(href)

yts()