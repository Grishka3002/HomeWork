import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://nplus1.ru/"
a = []
b = []
linkd = []

page = requests.get(url)
text = page.text 


soup = BeautifulSoup(text, "html.parser")
for link in soup.findAll('a'):
    a.append(link.get('href'))
for i in a:
    p = re.findall("/news.+", i)
    b.append(p)
for i in range(len(b)):
    if len(b[i]) != 0:
        linkd.append(b[i])
print(linkd)
