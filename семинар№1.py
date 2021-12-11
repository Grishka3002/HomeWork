import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

url = "https://nplus1.ru/"
alls = []

page = requests.get(url)
text = page.text 

soup = BeautifulSoup(text, "lxml")

for a in soup.find_all('article', {"class":"item item-news item-news- _exist-image"}):
    link = url + a('a')[0].get('href')
    date = a('span')[0].get('title')
    page2 = requests.get(link)
    soup = BeautifulSoup(page2.text,"lxml")
    all_content = soup.find_all('article', {"class":"content"})
    for content in all_content:
        dif = content('span', {"class":"difficult-value"})[0].text
        rubrics = content('p', {"class":"table"})[0].text
        title = content('h1')[0].text
        text = content('p',{"class":None})
        author = text[len(text)-1].text
        text_container = content('p',{"class":None})
        texts = ""
        desc = None
        for i in range(0,len(text_container)-2):
            texts += text_container[i].text
    alls.append({'link':link, 'date':date, 'author':author, 'desc':desc, 'title':title, 'text':texts, 'rubric':rubrics.strip(), 'diff':[dif]})
    sleep(2)
df = pd.DataFrame(alls)
df.head()
df.to_csv("Семинар1.csv", encoding='utf-8', index=False)
