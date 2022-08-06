import random
from datetime import datetime, timedelta
import openpyxl
import requests
from bs4 import BeautifulSoup as bs
import urllib

today = datetime.today().strftime('%y%m%d')
yesterday = (datetime.today() - timedelta(1)).strftime('%y%m%d')


ll = 'as'
pp = ['ебучий','хуй']

str = 'я ебучий собак хуй'
strsplt = str.split()
counter = 0
for i in pp:
    for j in strsplt:
        if j == i:
            counter += 1

# if counter >0:
#     normative = ''
#     for count in range(counter):

for i in pp:
    for j in strsplt:
        if j == i:
            indx = strsplt.index(j)
            lenofwrd = len(strsplt[indx])
            stars = lenofwrd - 2
            strsplt[indx] = strsplt[indx][0] + ('*'*stars) + strsplt[indx][-1]
            print(strsplt)


print(strsplt)


z = []
print(len(z))

z[0] = 's'
z[2] = 'ss'

print(z)