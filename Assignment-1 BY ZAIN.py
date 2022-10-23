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

#Print the total number of students who have a three words name (first-middle-surname)
df[df['Name'].str.split(' ').str.len() == 3]['Name'].count()


#Those whose CGPA is more than pr equal to 3.0:
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

    
#CGPA of all male students on a histogram with intervals 2.0-2.5, 2.6-3.0, 3.1-3.5, 3.6-4.0
df = df.astype({'CGPA': 'float'})
zain = df['CGPA']
bins = [2.0,2.5,3.0,3.5,4.0]

plt.hist(zain, bins=bins, edgecolor='blue')
plt.show()

#Plot the favorite colors of male vs female students on a bar chart
(df['FavoriteColor'].str.strip().str).lower().value_counts().plot(kind='bar')


#Creating the correlation matrix between HSSC-1 and HSSC-2 marks and then plot on a heatmap chart:
df = df.astype({'HSSC-1': 'int','HSSC-2': 'int'})
correlational = df[['HSSC-1','HSSC-2']].corr()
sns.heatmap(correlational, annot=True)
plt.show()

