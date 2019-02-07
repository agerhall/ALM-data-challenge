import numpy as np
import csv

# Method to load the csv data
def readData(filename):
    data=list()
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile) # create a csv reader object
        for row in reader:
            data.append(row[1]) # loop through the reader and add new fields to  the data
    data = data[1:]
    return data

Xtr0= readData('Xtr0.csv')
Ytr0 = readData('Ytr0.csv')

print(Xtr0)
'''
hypothesis methods:

# SVM with sequential kernel

# RNN

# LSTM

'''


