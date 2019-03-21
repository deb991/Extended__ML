    
#!/usr/bin/env python -i
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ds = pd.read_csv("C:\\Users\\DE635273\\PycharmProjects\\TG_proj\\datasets\\data.csv")
print('\nData Set loaded')  

def dataSet_Ops():
    for col in ds.columns:
        print(col)
        column = pd.DataFrame([col])
        print('\Columns data types are as follows ::\t{}'.format(column.dtypes))
        
        
    print('\nFew basic operation can be included as per the requirement\nto extract data from data set')
    
def MaxMin():
    print('\nHeight comparision\n')
    max__age = ds['Age'].max()
    min__age = ds['Age'].min()
       
    #max__height = ds['Height'].max()
    #min__Height = ds['Height'].min()
    
    print('\nAcceleration comparision\n')
    max__Acceleration = ds['Acceleration'].max()
    min__Acceleration = ds['Acceleration'].min()



    print('\nMax Age ::\t{}, \nMin Age ::\t{}'.format(max__age, min__age))
    #print('\nMax Height ::\t{}, \nMin Height ::\t{}'.format(max__height, min__Height))
    print('\nMax Acceleration ::\t{}, \nMin Acceleration ::\t{}'.format(max__Acceleration, min__Acceleration))

    ##Simple PYPlot demo ##
    plt.plot([max__age, min__age, max__Acceleration, min__Acceleration], 'b--')
    plt.ylabel('Acceleration')
    plt.xlabel('Age')
    plt.show()
    
    ##Complex PyPlot demo##
    

dataSet_Ops()
#MaxMin()
print('\nEOF\n')
