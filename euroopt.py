import requests
from bs4 import BeautifulSoup

URL = 'https://evroopt.by/redprice/vse-tovary/'


def get_data_euroopt(url=URL):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('img', attrs={'class': 'aligncenter'})
    return data
