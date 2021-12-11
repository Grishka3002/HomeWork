import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

doc = open('C:\\Users\\Иван\\Downloads\\Titanic.csv','r+')

text = doc.read()

df = pd.read_csv('C:\\Users\\Иван\\Downloads\\Titanic.csv',index_col="PassengerId")
df.head()
df.to_csv("C:\\Users\\Иван\\Downloads\\Titanic.csv", encoding='utf-8')
print(df)