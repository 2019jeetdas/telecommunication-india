# -*- coding: utf-8 -*-

#-----(10-A) data analysis of Rural-Telephone-2002-2012 -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/No_Telephone_Lines_rural_during_2002-2012.csv',encoding="cp1252")
print("\n------- output data :-----------\n")
print("Rural telephone lines data analysis:")
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

# Question-0 --> Particulars

rural_BSNL = df['Particulars']
print("------------------------------")
print("\t Rural regions")
print("------------------------------")
for i in range(0,24):
    print(i,"---->",rural_BSNL[i])
print("------------------------------")

# 1 -->  3-2002
# 2 -->  3-2003
# 3 -->  3-2004
# 4 -->  3-2005
# 5 -->  3-2006
# 6 -->  3-2007

df_1 = df['2002'].replace(np.nan,0)
df_2 = df['2003'].replace(np.nan,0)
df_3 = df['2004'].replace(np.nan,0)
df_4 = df['2005'].replace(np.nan,0)
df_5 = df['2006'].replace(np.nan,0)
df_6 = df['2007'].replace(np.nan,0)

print("----------[2002]-------------------------")

for i in range(len(df_1)):
    print(i,"------->",int(df_1[i]))
    
print("-----------[2003]------------------------")
    
for i in range(len(df_2)):
    print(i,"------->",int(df_2[i]))

print("-------------[2004]----------------------")
    
for i in range(len(df_3)):
    print(i,"------->",int(df_3[i]))
    
print("-----------[2005]------------------------")
    
for i in range(len(df_4)):
    print(i,"------->",int(df_4[i]))
    
print("\n-------------[2006]----------------------\n")
    
for i in range(len(df_5)):
    print(i,"------->",int(df_5[i]))
    
print("\n-------------[2007]----------------------\n")
    
for i in range(len(df_6)):
    print(i,"------->",int(df_6[i]))
    
print("\n-----------[END]----------------\n")                                                            

plt.title('plot - 1 :Number of rural telephone lines in India [2002-2012]')
plt.xlabel("BSNL regions --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2002")

plt.plot(df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2003")

plt.plot(df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2004")
            
plt.plot(df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2005")
            
plt.plot(df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2006")
            
plt.plot(df_6,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="6 --> 2007")            
            
plt.legend()
plt.show()

    


# 7 -->  3-2008
# 8 -->  3-2009
# 9 -->  3-2010
# 10 -->  3-2011
# 11 -->  3-2012

df_7 = df['2008'].replace(np.nan,0)
df_8 = df['2009'].replace(np.nan,0)
df_9 = df['2010'].replace(np.nan,0)
df_10 = df['2011'].replace(np.nan,0)
df_11 = df['2012'].replace(np.nan,0)

print("----------[2008]-------------------------")

for i in range(len(df_7)):
    print(i,"------->",int(df_7[i]))
    
print("-----------[2009]------------------------")
    
for i in range(len(df_8)):
    print(i,"------->",int(df_8[i]))

print("-------------[2010]----------------------")
    
for i in range(len(df_9)):
    print(i,"------->",int(df_9[i]))
    
print("-----------[2011]------------------------")
    
for i in range(len(df_10)):
    print(i,"------->",int(df_10[i]))
    
print("\n-------------[2012]----------------------\n")
    
for i in range(len(df_11)):
    print(i,"------->",int(df_11[i]))
    
print("\n-----------[END]----------------\n")    

plt.title('plot - 2 :Number of rural telephone lines in India [2002-2012]')
plt.xlabel("BSNL regions --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_7,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2008")

plt.plot(df_8,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2009")

plt.plot(df_9,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2010")
            
plt.plot(df_10,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2011")
            
plt.plot(df_11,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2012")
            
plt.legend()
plt.show()
