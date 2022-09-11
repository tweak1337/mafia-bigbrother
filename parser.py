from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs
import urllib
import random
from fake_useragent import UserAgent
import replicate

ua = UserAgent()
model = replicate.models.get("stability-ai/stable-diffusion")

today = datetime.today().strftime('%y%m%d')
yesterday = (datetime.today() - timedelta(1)).strftime('%y%m%d')

old_memes = []

def get_meme():
    headers = {
        'user_agent': ua.chrome
    }
    url = f'https://www.anekdot.ru/last/mem_non_burning/'
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

    return list_of_memes

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


def get_meme_pikabu():
    headers = {
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
    }
    url = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353'
    url2 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=2'
    url3 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=3'
    url4 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=4'
    url5 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=5'
    url6 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=6'
    url7 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=7'
    url8 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=8'
    url9 = 'https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B,%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D1%81%D1%82&d=5346&D=5353&page=9'

    r = requests.get(url=url, headers=headers)
    r2 = requests.get(url=url2, headers=headers)
    r3 = requests.get(url=url3, headers=headers)
    r4 = requests.get(url=url4, headers=headers)
    r5 = requests.get(url=url5, headers=headers)
    r6 = requests.get(url=url6, headers=headers)
    r7 = requests.get(url=url7, headers=headers)
    r8 = requests.get(url=url8, headers=headers)
    r9 = requests.get(url=url9, headers=headers)

    soup = bs(r.text, 'lxml')
    soup2 = bs(r2.text, 'lxml')
    soup3 = bs(r3.text, 'lxml')
    soup4 = bs(r4.text, 'lxml')
    soup5 = bs(r5.text, 'lxml')
    soup6 = bs(r6.text, 'lxml')
    soup7 = bs(r6.text, 'lxml')
    soup8 = bs(r6.text, 'lxml')
    soup9 = bs(r6.text, 'lxml')

    images = soup.findAll('img')
    images2 = soup2.findAll('img')
    images3 = soup3.findAll('img')
    images4 = soup4.findAll('img')
    images5 = soup5.findAll('img')
    images6 = soup6.findAll('img')
    images7 = soup7.findAll('img')
    images8 = soup8.findAll('img')
    images9 = soup9.findAll('img')


    page1 = []
    for image in images:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page1.append(image['data-src'])
        except:
            pass

    page2 = []
    for image in images2:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page2.append(image['data-src'])
        except:
            pass

    page3 = []
    for image in images3:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page3.append(image['data-src'])
        except:
            pass

    page4 = []
    for image in images4:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page4.append(image['data-src'])
        except:
            pass

    page5 = []
    for image in images5:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page5.append(image['data-src'])
        except:
            pass

    page6 = []
    for image in images6:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page6.append(image['data-src'])
        except:
            pass

    page7 = []
    for image in images7:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page7.append(image['data-src'])
        except:
            pass

    page8 = []
    for image in images8:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page8.append(image['data-src'])
        except:
            pass

    page9 = []
    for image in images9:
        try:
            if 'post_img' in image['data-src'] and 'длиннопост' not in str(image).lower():
                page9.append(image['data-src'])
        except:
            pass

    list_of_memes = page1+page2+page3+page4+page5+page6+page7+page8+page9

    return list_of_memes
    # images = soup.findAll('img')
    # images2 = soup2.findAll('img')
    # images3 = soup3.findAll('img')


def whole_memes():

    list_of_memes = get_meme_pikabu()

    def generate_random():
        random_meme = random.choice(list_of_memes)

        if random_meme in old_memes:
            generate_random()
        else:
            old_memes.append(random_meme)
            urllib.request.urlretrieve(f'{random_meme}', 'my_image.jpg')

    generate_random()
    

def generate_picture(promt):
    output = model.predict(prompt=promt)
    output = output[0]
    p = requests.get(output)
    out = open("myimg.jpg", "wb")
    out.write(p.content)
    out.close()