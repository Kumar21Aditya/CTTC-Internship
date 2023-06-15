# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:22:10 2023

@author: Naina Sahu
"""

import pandas as pd
import numpy as np
#Loading the dataset

df=pd.read_csv(r"F:\cttc\datasets\zomato.csv")
df
df.columns
df.head()
df.tail()
df.info()
df.shape
df.describe(include="all")
df.isnull().any()
df.isnull().sum()
df.duplicated().any()
df.columns         
df.drop(columns=['url', 'address',  'phone', 'dish_liked', 'reviews_list', 'menu_item', 'listed_in(city)'],inplace=True)
df.columns
df.columns=['Name','Online_order','Book_table','Rate','Votes','Location','Rest_type','Cuisines','Cost(2_people)','Category']
dup=df[df.duplicated()]
dup
dup.sum()

#dropping the duplictaed entries
df=df.drop_duplicates()

#Checking all duplicates are deleted
df[df.duplicated()].count()

# setting yes to 1 and no to 0
from sklearn.preprocessing import LabelEncoder
lb= LabelEncoder()
df['Online_order']= lb.fit_transform(df['Online_order'])
df['Book_table']= lb.fit_transform(df['Book_table'])

#Changing the rating value from fractional string value to float
df['Rate']=df.Rate.astype(str).apply(lambda x: x.split("/")[0])

#checking the top location of restraunts by checking the count
top_locations= df['Location'].value_counts(ascending = False)
df.isnull().sum()

#checking cost for 2 people
df['Cost(2_people)'].unique()
df['Cost(2_people)']= df['Cost(2_people)'].fillna(0)

# comma_remove function to remove comma from Cost(2_people)
def comma_remove(value):
    value= str(value)
    if ',' in value:
        value=value.replace(',','')
        return int(value)
    else:
        return int(value)
df['Cost(2_people)']=df['Cost(2_people)'].apply(comma_remove)
#Converting ['Cost(2_people)'] values to int and replaceing 
df['Cost(2_people)']= df['Cost(2_people)'].astype.int
df['Cost(2_people)'].mean()
df['Cost(2_people)'].replace(0,round(df['Cost(2_people)'].mean())).unique()
vf=round(df['Cost(2_people)'].mean())
vf
df.isnull().sum()
df.Online_order.unique()
df.Rate.unique()
df.Cuisines.unique()

df['Rate']=df['Rate'].replace("NEW",np.nan)
df['Rate']=df['Rate'].replace('_', np.nan)
df['Rate']=df['Rate'].replace('nan',np.nan)

df['Rate']=df['Rate'].fillna(0)
df['Rate'].unique

df.Cuisines.isnull()
df.Cuisines.nunique()
#Finding the mopst recurring cusinie  in given data
df['Cuisines'].mode()

#Replacing all the null values with the highest recurring cuisines
df['Cuisines'].fillna('North Indian', inplace=True)
df.Cuisines.isnull().sum()
df.isnull().sum()
df.Rest_type.unique()

'''MANY ENTRIES IN GIVEN DATA WERE REPETITIVE IN NATURE.
FOR EX-'Cafe Casual Dining' and 'Casual Dining, Cafe'.
THUS SPLITTING THEM TO COLLECT ONLY THE FIRST VALUE IN GIVEN STRING.'''

df["Rest_type"]=df.Rest_type.astype(str).apply(lambda x:x.split(",")[0])
df['Rest_type'].mode()

df['Rest_type'].fillna('Quick Bites',inplace =True)
df['Rest_type']

df['Rest_type']=df['Rest_type'].replace('nan','Quick Bites')
df.Rest_type.unique()
