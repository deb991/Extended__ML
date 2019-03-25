#!/usr/bin/env python -i
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

ds = pd.read_csv("D:\\PycharmProjects\\extended\\Machine_Learning\\fifa19\\data.csv")
print('\nData Set loaded')

print(ds.shape)

for cols in ds.columns:
    print(cols)
    print(ds.iloc[0, :])
    print(ds.loc[0:5, :])
    break

print((ds.loc[:5, ['Age', 'Acceleration']]))
print('\nEOP')

print(ds['Aggression'])
print(ds[['Age', 'Aggression', 'Acceleration']])

print('\nCreating/modifying new Pandas Series')
s1 = pd.Series([1, 2])
s2 = pd.Series(['Bob', 'Marley'])
print(s2)

print('\n Now creating A DataFrame\n')
df = pd.DataFrame([s1, s2])
print(df)

df1 = pd.DataFrame([[1, 2], ['Bob', 'Marley']], index=['Row1', 'Row2'], columns=['First__Name', 'Last__Name'])
print(df1)

df2 = pd.DataFrame(
    {'column1': [577, "Dad's home"],
     'column2': [3699, "Jey's home"]
     }
)

print(df2)

print(ds.corr( ))

#ds[ds["Age"] == "Acceleration"]["Value"].plot(kind="")

print(ds.loc[:5, ['Name', 'Age', 'Aggression', 'Acceleration']])


plt.plot([ds['Age'], ds['Acceleration'], ds['Aggression']], 'g^')
plt.ylabel('Y')
plt.xlabel('X')
#plt.show()


##matplotlib tutorials are provided

x = [(ds['Age'].max()), (ds['Acceleration'].max()), (ds['Aggression'].max())]
y = [(ds['Age'].min()), (ds['Acceleration'].min()), (ds['Aggression'].min())]

plt.plot(x, y, linewidth=5)

plt.title('Comparision between Age -- Acceleration -- Aggression')
plt.ylabel('Y -- Axis')
plt.xlabel('X -- Axis')

#plt.show()

plt.bar(x, y, align='center')

plt.title('Comparision between Age -- Acceleration -- Aggression')
plt.ylabel('Y -- Axis')
plt.xlabel('X -- Axis')

plt.show()
