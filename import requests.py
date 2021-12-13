import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

doc = open('C:\\Users\\Иван\\Downloads\\Titanic.csv','r+')
PassengerId =[]
Survived = []
Pclass = []
Name = []
Sex = []
Age = []
SibSp = []
Parch = []
Ticket = []
Fare = []
Cabin = []
Embarked = []
count = 0
Passenger = []
index = []
c = 0
Type = []
count_sur = 0

text = doc.read()

df = pd.read_csv('C:\\Users\\Иван\\Downloads\\Titanic.csv',index_col="PassengerId")

with open("C:\\Users\\Иван\\Downloads\\Titanic.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            ", ".join(row)
        PassengerId.append(row["PassengerId"])
        Survived.append(row["Survived"])
        Pclass.append(row["Pclass"])
        Name.append(row["Name"])
        Sex.append(row["Sex"])
        Age.append(row["Age"])
        SibSp.append(row["SibSp"])
        Parch.append(row["Parch"])
        Ticket.append(row["Ticket"])
        Fare.append(row["Fare"])
        Cabin.append(row["Cabin"])
        Embarked.append(row["Embarked"])

for i in range(len(Survived)):
    if len(Survived[i]) != 0:
        count_sur += 1

#print(df['Survived'].value_counts()) 

alls = list(zip(Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked))       
for i in range(len(alls)):
    for j in range(len(alls[i])): 
          if len(alls[i][j]) == 0:
            index.append(i) 
            count += 1
            break
c = 0
for i in index:
    i = i - c 
    c += 1
    alls.pop(i)

Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked = zip(*alls)

for i in range(1,891-count+1):
    Passenger.append(i)

df = pd.DataFrame({'PassengerId':Passenger,'Survived': Survived, 'Pclass':Pclass, 'Name':Name, 'Sex':Sex, 'Age':Age, 'SibSp':SibSp, 'Parch':Parch, 'Ticket':Ticket, 'Fare':Fare, 'Cabin':Cabin, 'Embarked':Embarked})
df.to_csv("C:\\Users\\Иван\\Desktop\\Titanic.csv", encoding='utf-8', index = False)

c = 0
datatypes = df.dtypes 
for dtype in datatypes: 
    c += 1
    Type.append(dtype)
Name_col = ['PassengerId','Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin',' Embarked']
print(pd.DataFrame({"Name_col": Name_col, "Type": Type}))   

