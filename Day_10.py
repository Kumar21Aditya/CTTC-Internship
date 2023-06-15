# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:52:37 2023

@author: Naina Sahu
"""

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data=pd.read_csv(r"F:\cttc\datasets\Churn_Modelling.csv")

#columns
data.columns

#disrtibution plot

sns.displot(data.CreditScore)
plt.show()

sns.kdeplot(data.CreditScore)
plt.show()


sns.displot(data.CreditScore[data.Exited==0])
sns.displot(data.CreditScore[data.Exited==1])
plt.show()

sns.displot(data.Tenure[data.Exited==0])
sns.displot(data.Tenure[data.Exited==1])
plt.show()

sns.displot(data.Age[data.Exited==0])
sns.displot(data.Age[data.Exited==1])
plt.show()

#count plot
sns.countplot(x=data.Geography)
plt.show()

sns.countplot(x=data.Geography[data.Exited==1])
plt.show()

sns.countplot(x=data.Geography[data.Exited==0])
plt.show()

sns.countplot(x=data.NumOfProducts,hue=data.Exited)
plt.show()

#boxplot
sns.boxplot(x=data.Geography, y= data.CreditScore)
plt.show()

sns.boxplot(x=data.Geography, y= data.CreditScore)
plt.show()

#pairplot
sns.pairplot(data)
plt.show()

data.corr()

#heatMap
plt.figure(figsize=(15,10))
co=data.corr()
sns.heatmap(co,annot=True)
plt.show()
