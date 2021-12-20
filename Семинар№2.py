import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot as plt

doc = open('C:\\Users\\Иван\\Downloads\\Titanic.csv','r+')

text = doc.read()

df = pd.read_csv('C:\\Users\\Иван\\Downloads\\Titanic.csv',index_col="PassengerId")

df = df.dropna(axis=0)
df.to_csv("Titanic-new.csv")

for name, val in df.iteritems():
    print(f"Colons {name}: Type={val.dtype}; кол-во={len(val)}")
for name, val in df.iteritems():
    if str(val.dtype) == "int64" or str(val.dtype) == "float64":
        print(df[name].describe())
        print('***')

ax = df["Age"].plot(kind="hist", color="red",title="Распределение возрастов", grid=True)
ax.set_xlabel("Age")
ax.set_ylabel("Freq")
plt.show()

df["Fare"].describe()

df.rename(columns={"Pclass" : "Class"}, inplace=True)
print(list(df))

female = df[df["Sex"] == "female"]
print(female["Sex"])

Ymale = df[(df["Sex"] == "male") & (df["Age"] < 32)]
print(Ymale["Age"])
print(Ymale["Sex"])

nobles = df[(df["Class"] == 1) | (df["Class"] == 2)]
nobles_alive = df[((df["Class"] == 1) | (df["Class"] == 2)) & (df["Survived"] == 1)]
print(nobles["Survived"])

female_column = df.rename(columns={"Sex":"Female"})["Female"]
female_column = female_column.apply(lambda x: 1 if x == 'female' else 0)
femaled_df = df.join(female_column)
print(femaled_df["Female"])

df = femaled_df

for val in df["Embarked"].unique():
    print(val)

group = df.groupby(df["Survived"])

for col in ['Age', 'SibSp', 'Parch', 'Fare']:
    print(group[col].mean())
    print("\n***")

group = df["Age"].groupby(df["Sex"])

(f_0, m_0) = group.mean()
(f_1, m_1) = group.median()

grouped_df = pd.DataFrame({"male" : [m_0, m_1], "female": [f_0, f_1]}, ["Среднее:", "Медианное:"])
print(grouped_df.to_string())

for col in list(df):
    df.rename(columns={col : col.lower()}, inplace=True)

print(list(df))

df.to_csv("Titanic-new.csv")