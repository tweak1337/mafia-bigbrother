from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs
import urllib
import random

url = 'https://ru.citaty.net/tsitaty-o-zhenshchinakh/'

today = datetime.today().strftime('%y%m%d')
yesterday = (datetime.today() - timedelta(1)).strftime('%y%m%d')

old_memes = ['https://www.anekdot.ru/i/caricatures/normal/22/8/3/1659558544.png']

def get_meme():
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = f'https://www.anekdot.ru/last/mem/'
    url2 = 'https://www.anekdot.ru/last/mem/2'
    r = requests.get(url=url, headers=headers)
    r2 = requests.get(url=url2, headers=headers)

    soup = bs(r.text, 'lxml')
    soup2 = bs(r2.text, 'lxml')
    images = soup.findAll('img')
    images2 = soup2.findAll('img')

    list_of_memes1 = [i['src'] for i in images if 'lazy' in str(i)]
    list_of_memes2 = [i['src'] for i in images2 if 'lazy' in str(i)]
    list_of_memes = list_of_memes1 + list_of_memes2

    def generate_random():
        random_meme = random.choice(list_of_memes)

        if random_meme in old_memes:
            generate_random()
        else:
            old_memes.append(random_meme)
            urllib.request.urlretrieve(f'{random_meme}', 'my_image.jpg')

    generate_random()


bot_hi = ['Гоп-стоп, мы подошли из-за угла.','Мне кажется или я где-то вас видел?','Какие планы на вечер?'
,'Привет, чуваки!','Как поживаешь, цыпленок?','Какие люди нарисовались!'
,'Давно не виделись, что я забыл черты твоего лица.','Случайно мы не знакомы?','Привет, собутыльники!'
,'Дай-ка я тебя расцелую.','Мое почтение!','Вот ты и попался!','Как и обещал. А вот и я!'
,'Ну, что? По кофейку или по пивасику?','Привет вашему дому.','Какая нечистая тебя притащила?'
,'Этот город недостаточно велик для нас двоих.','Однако, здравствуйте!','Здравия желаю!'
,'Слава КПСС!','Вау, все комплименты мира для тебя!','Как дела? Лови краба!','Ты прямо как ложка к обеду.'
,'Вечер в хату арестанты!','Ты где пропадал?','Несказанно рад тебя видеть!','Привет, солнце! Ты делаешь мой день ярче!'
,'Годы идут, а ты не меняешься!','Наша компания рада вас видеть!','Мир вашему дому!']