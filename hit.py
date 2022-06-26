import requests
from bs4 import BeautifulSoup

URL = 'https://hitdiscount.by/flyer/'


def get_data_hit(url=URL):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    figure_tags = soup.find_all('figure', attrs={'class': 'redactor-keep-figure'})
    img_tags = [i.contents for i in figure_tags]
    return img_tags
