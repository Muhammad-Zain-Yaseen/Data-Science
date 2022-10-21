# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:47:12 2022

@author: zaucc
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Pattern no 1:
df = pd.read_csv(r'E:\Data Science\hello-dataset-fa22.csv')
print(df.Name)

#pattern no 2: to retreive the Desired Coloumn
dfp = pd.read_csv(r'E:\Data Science\hello-dataset-fa22.csv', usecols = ['Name'], low_memory = False)
print(dfp)

#with these methods we can retreive anything from our CSV file:
#Now Find Those people whose name starting with H
name = df[df.Name.str.contains('^H')]
print(name.Name)


# print the percentage of the students whose CGPA is above 3
dfp = pd.read_csv(r'E:\Data Science\hello-dataset-fa22.csv')
s= dfp.CGPA
print(s)

#dfp = dfp[(dfp['CGPA'] >= 3)]
#print(dfp.CGPA)
#print(dfp.CGPA.count())
#print(dfp.CGPA.count()/100)

#Plot the pie chart to show the ratio of Female and Male Students:
print(dfp.Gender)
dfm= dfp[(dfp['Gender'] =='Male')]
dff= dfp[(dfp['Gender'] =='Female')]
print(dfm.Gender)
print(dff.Gender)
a= dfm.Gender.count()
b= dff.Gender.count()
print(a)
print(b)
male= ['Male', 'female']
female= ['females']
numbers = [a, b]
plt.pie(numbers, labels= male)
plt.show()

    