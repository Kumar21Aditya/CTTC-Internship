# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:55:39 2023

@author: Naina Sahu
"""

import numpy as np

import matplotlib.pyplot as plt

x= np.linspace(0,10,50)
y= np.sin(x)

plt.xlabel("This is my x axis")
plt.ylabel("This is my y axis")
plt.title("This is my title")
plt.plot(x,y)

#Scatterplot
x=np.random.rand(50)
y=np.random.rand(50)
plt.xlabel("X - Data")
plt.ylabel("Y - Data")
plt.title("Scatter Plot")
plt.scatter(x,y)
plt.show()

colours=np.random.rand(50)
Size=1000*np.random.rand(50)
plt.scatter(x,y, c= colours,s=Size, alpha=.8)
plt.xlabel("X - Data")
plt.ylabel("Y - Data")

#barplot
x=['a','b','c','d']
y=np.random.rand(4)
plt.bar(x,y)
plt.xlabel("X - Data")
plt.ylabel("Y - Data")
plt.title("This is bar graph")

x=['a','b','c','d']
y=np.random.rand(4)
plt.barh(x,y)

plt.title("This is bar graph")

#grid
plt.figure(figsize=(6,4))
plt.plot(x,y)
plt.xlabel("X - Data")
plt.ylabel("Y - Data")
plt.grid()
plt.show()


x=np.random.rand(50)
y=np.random.rand(50)
colours=np.random.rand(50)
Size=1000*np.random.rand(50)
plt.scatter(x,y, c= colours,s=Size, alpha=.8, marker='v')
plt.xlabel("X - Data")
plt.ylabel("Y - Data")

data=[1,2,4,2,4,6,2,6,8,3,43,8,0,5,3,45,2,6,7,3,6,7]
plt.hist(data)
plt.show

x=[1,2,3,4,5]
y=[60,45,25,69,42]
colour=['red','pink','black','grey','blue']
plt.scatter(x,y,c=colour,s=150)
plt.show()

x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)

fig= plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()
