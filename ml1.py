#!/usr/bin/env python -i
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#ds = DS stands for data sets.

ds = pd.read_csv("C:\\Users\\DE635273\\PycharmProjects\\TG_proj\\datasets\\data.csv")
#ds2 = pd.read_csv("datasets\\data.csv")


#print(pd.DataFrame.equals(ds, ds2))
#print(ds.head(5))

#article = pd.read_csv("C:\\Users\\DE635273\\PycharmProjects\\TG_proj\\datasets\\data.csv", names=['Name', 'Nation', 'Age'])
#print(article)


print('Age  ::', ds['Age'].max())
print('Age  ::', ds['Age'].min())
