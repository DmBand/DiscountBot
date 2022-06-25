import requests
from bs4 import BeautifulSoup

URL_RED_PRICE = 'https://evroopt.by/redprice/vse-tovary/'
URL_BLACKFRIDAY_PRICE = 'https://evroopt.by/deals/blackfriday/'


def _get_data(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('img', attrs={'class': 'aligncenter'})
    return data[:-1]


def get_red_price():
    return _get_data(url=URL_RED_PRICE)


def get_blackfriday_price():
    return _get_data(url=URL_BLACKFRIDAY_PRICE)
