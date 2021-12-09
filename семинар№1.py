import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep

url = "https://nplus1.ru/"
a = []
b = []
linkd = []
time = []

page = requests.get(url)
text = page.text 


soup = BeautifulSoup(text, "html.parser")
for link in soup.findAll('a'):
    a.append(link.get('href'))
for i in a:
    p = re.findall("/news.+", i)
    b.append(p)
for i in b:
    if len(i) != 0:
        c = 'https://nplus1.ru'+''.join(i)
        page = requests.get(c)
        text = page.text
        soup = BeautifulSoup(text, "lxml")
        for i in soup.findAll('time'):
            time.append(i)
for i in time:
    #p = re.findall("\d{2}\s\w{3}\.\s\d{4}", i)
    print(i)