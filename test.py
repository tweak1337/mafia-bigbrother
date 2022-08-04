import random
from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs
import urllib

today = datetime.today().strftime('%y%m%d')
yesterday = (datetime.today() - timedelta(1)).strftime('%y%m%d')


def get_meme():
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = f'https://www.anekdot.ru/last/mem/'
    r = requests.get(url=url, headers=headers)

    soup = bs(r.text, 'lxml')

    images = soup.findAll('img')

    list_of_memes = [i['src'] for i in images if 'lazy' in str(i)]
    print(list_of_memes)
    
    urllib.request.urlretrieve(f'{random.choice(list_of_memes)}', 'my_image.jpg')


get_meme()