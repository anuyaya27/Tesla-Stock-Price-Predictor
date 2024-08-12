#Ananya Saxena
#Date: 10/08/2024
#Language: Python
#Data used: https://www.kaggle.com/code/meeratif/eda-tesla-stock-price/input

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_csv('C:/Users/LENOVO/Downloads/Tesla price data.csv')

data_set.shape

data_set.head()

data_set.info()

data_set.isnull().sum()

print("Columns are in Data_set", data_set.columns)

print("Average Open Share Price :- ", np.median(data_set['Open']))
print("Average Close Share Price :- ", np.median(data_set['Close']))

data_set['Open'].value_counts()
data_set['Close'].value_counts()

print(data_set['High'].value_counts().keys(), "\n", "\n", data_set['Low'].value_counts().keys())

print("Frequency of Share Volume :- \n", data_set['Volume'].value_counts())

#Plotting the graph for High and Low price of the stock

plt.figure(figsize=(15, 7))
sns.lineplot(data=data_set,x="Date",y="High",color="red",label="High")
sns.lineplot(data=data_set,x="Date",y="Low",color="blue",label="Low")
plt.show()

#Plotting the graph for Volume of the stock

plt.figure(figsize=(5,5))
plt.hist(list(data_set['Volume'].value_counts().keys()))
plt.title("Share Volume Graph")
plt.xlabel("Volume of Share")
plt.ylabel("Frequency")
plt.show()

#Plotting the graph for all values

bl_col = data_set.select_dtypes(include=('boolean'))

for i, col in enumerate(bl_col):
    plt.figure(i)
    sns.countplot(x=col, data=bl_col)

data_set.hist(figsize=(10, 10))
plt.show()

#All scatterplots
sns.pairplot(data_set)
plt.show()
