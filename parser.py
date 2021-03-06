from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs


url = 'https://ru.citaty.net/tsitaty-o-zhenshchinakh/'


def get_citates_women():
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = 'https://ru.citaty.net/tsitaty-o-zhenshchinakh/'
    r = requests.get(url=url, headers=headers)

    soup = bs(r.text, 'lxml')

    links = soup.find_all('p', class_='blockquote-text')

    women_list = [i.find('a', title=True)['title'][17:] for i in links]

    return women_list

def get_citates_men():
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = 'https://ru.citaty.net/poisk/?h=%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B'
    url2 = 'https://ru.citaty.net/poisk/?h=%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B&page=2'
    url3 = 'https://ru.citaty.net/poisk/?h=%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B&page=3'
    r = requests.get(url=url, headers=headers)
    r2 = requests.get(url=url2, headers=headers)
    r3 = requests.get(url=url3, headers=headers)
    soup = bs(r.text, 'lxml')
    soup2 = bs(r2.text, 'lxml')
    soup3 = bs(r3.text, 'lxml')
    links = soup.find_all('p', class_='blockquote-text')
    links2 = soup2.find_all('p', class_='blockquote-text')
    links3 = soup3.find_all('p', class_='blockquote-text')
    men_list = [i.find('a', title=True)['title'][17:] for i in links]
    men_list2 = [i.find('a', title=True)['title'][17:] for i in links2]
    men_list3 = [i.find('a', title=True)['title'][17:] for i in links3]
    men_final_list = men_list+men_list2+men_list3

    return men_final_list



bot_hi = ['Гоп-стоп, мы подошли из-за угла.','Мне кажется или я где-то вас видел?','Какие планы на вечер?'
,'Привет, чуваки!','Как поживаешь, цыпленок?','Какие люди нарисовались!'
,'Давно не виделись, что я забыл черты твоего лица.','Случайно мы не знакомы?','Привет, собутыльники!'
,'Дай-ка я тебя расцелую.','Мое почтение!','Вот ты и попался!','Как и обещал. А вот и я!'
,'Ну, что? По кофейку или по пивасику?','Привет вашему дому.','Какая нечистая тебя притащила?'
,'Этот город недостаточно велик для нас двоих.','Однако, здравствуйте!','Здравия желаю!'
,'Слава КПСС!','Вау, все комплименты мира для тебя!','Как дела? Лови краба!','Ты прямо как ложка к обеду.'
,'Вечер в хату арестанты!','Ты где пропадал?','Несказанно рад тебя видеть!','Привет, солнце! Ты делаешь мой день ярче!'
,'Годы идут, а ты не меняешься!','Наша компания рада вас видеть!','Мир вашему дому!']