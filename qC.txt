# -*- coding: utf-8 -*-

#-----(10-C) data analysis of Mobile connections-2002-2012 -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/mobile_connections.csv',encoding="cp1252")
print("\n------- output data :-----------\n")
print("Mobile connections (in million) as on 31.03.2018 :")
print("\n-----------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")


# Question-01 : Operators

df_1 = df['Operators']

print("---------------------------------------")
print("\t Mobile connection Operators")
print("---------------------------------------\n")

for i in range(0,len(df_1)):
    print(i,'---->',df_1[i])
    
print("---------------------------------------\n")

# Question - 02 : plotting operators vs. no.of mobile users

df_2 = df['Total mobile connections (in million) as on 31.03.2018'].replace(np.nan,0)

print("\n--------------------------------------------------")
print("mobile connections (in million) as on 31.03.2018")
print("-----------------------------------------------------\n")

for i in range(len(df_2)):
    print("[",i,"]",df_1[i],"------->",int(df_2[i]),'million\n')
    
print("-----------------------------------------------------\n")    

x = np.arange(0,12)

plt.title("Plot mobile connections (in million) as on 31.03.2018")
plt.xlabel("Operators sl. no. ---->")
plt.ylabel("Number of connections (in million)--->")
plt.plot(x,df_2)
plt.show()
