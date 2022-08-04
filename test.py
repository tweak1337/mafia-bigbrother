import random
from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs
import urllib

today = datetime.today().strftime('%y%m%d')
yesterday = (datetime.today() - timedelta(1)).strftime('%y%m%d')


ll = 'as'
pp = ['as','sdw']

if ll in pp:
    print('awsda')