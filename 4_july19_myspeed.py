# -*- coding: utf-8 -*-
#-----(10-D) July19_myspeed -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/July19_myspeed.csv',encoding="cp1252")
print("\n------- output data :-----------\n")
print("July19_myspeed data analysis:")
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

# 0 --> Service_provider
# 1 --> technology
# 2 --> Download_Upload
# 3 --> Data_Speed.Kbps.
# 4 --> signal_strength
# 5 --> Service_Area

# print service providers 

service_provider = df.groupby(['Service_provider'])[['technology']].count()
print("--------------------------------------------")
print("\t Service provider names : ")
print("--------------------------------------------")
print(service_provider)
print("--------------------------------------------")
count = 0
for row in range(len(service_provider)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-------------------------------------------\n")

# available technologies

techno = df.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno)
print("-------------------------------")
count = 0
for row in range(len(techno)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n")

# service areas 

ser_area = df.groupby(['Service_Area'])[['signal_strength']].count()
print("---------------------------------")
print("\t Service areas : ")
print("-------------------------------")
count = 0
for i in range(0,len(ser_area)):
        print("--------------------------------------------")
        print("[",i+1,"]",ser_area[i:i+1]) 
        print("--------------------------------------------")
        count = count + 1
        
print("Total no. of service area = ",count)        
print("-----------------------------------------\n")



# [1] Andhra Pradesh

print("\n---: Andhra Pradesh operation :-------")
df_andhra = df[df.Service_Area == 'Andhra Pradesh']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_andhra.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_andhra.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in andhra pradesh

techno_andhra = df_andhra.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_andhra)
print("-------------------------------")
count = 0
for row in range(len(techno_andhra)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

# Andhra Pradesh 3G operation

print("\n---: convert to andhra-3G operation :-------")
df_andhra_3G = df_andhra[df_andhra.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_andhra_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_andhra_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in Andhra Pradesh 3G

df_andhra_3G_sp = df_andhra_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_andhra_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_andhra_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_andhra_3G_sp_AIRTEL
# df_andhra_3G_sp_CELLONE                 
# df_andhra_3G_sp_IDEA                     
# df_andhra_3G_sp_VODAFONE   

print("\n---: andhra-3G operation  :-------")

df_andhra_3G_AIRTEL = df_andhra_3G[df_andhra_3G.Service_provider == 'AIRTEL']
df_andhra_3G_CELLONE = df_andhra_3G[df_andhra_3G.Service_provider == 'CELLONE']
df_andhra_3G_IDEA = df_andhra_3G[df_andhra_3G.Service_provider == 'IDEA']
df_andhra_3G_VODAFONE = df_andhra_3G[df_andhra_3G.Service_provider == 'VODAFONE']

# [1-A] andhra pradesh 3G upload plotting

df_andhra_3G_AIRTEL_upload = df_andhra_3G_AIRTEL[df_andhra_3G_AIRTEL.Download_Upload == 'upload']
df_andhra_3G_CELLONE_upload = df_andhra_3G_CELLONE[df_andhra_3G_CELLONE.Download_Upload == 'upload']
df_andhra_3G_IDEA_upload = df_andhra_3G_IDEA[df_andhra_3G_IDEA.Download_Upload == 'upload']
df_andhra_3G_VODAFONE_upload = df_andhra_3G_VODAFONE[df_andhra_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_andhra_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_andhra_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_andhra_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_andhra_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A] andhra pradesh 3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_andhra_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_andhra_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_andhra_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_andhra_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B] andhra pradesh 3G download plotting

df_andhra_3G_AIRTEL_download = df_andhra_3G_AIRTEL[df_andhra_3G_AIRTEL.Download_Upload == 'download']
df_andhra_3G_CELLONE_download = df_andhra_3G_CELLONE[df_andhra_3G_CELLONE.Download_Upload == 'download']
df_andhra_3G_IDEA_download = df_andhra_3G_IDEA[df_andhra_3G_IDEA.Download_Upload == 'download']
df_andhra_3G_VODAFONE_download = df_andhra_3G_VODAFONE[df_andhra_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_andhra_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_andhra_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_andhra_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_andhra_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B] andhra pradesh 3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_andhra_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_andhra_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_andhra_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_andhra_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

# Andhra Pradesh 4G operation

print("\n---: convert to andhra-4G operation :-------")
df_andhra_4G = df_andhra[df_andhra.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_andhra_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_andhra_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in Andhra Pradesh 4G

df_andhra_4G_sp = df_andhra_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_andhra_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_andhra_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_andhra_4G_sp_AIRTEL
# df_andhra_4G_sp_CELLONE                 
# df_andhra_4G_sp_IDEA                     
# df_andhra_4G_sp_VODAFONE   
# df_andhra_4G_sp_JIO

print("\n---: andhra-4G operation  :-------")

df_andhra_4G_AIRTEL = df_andhra_4G[df_andhra_4G.Service_provider == 'AIRTEL']
df_andhra_4G_CELLONE = df_andhra_4G[df_andhra_4G.Service_provider == 'CELLONE']
df_andhra_4G_IDEA = df_andhra_4G[df_andhra_4G.Service_provider == 'IDEA']
df_andhra_4G_VODAFONE = df_andhra_4G[df_andhra_4G.Service_provider == 'VODAFONE']
df_andhra_4G_JIO = df_andhra_4G[df_andhra_4G.Service_provider == 'JIO']

# andhra pradesh 4G upload plotting

df_andhra_4G_AIRTEL_upload = df_andhra_4G_AIRTEL[df_andhra_4G_AIRTEL.Download_Upload == 'upload']
df_andhra_4G_CELLONE_upload = df_andhra_4G_CELLONE[df_andhra_4G_CELLONE.Download_Upload == 'upload']
df_andhra_4G_IDEA_upload = df_andhra_4G_IDEA[df_andhra_4G_IDEA.Download_Upload == 'upload']
df_andhra_4G_VODAFONE_upload = df_andhra_4G_VODAFONE[df_andhra_4G_VODAFONE.Download_Upload == 'upload']
df_andhra_4G_JIO_upload = df_andhra_4G_JIO[df_andhra_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_andhra_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_andhra_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_andhra_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_andhra_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_andhra_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C] andhra pradesh 4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_andhra_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_andhra_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_andhra_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_andhra_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_andhra_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


# andhra pradesh 4G download plotting
                                                                                                                                                          
df_andhra_4G_AIRTEL_download = df_andhra_4G_AIRTEL[df_andhra_4G_AIRTEL.Download_Upload == 'download']
df_andhra_4G_CELLONE_download = df_andhra_4G_CELLONE[df_andhra_4G_CELLONE.Download_Upload == 'download']
df_andhra_4G_IDEA_download = df_andhra_4G_IDEA[df_andhra_4G_IDEA.Download_Upload == 'download']
df_andhra_4G_VODAFONE_download = df_andhra_4G_VODAFONE[df_andhra_4G_VODAFONE.Download_Upload == 'download']
df_andhra_4G_JIO_download = df_andhra_4G_JIO[df_andhra_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_andhra_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_andhra_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_andhra_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_andhra_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_andhra_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D] andhra pradesh 4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_andhra_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_andhra_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_andhra_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_andhra_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_andhra_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                                                     
                                                                                              
# [2] Assam 


print("\n---: [2] Assam operation :-------")
df_assam = df[df.Service_Area == 'Assam']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_assam.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_assam.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in assam 

techno_assam = df_assam.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_assam)
print("-------------------------------")
count = 0
for row in range(len(techno_assam)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

# Assam 3G operation

print("\n---: convert to assam-3G operation :-------")
df_assam_3G = df_assam[df_assam.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_assam_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_assam_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in Assam 3G

df_assam_3G_sp = df_assam_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_assam_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_assam_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_assam_3G_sp_AIRTEL
# df_assam_3G_sp_CELLONE                 
# df_assam_3G_sp_IDEA                     
# df_assam_3G_sp_VODAFONE   

print("\n---: assam-3G operation  :-------")

df_assam_3G_AIRTEL = df_assam_3G[df_assam_3G.Service_provider == 'AIRTEL']
df_assam_3G_CELLONE = df_assam_3G[df_assam_3G.Service_provider == 'CELLONE']
df_assam_3G_IDEA = df_assam_3G[df_assam_3G.Service_provider == 'IDEA']
df_assam_3G_VODAFONE = df_assam_3G[df_assam_3G.Service_provider == 'VODAFONE']

# [1-A] assam  3G upload plotting

df_assam_3G_AIRTEL_upload = df_assam_3G_AIRTEL[df_assam_3G_AIRTEL.Download_Upload == 'upload']
df_assam_3G_CELLONE_upload = df_assam_3G_CELLONE[df_assam_3G_CELLONE.Download_Upload == 'upload']
df_assam_3G_IDEA_upload = df_assam_3G_IDEA[df_assam_3G_IDEA.Download_Upload == 'upload']
df_assam_3G_VODAFONE_upload = df_assam_3G_VODAFONE[df_assam_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_assam_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_assam_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_assam_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_assam_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A] assam  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_assam_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_assam_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_assam_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_assam_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B] assam  3G download plotting

                                                                                                                                                          
df_assam_3G_AIRTEL_download = df_assam_3G_AIRTEL[df_assam_3G_AIRTEL.Download_Upload == 'download']
df_assam_3G_CELLONE_download = df_assam_3G_CELLONE[df_assam_3G_CELLONE.Download_Upload == 'download']
df_assam_3G_IDEA_download = df_assam_3G_IDEA[df_assam_3G_IDEA.Download_Upload == 'download']
df_assam_3G_VODAFONE_download = df_assam_3G_VODAFONE[df_assam_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_assam_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_assam_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_assam_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_assam_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B] assam  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_assam_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_assam_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_assam_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_assam_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

# Andhra Pradesh 4G operation

print("\n---: convert to assam-4G operation :-------")
df_assam_4G = df_assam[df_assam.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_assam_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_assam_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in Assam 4G

df_assam_4G_sp = df_assam_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_assam_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_assam_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_assam_4G_sp_AIRTEL
# df_assam_4G_sp_CELLONE                 
# df_assam_4G_sp_IDEA                     
# df_assam_4G_sp_VODAFONE 
# df_assam_4G_sp_JIO  

print("\n---: assam-4G operation  :-------")

df_assam_4G_AIRTEL = df_assam_4G[df_assam_4G.Service_provider == 'AIRTEL']
df_assam_4G_CELLONE = df_assam_4G[df_assam_4G.Service_provider == 'CELLONE']
df_assam_4G_IDEA = df_assam_4G[df_assam_4G.Service_provider == 'IDEA']
df_assam_4G_VODAFONE = df_assam_4G[df_assam_4G.Service_provider == 'VODAFONE']
df_assam_4G_JIO = df_assam_4G[df_assam_4G.Service_provider == 'JIO']

# assam  4G upload plotting

df_assam_4G_AIRTEL_upload = df_assam_4G_AIRTEL[df_assam_4G_AIRTEL.Download_Upload == 'upload']
df_assam_4G_CELLONE_upload = df_assam_4G_CELLONE[df_assam_4G_CELLONE.Download_Upload == 'upload']
df_assam_4G_IDEA_upload = df_assam_4G_IDEA[df_assam_4G_IDEA.Download_Upload == 'upload']
df_assam_4G_VODAFONE_upload = df_assam_4G_VODAFONE[df_assam_4G_VODAFONE.Download_Upload == 'upload']
df_assam_4G_JIO_upload = df_assam_4G_JIO[df_assam_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_assam_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_assam_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_assam_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_assam_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_assam_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C] assam  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_assam_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_assam_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_assam_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_assam_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_assam_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


# assam  4G download plotting
                                                                                                                                                          
df_assam_4G_AIRTEL_download = df_assam_4G_AIRTEL[df_assam_4G_AIRTEL.Download_Upload == 'download']
df_assam_4G_CELLONE_download = df_assam_4G_CELLONE[df_assam_4G_CELLONE.Download_Upload == 'download']
df_assam_4G_IDEA_download = df_assam_4G_IDEA[df_assam_4G_IDEA.Download_Upload == 'download']
df_assam_4G_VODAFONE_download = df_assam_4G_VODAFONE[df_assam_4G_VODAFONE.Download_Upload == 'download']
df_assam_4G_JIO_download = df_assam_4G_JIO[df_assam_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_assam_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_assam_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_assam_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_assam_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_assam_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D] assam  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_assam_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_assam_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_assam_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_assam_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_assam_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                             
                                                                     


# [3]  Bihar 


print("\n---: [3]  Bihar operation :-------")
df_bihar = df[df.Service_Area == 'Bihar']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_bihar.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_bihar.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  bihar 

techno_bihar = df_bihar.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_bihar)
print("-------------------------------")
count = 0
for row in range(len(techno_bihar)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Bihar 3G operation

print("\n---: convert to  bihar-3G operation :-------")
df_bihar_3G = df_bihar[df_bihar.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_bihar_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_bihar_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Bihar 3G

df_bihar_3G_sp = df_bihar_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_bihar_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_bihar_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_bihar_3G_sp_AIRTEL
# df_bihar_3G_sp_CELLONE                 
# df_bihar_3G_sp_IDEA                     
# df_bihar_3G_sp_VODAFONE   

print("\n---:  bihar-3G operation  :-------")

df_bihar_3G_AIRTEL = df_bihar_3G[df_bihar_3G.Service_provider == 'AIRTEL']
df_bihar_3G_CELLONE = df_bihar_3G[df_bihar_3G.Service_provider == 'CELLONE']
df_bihar_3G_IDEA = df_bihar_3G[df_bihar_3G.Service_provider == 'IDEA']
df_bihar_3G_VODAFONE = df_bihar_3G[df_bihar_3G.Service_provider == 'VODAFONE']

# [1-A]  bihar  3G upload plotting

df_bihar_3G_AIRTEL_upload = df_bihar_3G_AIRTEL[df_bihar_3G_AIRTEL.Download_Upload == 'upload']
df_bihar_3G_CELLONE_upload = df_bihar_3G_CELLONE[df_bihar_3G_CELLONE.Download_Upload == 'upload']
df_bihar_3G_IDEA_upload = df_bihar_3G_IDEA[df_bihar_3G_IDEA.Download_Upload == 'upload']
df_bihar_3G_VODAFONE_upload = df_bihar_3G_VODAFONE[df_bihar_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_bihar_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_bihar_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_bihar_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_bihar_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  bihar  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_bihar_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_bihar_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_bihar_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_bihar_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  bihar  3G download plotting

                                                                                                                                                          
df_bihar_3G_AIRTEL_download = df_bihar_3G_AIRTEL[df_bihar_3G_AIRTEL.Download_Upload == 'download']
df_bihar_3G_CELLONE_download = df_bihar_3G_CELLONE[df_bihar_3G_CELLONE.Download_Upload == 'download']
df_bihar_3G_IDEA_download = df_bihar_3G_IDEA[df_bihar_3G_IDEA.Download_Upload == 'download']
df_bihar_3G_VODAFONE_download = df_bihar_3G_VODAFONE[df_bihar_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_bihar_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_bihar_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_bihar_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_bihar_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  bihar  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_bihar_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_bihar_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_bihar_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_bihar_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  bihar 4G operation

print("\n---: convert to  bihar-4G operation :-------")
df_bihar_4G = df_bihar[df_bihar.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_bihar_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_bihar_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Bihar 4G

df_bihar_4G_sp = df_bihar_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_bihar_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_bihar_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_bihar_4G_sp_AIRTEL
# df_bihar_4G_sp_CELLONE                 
# df_bihar_4G_sp_IDEA                     
# df_bihar_4G_sp_VODAFONE 
# df_bihar_4G_sp_JIO  

print("\n---:  bihar-4G operation  :-------")

df_bihar_4G_AIRTEL = df_bihar_4G[df_bihar_4G.Service_provider == 'AIRTEL']
df_bihar_4G_CELLONE = df_bihar_4G[df_bihar_4G.Service_provider == 'CELLONE']
df_bihar_4G_IDEA = df_bihar_4G[df_bihar_4G.Service_provider == 'IDEA']
df_bihar_4G_VODAFONE = df_bihar_4G[df_bihar_4G.Service_provider == 'VODAFONE']
df_bihar_4G_JIO = df_bihar_4G[df_bihar_4G.Service_provider == 'JIO']

#  bihar  4G upload plotting

df_bihar_4G_AIRTEL_upload = df_bihar_4G_AIRTEL[df_bihar_4G_AIRTEL.Download_Upload == 'upload']
df_bihar_4G_CELLONE_upload = df_bihar_4G_CELLONE[df_bihar_4G_CELLONE.Download_Upload == 'upload']
df_bihar_4G_IDEA_upload = df_bihar_4G_IDEA[df_bihar_4G_IDEA.Download_Upload == 'upload']
df_bihar_4G_VODAFONE_upload = df_bihar_4G_VODAFONE[df_bihar_4G_VODAFONE.Download_Upload == 'upload']
df_bihar_4G_JIO_upload = df_bihar_4G_JIO[df_bihar_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_bihar_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_bihar_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_bihar_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_bihar_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_bihar_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  bihar  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_bihar_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_bihar_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_bihar_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_bihar_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_bihar_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  bihar  4G download plotting
                                                                                                                                                          
df_bihar_4G_AIRTEL_download = df_bihar_4G_AIRTEL[df_bihar_4G_AIRTEL.Download_Upload == 'download']
df_bihar_4G_CELLONE_download = df_bihar_4G_CELLONE[df_bihar_4G_CELLONE.Download_Upload == 'download']
df_bihar_4G_IDEA_download = df_bihar_4G_IDEA[df_bihar_4G_IDEA.Download_Upload == 'download']
df_bihar_4G_VODAFONE_download = df_bihar_4G_VODAFONE[df_bihar_4G_VODAFONE.Download_Upload == 'download']
df_bihar_4G_JIO_download = df_bihar_4G_JIO[df_bihar_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_bihar_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_bihar_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_bihar_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_bihar_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_bihar_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  bihar  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_bihar_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_bihar_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_bihar_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_bihar_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_bihar_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                                 
                                                                  
# [4] Chennai  

# [4] Chennai


print("\n---: [4]  chennai operation :-------")
df_chennai = df[df.Service_Area == 'Chennai']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_chennai.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_chennai.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  chennai 

techno_chennai = df_chennai.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_chennai)
print("-------------------------------")
count = 0
for row in range(len(techno_chennai)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Bihar 3G operation

print("\n---: convert to  chennai-3G operation :-------")
df_chennai_3G = df_chennai[df_chennai.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_chennai_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_chennai_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Bihar 3G

df_chennai_3G_sp = df_chennai_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_chennai_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_chennai_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_chennai_3G_sp_AIRTEL
# df_chennai_3G_sp_CELLONE                 
# df_chennai_3G_sp_IDEA                     
# df_chennai_3G_sp_VODAFONE   

print("\n---:  chennai-3G operation  :-------")

df_chennai_3G_AIRTEL = df_chennai_3G[df_chennai_3G.Service_provider == 'AIRTEL']
df_chennai_3G_CELLONE = df_chennai_3G[df_chennai_3G.Service_provider == 'CELLONE']
df_chennai_3G_IDEA = df_chennai_3G[df_chennai_3G.Service_provider == 'IDEA']
df_chennai_3G_VODAFONE = df_chennai_3G[df_chennai_3G.Service_provider == 'VODAFONE']

# [1-A]  chennai  3G upload plotting

df_chennai_3G_AIRTEL_upload = df_chennai_3G_AIRTEL[df_chennai_3G_AIRTEL.Download_Upload == 'upload']
df_chennai_3G_CELLONE_upload = df_chennai_3G_CELLONE[df_chennai_3G_CELLONE.Download_Upload == 'upload']
df_chennai_3G_IDEA_upload = df_chennai_3G_IDEA[df_chennai_3G_IDEA.Download_Upload == 'upload']
df_chennai_3G_VODAFONE_upload = df_chennai_3G_VODAFONE[df_chennai_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_chennai_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_chennai_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_chennai_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_chennai_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  chennai  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_chennai_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_chennai_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_chennai_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_chennai_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  chennai  3G download plotting

                                                                                                                                                          
df_chennai_3G_AIRTEL_download = df_chennai_3G_AIRTEL[df_chennai_3G_AIRTEL.Download_Upload == 'download']
df_chennai_3G_CELLONE_download = df_chennai_3G_CELLONE[df_chennai_3G_CELLONE.Download_Upload == 'download']
df_chennai_3G_IDEA_download = df_chennai_3G_IDEA[df_chennai_3G_IDEA.Download_Upload == 'download']
df_chennai_3G_VODAFONE_download = df_chennai_3G_VODAFONE[df_chennai_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_chennai_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_chennai_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_chennai_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_chennai_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  chennai  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_chennai_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_chennai_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_chennai_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_chennai_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  chennai 4G operation

print("\n---: convert to  chennai-4G operation :-------")
df_chennai_4G = df_chennai[df_chennai.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_chennai_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_chennai_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Bihar 4G

df_chennai_4G_sp = df_chennai_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names in Andhra Pradesh : ")
print("-------------------------------")
print(df_chennai_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_chennai_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_chennai_4G_sp_AIRTEL
# df_chennai_4G_sp_CELLONE                 
# df_chennai_4G_sp_IDEA                     
# df_chennai_4G_sp_VODAFONE 
# df_chennai_4G_sp_JIO  

print("\n---:  chennai-4G operation  :-------")

df_chennai_4G_AIRTEL = df_chennai_4G[df_chennai_4G.Service_provider == 'AIRTEL']
df_chennai_4G_CELLONE = df_chennai_4G[df_chennai_4G.Service_provider == 'CELLONE']
df_chennai_4G_IDEA = df_chennai_4G[df_chennai_4G.Service_provider == 'IDEA']
df_chennai_4G_VODAFONE = df_chennai_4G[df_chennai_4G.Service_provider == 'VODAFONE']
df_chennai_4G_JIO = df_chennai_4G[df_chennai_4G.Service_provider == 'JIO']

#  chennai  4G upload plotting

df_chennai_4G_AIRTEL_upload = df_chennai_4G_AIRTEL[df_chennai_4G_AIRTEL.Download_Upload == 'upload']
df_chennai_4G_CELLONE_upload = df_chennai_4G_CELLONE[df_chennai_4G_CELLONE.Download_Upload == 'upload']
df_chennai_4G_IDEA_upload = df_chennai_4G_IDEA[df_chennai_4G_IDEA.Download_Upload == 'upload']
df_chennai_4G_VODAFONE_upload = df_chennai_4G_VODAFONE[df_chennai_4G_VODAFONE.Download_Upload == 'upload']
df_chennai_4G_JIO_upload = df_chennai_4G_JIO[df_chennai_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_chennai_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_chennai_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_chennai_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_chennai_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_chennai_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  chennai  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_chennai_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_chennai_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_chennai_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_chennai_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_chennai_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  chennai  4G download plotting
                                                                                                                                                          
df_chennai_4G_AIRTEL_download = df_chennai_4G_AIRTEL[df_chennai_4G_AIRTEL.Download_Upload == 'download']
df_chennai_4G_CELLONE_download = df_chennai_4G_CELLONE[df_chennai_4G_CELLONE.Download_Upload == 'download']
df_chennai_4G_IDEA_download = df_chennai_4G_IDEA[df_chennai_4G_IDEA.Download_Upload == 'download']
df_chennai_4G_VODAFONE_download = df_chennai_4G_VODAFONE[df_chennai_4G_VODAFONE.Download_Upload == 'download']
df_chennai_4G_JIO_download = df_chennai_4G_JIO[df_chennai_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_chennai_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_chennai_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_chennai_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_chennai_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_chennai_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  chennai  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_chennai_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_chennai_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_chennai_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_chennai_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_chennai_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                     
                                                            
# [5] Delhi


print("\n---: [5]  delhi operation :-------")
df_delhi = df[df.Service_Area == 'Delhi']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_delhi.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_delhi.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  delhi 

techno_delhi = df_delhi.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_delhi)
print("-------------------------------")
count = 0
for row in range(len(techno_delhi)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  delhi 3G operation

print("\n---: convert to  delhi-3G operation :-------")
df_delhi_3G = df_delhi[df_delhi.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_delhi_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_delhi_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  delhi 3G

df_delhi_3G_sp = df_delhi_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_delhi_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_delhi_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_delhi_3G_sp_AIRTEL
# df_delhi_3G_sp_CELLONE                 
# df_delhi_3G_sp_IDEA                     
# df_delhi_3G_sp_VODAFONE   

print("\n---:  delhi-3G operation  :-------")

df_delhi_3G_AIRTEL = df_delhi_3G[df_delhi_3G.Service_provider == 'AIRTEL']
df_delhi_3G_CELLONE = df_delhi_3G[df_delhi_3G.Service_provider == 'CELLONE']
df_delhi_3G_IDEA = df_delhi_3G[df_delhi_3G.Service_provider == 'IDEA']
df_delhi_3G_VODAFONE = df_delhi_3G[df_delhi_3G.Service_provider == 'VODAFONE']

# [1-A]  delhi  3G upload plotting

df_delhi_3G_AIRTEL_upload = df_delhi_3G_AIRTEL[df_delhi_3G_AIRTEL.Download_Upload == 'upload']
df_delhi_3G_CELLONE_upload = df_delhi_3G_CELLONE[df_delhi_3G_CELLONE.Download_Upload == 'upload']
df_delhi_3G_IDEA_upload = df_delhi_3G_IDEA[df_delhi_3G_IDEA.Download_Upload == 'upload']
df_delhi_3G_VODAFONE_upload = df_delhi_3G_VODAFONE[df_delhi_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_delhi_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_delhi_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_delhi_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_delhi_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  delhi  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_delhi_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_delhi_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_delhi_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_delhi_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  delhi  3G download plotting

                                                                                                                                                          
df_delhi_3G_AIRTEL_download = df_delhi_3G_AIRTEL[df_delhi_3G_AIRTEL.Download_Upload == 'download']
df_delhi_3G_CELLONE_download = df_delhi_3G_CELLONE[df_delhi_3G_CELLONE.Download_Upload == 'download']
df_delhi_3G_IDEA_download = df_delhi_3G_IDEA[df_delhi_3G_IDEA.Download_Upload == 'download']
df_delhi_3G_VODAFONE_download = df_delhi_3G_VODAFONE[df_delhi_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_delhi_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_delhi_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_delhi_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_delhi_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  delhi  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_delhi_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_delhi_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_delhi_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_delhi_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  delhi 4G operation

print("\n---: convert to  delhi-4G operation :-------")
df_delhi_4G = df_delhi[df_delhi.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_delhi_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_delhi_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  delhi 4G

df_delhi_4G_sp = df_delhi_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_delhi_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_delhi_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_delhi_4G_sp_AIRTEL
# df_delhi_4G_sp_CELLONE                 
# df_delhi_4G_sp_IDEA                     
# df_delhi_4G_sp_VODAFONE 
# df_delhi_4G_sp_JIO  

print("\n---:  delhi-4G operation  :-------")

df_delhi_4G_AIRTEL = df_delhi_4G[df_delhi_4G.Service_provider == 'AIRTEL']
df_delhi_4G_CELLONE = df_delhi_4G[df_delhi_4G.Service_provider == 'CELLONE']
df_delhi_4G_IDEA = df_delhi_4G[df_delhi_4G.Service_provider == 'IDEA']
df_delhi_4G_VODAFONE = df_delhi_4G[df_delhi_4G.Service_provider == 'VODAFONE']
df_delhi_4G_JIO = df_delhi_4G[df_delhi_4G.Service_provider == 'JIO']

#  delhi  4G upload plotting

df_delhi_4G_AIRTEL_upload = df_delhi_4G_AIRTEL[df_delhi_4G_AIRTEL.Download_Upload == 'upload']
df_delhi_4G_CELLONE_upload = df_delhi_4G_CELLONE[df_delhi_4G_CELLONE.Download_Upload == 'upload']
df_delhi_4G_IDEA_upload = df_delhi_4G_IDEA[df_delhi_4G_IDEA.Download_Upload == 'upload']
df_delhi_4G_VODAFONE_upload = df_delhi_4G_VODAFONE[df_delhi_4G_VODAFONE.Download_Upload == 'upload']
df_delhi_4G_JIO_upload = df_delhi_4G_JIO[df_delhi_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_delhi_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_delhi_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_delhi_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_delhi_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_delhi_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  delhi  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_delhi_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_delhi_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_delhi_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_delhi_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_delhi_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  delhi  4G download plotting
                                                                                                                                                          
df_delhi_4G_AIRTEL_download = df_delhi_4G_AIRTEL[df_delhi_4G_AIRTEL.Download_Upload == 'download']
df_delhi_4G_CELLONE_download = df_delhi_4G_CELLONE[df_delhi_4G_CELLONE.Download_Upload == 'download']
df_delhi_4G_IDEA_download = df_delhi_4G_IDEA[df_delhi_4G_IDEA.Download_Upload == 'download']
df_delhi_4G_VODAFONE_download = df_delhi_4G_VODAFONE[df_delhi_4G_VODAFONE.Download_Upload == 'download']
df_delhi_4G_JIO_download = df_delhi_4G_JIO[df_delhi_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_delhi_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_delhi_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_delhi_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_delhi_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_delhi_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  delhi  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_delhi_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_delhi_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_delhi_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_delhi_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_delhi_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                                      
                                                                     
# [6] Gujarat


print("\n---: [6]  gujrat operation :-------")
df_gujrat = df[df.Service_Area == 'Gujarat']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_gujrat.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_gujrat.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  gujrat 

techno_gujrat = df_gujrat.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_gujrat)
print("-------------------------------")
count = 0
for row in range(len(techno_gujrat)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  gujrat 3G operation

print("\n---: convert to  gujrat-3G operation :-------")
df_gujrat_3G = df_gujrat[df_gujrat.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_gujrat_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_gujrat_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  gujrat 3G

df_gujrat_3G_sp = df_gujrat_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_gujrat_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_gujrat_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_gujrat_3G_sp_AIRTEL
# df_gujrat_3G_sp_CELLONE                 
# df_gujrat_3G_sp_IDEA                     
# df_gujrat_3G_sp_VODAFONE   

print("\n---:  gujrat-3G operation  :-------")

df_gujrat_3G_AIRTEL = df_gujrat_3G[df_gujrat_3G.Service_provider == 'AIRTEL']
df_gujrat_3G_CELLONE = df_gujrat_3G[df_gujrat_3G.Service_provider == 'CELLONE']
df_gujrat_3G_IDEA = df_gujrat_3G[df_gujrat_3G.Service_provider == 'IDEA']
df_gujrat_3G_VODAFONE = df_gujrat_3G[df_gujrat_3G.Service_provider == 'VODAFONE']

# [1-A]  gujrat  3G upload plotting

df_gujrat_3G_AIRTEL_upload = df_gujrat_3G_AIRTEL[df_gujrat_3G_AIRTEL.Download_Upload == 'upload']
df_gujrat_3G_CELLONE_upload = df_gujrat_3G_CELLONE[df_gujrat_3G_CELLONE.Download_Upload == 'upload']
df_gujrat_3G_IDEA_upload = df_gujrat_3G_IDEA[df_gujrat_3G_IDEA.Download_Upload == 'upload']
df_gujrat_3G_VODAFONE_upload = df_gujrat_3G_VODAFONE[df_gujrat_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_gujrat_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_gujrat_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_gujrat_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_gujrat_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  gujrat  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_gujrat_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_gujrat_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_gujrat_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_gujrat_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  gujrat  3G download plotting

                                                                                                                                                          
df_gujrat_3G_AIRTEL_download = df_gujrat_3G_AIRTEL[df_gujrat_3G_AIRTEL.Download_Upload == 'download']
df_gujrat_3G_CELLONE_download = df_gujrat_3G_CELLONE[df_gujrat_3G_CELLONE.Download_Upload == 'download']
df_gujrat_3G_IDEA_download = df_gujrat_3G_IDEA[df_gujrat_3G_IDEA.Download_Upload == 'download']
df_gujrat_3G_VODAFONE_download = df_gujrat_3G_VODAFONE[df_gujrat_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_gujrat_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_gujrat_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_gujrat_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_gujrat_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  gujrat  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_gujrat_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_gujrat_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_gujrat_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_gujrat_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  gujrat 4G operation

print("\n---: convert to  gujrat-4G operation :-------")
df_gujrat_4G = df_gujrat[df_gujrat.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_gujrat_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_gujrat_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  gujrat 4G

df_gujrat_4G_sp = df_gujrat_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_gujrat_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_gujrat_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_gujrat_4G_sp_AIRTEL
# df_gujrat_4G_sp_CELLONE                 
# df_gujrat_4G_sp_IDEA                     
# df_gujrat_4G_sp_VODAFONE 
# df_gujrat_4G_sp_JIO  

print("\n---:  gujrat-4G operation  :-------")

df_gujrat_4G_AIRTEL = df_gujrat_4G[df_gujrat_4G.Service_provider == 'AIRTEL']
df_gujrat_4G_CELLONE = df_gujrat_4G[df_gujrat_4G.Service_provider == 'CELLONE']
df_gujrat_4G_IDEA = df_gujrat_4G[df_gujrat_4G.Service_provider == 'IDEA']
df_gujrat_4G_VODAFONE = df_gujrat_4G[df_gujrat_4G.Service_provider == 'VODAFONE']
df_gujrat_4G_JIO = df_gujrat_4G[df_gujrat_4G.Service_provider == 'JIO']

#  gujrat  4G upload plotting

df_gujrat_4G_AIRTEL_upload = df_gujrat_4G_AIRTEL[df_gujrat_4G_AIRTEL.Download_Upload == 'upload']
df_gujrat_4G_CELLONE_upload = df_gujrat_4G_CELLONE[df_gujrat_4G_CELLONE.Download_Upload == 'upload']
df_gujrat_4G_IDEA_upload = df_gujrat_4G_IDEA[df_gujrat_4G_IDEA.Download_Upload == 'upload']
df_gujrat_4G_VODAFONE_upload = df_gujrat_4G_VODAFONE[df_gujrat_4G_VODAFONE.Download_Upload == 'upload']
df_gujrat_4G_JIO_upload = df_gujrat_4G_JIO[df_gujrat_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_gujrat_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_gujrat_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_gujrat_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_gujrat_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_gujrat_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  gujrat  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_gujrat_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_gujrat_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_gujrat_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_gujrat_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_gujrat_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  gujrat  4G download plotting
                                                                                                                                                          
df_gujrat_4G_AIRTEL_download = df_gujrat_4G_AIRTEL[df_gujrat_4G_AIRTEL.Download_Upload == 'download']
df_gujrat_4G_CELLONE_download = df_gujrat_4G_CELLONE[df_gujrat_4G_CELLONE.Download_Upload == 'download']
df_gujrat_4G_IDEA_download = df_gujrat_4G_IDEA[df_gujrat_4G_IDEA.Download_Upload == 'download']
df_gujrat_4G_VODAFONE_download = df_gujrat_4G_VODAFONE[df_gujrat_4G_VODAFONE.Download_Upload == 'download']
df_gujrat_4G_JIO_download = df_gujrat_4G_JIO[df_gujrat_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_gujrat_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_gujrat_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_gujrat_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_gujrat_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_gujrat_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  gujrat  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_gujrat_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_gujrat_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_gujrat_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_gujrat_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_gujrat_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                      
                                                               
# [7] Haryana


print("\n---: [7]  haryana operation :-------")
df_haryana = df[df.Service_Area == 'Haryana']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_haryana.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_haryana.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  haryana 

techno_haryana = df_haryana.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_haryana)
print("-------------------------------")
count = 0
for row in range(len(techno_haryana)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  haryana 3G operation

print("\n---: convert to  haryana-3G operation :-------")
df_haryana_3G = df_haryana[df_haryana.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_haryana_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_haryana_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  haryana 3G

df_haryana_3G_sp = df_haryana_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_haryana_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_haryana_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_haryana_3G_sp_AIRTEL
# df_haryana_3G_sp_CELLONE                 
# df_haryana_3G_sp_IDEA                     
# df_haryana_3G_sp_VODAFONE   

print("\n---:  haryana-3G operation  :-------")

df_haryana_3G_AIRTEL = df_haryana_3G[df_haryana_3G.Service_provider == 'AIRTEL']
df_haryana_3G_CELLONE = df_haryana_3G[df_haryana_3G.Service_provider == 'CELLONE']
df_haryana_3G_IDEA = df_haryana_3G[df_haryana_3G.Service_provider == 'IDEA']
df_haryana_3G_VODAFONE = df_haryana_3G[df_haryana_3G.Service_provider == 'VODAFONE']

# [1-A]  haryana  3G upload plotting

df_haryana_3G_AIRTEL_upload = df_haryana_3G_AIRTEL[df_haryana_3G_AIRTEL.Download_Upload == 'upload']
df_haryana_3G_CELLONE_upload = df_haryana_3G_CELLONE[df_haryana_3G_CELLONE.Download_Upload == 'upload']
df_haryana_3G_IDEA_upload = df_haryana_3G_IDEA[df_haryana_3G_IDEA.Download_Upload == 'upload']
df_haryana_3G_VODAFONE_upload = df_haryana_3G_VODAFONE[df_haryana_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_haryana_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_haryana_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_haryana_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_haryana_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  haryana  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_haryana_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_haryana_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_haryana_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_haryana_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  haryana  3G download plotting

                                                                                                                                                          
df_haryana_3G_AIRTEL_download = df_haryana_3G_AIRTEL[df_haryana_3G_AIRTEL.Download_Upload == 'download']
df_haryana_3G_CELLONE_download = df_haryana_3G_CELLONE[df_haryana_3G_CELLONE.Download_Upload == 'download']
df_haryana_3G_IDEA_download = df_haryana_3G_IDEA[df_haryana_3G_IDEA.Download_Upload == 'download']
df_haryana_3G_VODAFONE_download = df_haryana_3G_VODAFONE[df_haryana_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_haryana_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_haryana_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_haryana_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_haryana_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  haryana  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_haryana_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_haryana_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_haryana_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_haryana_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  haryana 4G operation

print("\n---: convert to  haryana-4G operation :-------")
df_haryana_4G = df_haryana[df_haryana.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_haryana_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_haryana_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  haryana 4G

df_haryana_4G_sp = df_haryana_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_haryana_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_haryana_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_haryana_4G_sp_AIRTEL
# df_haryana_4G_sp_CELLONE                 
# df_haryana_4G_sp_IDEA                     
# df_haryana_4G_sp_VODAFONE 
# df_haryana_4G_sp_JIO  

print("\n---:  haryana-4G operation  :-------")

df_haryana_4G_AIRTEL = df_haryana_4G[df_haryana_4G.Service_provider == 'AIRTEL']
df_haryana_4G_CELLONE = df_haryana_4G[df_haryana_4G.Service_provider == 'CELLONE']
df_haryana_4G_IDEA = df_haryana_4G[df_haryana_4G.Service_provider == 'IDEA']
df_haryana_4G_VODAFONE = df_haryana_4G[df_haryana_4G.Service_provider == 'VODAFONE']
df_haryana_4G_JIO = df_haryana_4G[df_haryana_4G.Service_provider == 'JIO']

#  haryana  4G upload plotting

df_haryana_4G_AIRTEL_upload = df_haryana_4G_AIRTEL[df_haryana_4G_AIRTEL.Download_Upload == 'upload']
df_haryana_4G_CELLONE_upload = df_haryana_4G_CELLONE[df_haryana_4G_CELLONE.Download_Upload == 'upload']
df_haryana_4G_IDEA_upload = df_haryana_4G_IDEA[df_haryana_4G_IDEA.Download_Upload == 'upload']
df_haryana_4G_VODAFONE_upload = df_haryana_4G_VODAFONE[df_haryana_4G_VODAFONE.Download_Upload == 'upload']
df_haryana_4G_JIO_upload = df_haryana_4G_JIO[df_haryana_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_haryana_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_haryana_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_haryana_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_haryana_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_haryana_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  haryana  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_haryana_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_haryana_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_haryana_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_haryana_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_haryana_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  haryana  4G download plotting
                                                                                                                                                          
df_haryana_4G_AIRTEL_download = df_haryana_4G_AIRTEL[df_haryana_4G_AIRTEL.Download_Upload == 'download']
df_haryana_4G_CELLONE_download = df_haryana_4G_CELLONE[df_haryana_4G_CELLONE.Download_Upload == 'download']
df_haryana_4G_IDEA_download = df_haryana_4G_IDEA[df_haryana_4G_IDEA.Download_Upload == 'download']
df_haryana_4G_VODAFONE_download = df_haryana_4G_VODAFONE[df_haryana_4G_VODAFONE.Download_Upload == 'download']
df_haryana_4G_JIO_download = df_haryana_4G_JIO[df_haryana_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_haryana_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_haryana_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_haryana_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_haryana_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_haryana_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  haryana  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_haryana_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_haryana_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_haryana_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_haryana_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_haryana_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                      
                                                               
# [8] Himachal Pradesh 




print("\n---: [8]  himachal_pradesh operation :-------")
df_himachal_pradesh = df[df.Service_Area == 'Himachal Pradesh']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_himachal_pradesh.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_himachal_pradesh.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  himachal_pradesh 

techno_himachal_pradesh = df_himachal_pradesh.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_himachal_pradesh)
print("-------------------------------")
count = 0
for row in range(len(techno_himachal_pradesh)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  himachal_pradesh 3G operation

print("\n---: convert to  himachal_pradesh-3G operation :-------")
df_himachal_pradesh_3G = df_himachal_pradesh[df_himachal_pradesh.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_himachal_pradesh_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_himachal_pradesh_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  himachal_pradesh 3G

df_himachal_pradesh_3G_sp = df_himachal_pradesh_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_himachal_pradesh_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_himachal_pradesh_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_himachal_pradesh_3G_sp_AIRTEL
# df_himachal_pradesh_3G_sp_CELLONE                 
# df_himachal_pradesh_3G_sp_IDEA                     
# df_himachal_pradesh_3G_sp_VODAFONE   

print("\n---:  himachal_pradesh-3G operation  :-------")

df_himachal_pradesh_3G_AIRTEL = df_himachal_pradesh_3G[df_himachal_pradesh_3G.Service_provider == 'AIRTEL']
df_himachal_pradesh_3G_CELLONE = df_himachal_pradesh_3G[df_himachal_pradesh_3G.Service_provider == 'CELLONE']
df_himachal_pradesh_3G_IDEA = df_himachal_pradesh_3G[df_himachal_pradesh_3G.Service_provider == 'IDEA']
df_himachal_pradesh_3G_VODAFONE = df_himachal_pradesh_3G[df_himachal_pradesh_3G.Service_provider == 'VODAFONE']

# [1-A]  himachal_pradesh  3G upload plotting

df_himachal_pradesh_3G_AIRTEL_upload = df_himachal_pradesh_3G_AIRTEL[df_himachal_pradesh_3G_AIRTEL.Download_Upload == 'upload']
df_himachal_pradesh_3G_CELLONE_upload = df_himachal_pradesh_3G_CELLONE[df_himachal_pradesh_3G_CELLONE.Download_Upload == 'upload']
df_himachal_pradesh_3G_IDEA_upload = df_himachal_pradesh_3G_IDEA[df_himachal_pradesh_3G_IDEA.Download_Upload == 'upload']
df_himachal_pradesh_3G_VODAFONE_upload = df_himachal_pradesh_3G_VODAFONE[df_himachal_pradesh_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_himachal_pradesh_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_himachal_pradesh_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_himachal_pradesh_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_himachal_pradesh_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  himachal_pradesh  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_himachal_pradesh_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_himachal_pradesh_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_himachal_pradesh_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_himachal_pradesh_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  himachal_pradesh  3G download plotting

                                                                                                                                                          
df_himachal_pradesh_3G_AIRTEL_download = df_himachal_pradesh_3G_AIRTEL[df_himachal_pradesh_3G_AIRTEL.Download_Upload == 'download']
df_himachal_pradesh_3G_CELLONE_download = df_himachal_pradesh_3G_CELLONE[df_himachal_pradesh_3G_CELLONE.Download_Upload == 'download']
df_himachal_pradesh_3G_IDEA_download = df_himachal_pradesh_3G_IDEA[df_himachal_pradesh_3G_IDEA.Download_Upload == 'download']
df_himachal_pradesh_3G_VODAFONE_download = df_himachal_pradesh_3G_VODAFONE[df_himachal_pradesh_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_himachal_pradesh_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_himachal_pradesh_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_himachal_pradesh_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_himachal_pradesh_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  himachal_pradesh  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_himachal_pradesh_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_himachal_pradesh_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_himachal_pradesh_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_himachal_pradesh_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  himachal_pradesh 4G operation

print("\n---: convert to  himachal_pradesh-4G operation :-------")
df_himachal_pradesh_4G = df_himachal_pradesh[df_himachal_pradesh.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_himachal_pradesh_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_himachal_pradesh_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  himachal_pradesh 4G

df_himachal_pradesh_4G_sp = df_himachal_pradesh_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_himachal_pradesh_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_himachal_pradesh_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_himachal_pradesh_4G_sp_AIRTEL
# df_himachal_pradesh_4G_sp_CELLONE                 
# df_himachal_pradesh_4G_sp_IDEA                     
# df_himachal_pradesh_4G_sp_VODAFONE 
# df_himachal_pradesh_4G_sp_JIO  

print("\n---:  himachal_pradesh-4G operation  :-------")

df_himachal_pradesh_4G_AIRTEL = df_himachal_pradesh_4G[df_himachal_pradesh_4G.Service_provider == 'AIRTEL']
df_himachal_pradesh_4G_CELLONE = df_himachal_pradesh_4G[df_himachal_pradesh_4G.Service_provider == 'CELLONE']
df_himachal_pradesh_4G_IDEA = df_himachal_pradesh_4G[df_himachal_pradesh_4G.Service_provider == 'IDEA']
df_himachal_pradesh_4G_VODAFONE = df_himachal_pradesh_4G[df_himachal_pradesh_4G.Service_provider == 'VODAFONE']
df_himachal_pradesh_4G_JIO = df_himachal_pradesh_4G[df_himachal_pradesh_4G.Service_provider == 'JIO']

#  himachal_pradesh  4G upload plotting

df_himachal_pradesh_4G_AIRTEL_upload = df_himachal_pradesh_4G_AIRTEL[df_himachal_pradesh_4G_AIRTEL.Download_Upload == 'upload']
df_himachal_pradesh_4G_CELLONE_upload = df_himachal_pradesh_4G_CELLONE[df_himachal_pradesh_4G_CELLONE.Download_Upload == 'upload']
df_himachal_pradesh_4G_IDEA_upload = df_himachal_pradesh_4G_IDEA[df_himachal_pradesh_4G_IDEA.Download_Upload == 'upload']
df_himachal_pradesh_4G_VODAFONE_upload = df_himachal_pradesh_4G_VODAFONE[df_himachal_pradesh_4G_VODAFONE.Download_Upload == 'upload']
df_himachal_pradesh_4G_JIO_upload = df_himachal_pradesh_4G_JIO[df_himachal_pradesh_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_himachal_pradesh_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_himachal_pradesh_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_himachal_pradesh_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_himachal_pradesh_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_himachal_pradesh_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  himachal_pradesh  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_himachal_pradesh_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_himachal_pradesh_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_himachal_pradesh_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_himachal_pradesh_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_himachal_pradesh_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  himachal_pradesh  4G download plotting
                                                                                                                                                          
df_himachal_pradesh_4G_AIRTEL_download = df_himachal_pradesh_4G_AIRTEL[df_himachal_pradesh_4G_AIRTEL.Download_Upload == 'download']
df_himachal_pradesh_4G_CELLONE_download = df_himachal_pradesh_4G_CELLONE[df_himachal_pradesh_4G_CELLONE.Download_Upload == 'download']
df_himachal_pradesh_4G_IDEA_download = df_himachal_pradesh_4G_IDEA[df_himachal_pradesh_4G_IDEA.Download_Upload == 'download']
df_himachal_pradesh_4G_VODAFONE_download = df_himachal_pradesh_4G_VODAFONE[df_himachal_pradesh_4G_VODAFONE.Download_Upload == 'download']
df_himachal_pradesh_4G_JIO_download = df_himachal_pradesh_4G_JIO[df_himachal_pradesh_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_himachal_pradesh_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_himachal_pradesh_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_himachal_pradesh_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_himachal_pradesh_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_himachal_pradesh_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  himachal_pradesh  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_himachal_pradesh_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_himachal_pradesh_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_himachal_pradesh_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_himachal_pradesh_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_himachal_pradesh_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                             
                                    
# [9] Jammu & Kashmir 




print("\n---: [9]  jammu_kashmir operation :-------")
df_jammu_kashmir = df[df.Service_Area == 'Jammu & Kashmir']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_jammu_kashmir.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_jammu_kashmir.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  jammu_kashmir 

techno_jammu_kashmir = df_jammu_kashmir.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_jammu_kashmir)
print("-------------------------------")
count = 0
for row in range(len(techno_jammu_kashmir)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  jammu_kashmir 3G operation

print("\n---: convert to  jammu_kashmir-3G operation :-------")
df_jammu_kashmir_3G = df_jammu_kashmir[df_jammu_kashmir.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_jammu_kashmir_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_jammu_kashmir_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  jammu_kashmir 3G

df_jammu_kashmir_3G_sp = df_jammu_kashmir_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_jammu_kashmir_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_jammu_kashmir_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_jammu_kashmir_3G_sp_AIRTEL
# df_jammu_kashmir_3G_sp_CELLONE                 
# df_jammu_kashmir_3G_sp_IDEA                     
# df_jammu_kashmir_3G_sp_VODAFONE   

print("\n---:  jammu_kashmir-3G operation  :-------")

df_jammu_kashmir_3G_AIRTEL = df_jammu_kashmir_3G[df_jammu_kashmir_3G.Service_provider == 'AIRTEL']
df_jammu_kashmir_3G_CELLONE = df_jammu_kashmir_3G[df_jammu_kashmir_3G.Service_provider == 'CELLONE']
df_jammu_kashmir_3G_IDEA = df_jammu_kashmir_3G[df_jammu_kashmir_3G.Service_provider == 'IDEA']
df_jammu_kashmir_3G_VODAFONE = df_jammu_kashmir_3G[df_jammu_kashmir_3G.Service_provider == 'VODAFONE']

# [1-A]  jammu_kashmir  3G upload plotting

df_jammu_kashmir_3G_AIRTEL_upload = df_jammu_kashmir_3G_AIRTEL[df_jammu_kashmir_3G_AIRTEL.Download_Upload == 'upload']
df_jammu_kashmir_3G_CELLONE_upload = df_jammu_kashmir_3G_CELLONE[df_jammu_kashmir_3G_CELLONE.Download_Upload == 'upload']
df_jammu_kashmir_3G_IDEA_upload = df_jammu_kashmir_3G_IDEA[df_jammu_kashmir_3G_IDEA.Download_Upload == 'upload']
df_jammu_kashmir_3G_VODAFONE_upload = df_jammu_kashmir_3G_VODAFONE[df_jammu_kashmir_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_jammu_kashmir_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_jammu_kashmir_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_jammu_kashmir_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_jammu_kashmir_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  jammu_kashmir  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_jammu_kashmir_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_jammu_kashmir_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_jammu_kashmir_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_jammu_kashmir_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  jammu_kashmir  3G download plotting

                                                                                                                                                          
df_jammu_kashmir_3G_AIRTEL_download = df_jammu_kashmir_3G_AIRTEL[df_jammu_kashmir_3G_AIRTEL.Download_Upload == 'download']
df_jammu_kashmir_3G_CELLONE_download = df_jammu_kashmir_3G_CELLONE[df_jammu_kashmir_3G_CELLONE.Download_Upload == 'download']
df_jammu_kashmir_3G_IDEA_download = df_jammu_kashmir_3G_IDEA[df_jammu_kashmir_3G_IDEA.Download_Upload == 'download']
df_jammu_kashmir_3G_VODAFONE_download = df_jammu_kashmir_3G_VODAFONE[df_jammu_kashmir_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_jammu_kashmir_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_jammu_kashmir_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_jammu_kashmir_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_jammu_kashmir_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  jammu_kashmir  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_jammu_kashmir_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_jammu_kashmir_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_jammu_kashmir_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_jammu_kashmir_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  jammu_kashmir 4G operation

print("\n---: convert to  jammu_kashmir-4G operation :-------")
df_jammu_kashmir_4G = df_jammu_kashmir[df_jammu_kashmir.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_jammu_kashmir_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_jammu_kashmir_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  jammu_kashmir 4G

df_jammu_kashmir_4G_sp = df_jammu_kashmir_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_jammu_kashmir_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_jammu_kashmir_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_jammu_kashmir_4G_sp_AIRTEL
# df_jammu_kashmir_4G_sp_CELLONE                 
# df_jammu_kashmir_4G_sp_IDEA                     
# df_jammu_kashmir_4G_sp_VODAFONE 
# df_jammu_kashmir_4G_sp_JIO  

print("\n---:  jammu_kashmir-4G operation  :-------")

df_jammu_kashmir_4G_AIRTEL = df_jammu_kashmir_4G[df_jammu_kashmir_4G.Service_provider == 'AIRTEL']
df_jammu_kashmir_4G_CELLONE = df_jammu_kashmir_4G[df_jammu_kashmir_4G.Service_provider == 'CELLONE']
df_jammu_kashmir_4G_IDEA = df_jammu_kashmir_4G[df_jammu_kashmir_4G.Service_provider == 'IDEA']
df_jammu_kashmir_4G_VODAFONE = df_jammu_kashmir_4G[df_jammu_kashmir_4G.Service_provider == 'VODAFONE']
df_jammu_kashmir_4G_JIO = df_jammu_kashmir_4G[df_jammu_kashmir_4G.Service_provider == 'JIO']

#  jammu_kashmir  4G upload plotting

df_jammu_kashmir_4G_AIRTEL_upload = df_jammu_kashmir_4G_AIRTEL[df_jammu_kashmir_4G_AIRTEL.Download_Upload == 'upload']
df_jammu_kashmir_4G_CELLONE_upload = df_jammu_kashmir_4G_CELLONE[df_jammu_kashmir_4G_CELLONE.Download_Upload == 'upload']
df_jammu_kashmir_4G_IDEA_upload = df_jammu_kashmir_4G_IDEA[df_jammu_kashmir_4G_IDEA.Download_Upload == 'upload']
df_jammu_kashmir_4G_VODAFONE_upload = df_jammu_kashmir_4G_VODAFONE[df_jammu_kashmir_4G_VODAFONE.Download_Upload == 'upload']
df_jammu_kashmir_4G_JIO_upload = df_jammu_kashmir_4G_JIO[df_jammu_kashmir_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_jammu_kashmir_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_jammu_kashmir_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_jammu_kashmir_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_jammu_kashmir_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_jammu_kashmir_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  jammu_kashmir  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_jammu_kashmir_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_jammu_kashmir_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_jammu_kashmir_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_jammu_kashmir_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_jammu_kashmir_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  jammu_kashmir  4G download plotting
                                                                                                                                                          
df_jammu_kashmir_4G_AIRTEL_download = df_jammu_kashmir_4G_AIRTEL[df_jammu_kashmir_4G_AIRTEL.Download_Upload == 'download']
df_jammu_kashmir_4G_CELLONE_download = df_jammu_kashmir_4G_CELLONE[df_jammu_kashmir_4G_CELLONE.Download_Upload == 'download']
df_jammu_kashmir_4G_IDEA_download = df_jammu_kashmir_4G_IDEA[df_jammu_kashmir_4G_IDEA.Download_Upload == 'download']
df_jammu_kashmir_4G_VODAFONE_download = df_jammu_kashmir_4G_VODAFONE[df_jammu_kashmir_4G_VODAFONE.Download_Upload == 'download']
df_jammu_kashmir_4G_JIO_download = df_jammu_kashmir_4G_JIO[df_jammu_kashmir_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_jammu_kashmir_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_jammu_kashmir_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_jammu_kashmir_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_jammu_kashmir_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_jammu_kashmir_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  jammu_kashmir  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_jammu_kashmir_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_jammu_kashmir_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_jammu_kashmir_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_jammu_kashmir_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_jammu_kashmir_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                              
                                       
# [10] Karnataka 




print("\n---: [10]  Karnataka operation :-------")
df_Karnataka = df[df.Service_Area == 'Karnataka']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Karnataka.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Karnataka.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Karnataka 

techno_Karnataka = df_Karnataka.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Karnataka)
print("-------------------------------")
count = 0
for row in range(len(techno_Karnataka)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Karnataka 3G operation

print("\n---: convert to  Karnataka-3G operation :-------")
df_Karnataka_3G = df_Karnataka[df_Karnataka.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Karnataka_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Karnataka_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Karnataka 3G

df_Karnataka_3G_sp = df_Karnataka_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Karnataka_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Karnataka_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Karnataka_3G_sp_AIRTEL
# df_Karnataka_3G_sp_CELLONE                 
# df_Karnataka_3G_sp_IDEA                     
# df_Karnataka_3G_sp_VODAFONE   

print("\n---:  Karnataka-3G operation  :-------")

df_Karnataka_3G_AIRTEL = df_Karnataka_3G[df_Karnataka_3G.Service_provider == 'AIRTEL']
df_Karnataka_3G_CELLONE = df_Karnataka_3G[df_Karnataka_3G.Service_provider == 'CELLONE']
df_Karnataka_3G_IDEA = df_Karnataka_3G[df_Karnataka_3G.Service_provider == 'IDEA']
df_Karnataka_3G_VODAFONE = df_Karnataka_3G[df_Karnataka_3G.Service_provider == 'VODAFONE']

# [1-A]  Karnataka  3G upload plotting

df_Karnataka_3G_AIRTEL_upload = df_Karnataka_3G_AIRTEL[df_Karnataka_3G_AIRTEL.Download_Upload == 'upload']
df_Karnataka_3G_CELLONE_upload = df_Karnataka_3G_CELLONE[df_Karnataka_3G_CELLONE.Download_Upload == 'upload']
df_Karnataka_3G_IDEA_upload = df_Karnataka_3G_IDEA[df_Karnataka_3G_IDEA.Download_Upload == 'upload']
df_Karnataka_3G_VODAFONE_upload = df_Karnataka_3G_VODAFONE[df_Karnataka_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Karnataka_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Karnataka_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Karnataka_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Karnataka_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Karnataka  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Karnataka_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Karnataka_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Karnataka_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Karnataka_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Karnataka  3G download plotting

                                                                                                                                                          
df_Karnataka_3G_AIRTEL_download = df_Karnataka_3G_AIRTEL[df_Karnataka_3G_AIRTEL.Download_Upload == 'download']
df_Karnataka_3G_CELLONE_download = df_Karnataka_3G_CELLONE[df_Karnataka_3G_CELLONE.Download_Upload == 'download']
df_Karnataka_3G_IDEA_download = df_Karnataka_3G_IDEA[df_Karnataka_3G_IDEA.Download_Upload == 'download']
df_Karnataka_3G_VODAFONE_download = df_Karnataka_3G_VODAFONE[df_Karnataka_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Karnataka_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Karnataka_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Karnataka_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Karnataka_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Karnataka  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Karnataka_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Karnataka_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Karnataka_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Karnataka_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Karnataka 4G operation

print("\n---: convert to  Karnataka-4G operation :-------")
df_Karnataka_4G = df_Karnataka[df_Karnataka.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Karnataka_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Karnataka_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Karnataka 4G

df_Karnataka_4G_sp = df_Karnataka_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Karnataka_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Karnataka_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Karnataka_4G_sp_AIRTEL
# df_Karnataka_4G_sp_CELLONE                 
# df_Karnataka_4G_sp_IDEA                     
# df_Karnataka_4G_sp_VODAFONE 
# df_Karnataka_4G_sp_JIO  

print("\n---:  Karnataka-4G operation  :-------")

df_Karnataka_4G_AIRTEL = df_Karnataka_4G[df_Karnataka_4G.Service_provider == 'AIRTEL']
df_Karnataka_4G_CELLONE = df_Karnataka_4G[df_Karnataka_4G.Service_provider == 'CELLONE']
df_Karnataka_4G_IDEA = df_Karnataka_4G[df_Karnataka_4G.Service_provider == 'IDEA']
df_Karnataka_4G_VODAFONE = df_Karnataka_4G[df_Karnataka_4G.Service_provider == 'VODAFONE']
df_Karnataka_4G_JIO = df_Karnataka_4G[df_Karnataka_4G.Service_provider == 'JIO']

#  Karnataka  4G upload plotting

df_Karnataka_4G_AIRTEL_upload = df_Karnataka_4G_AIRTEL[df_Karnataka_4G_AIRTEL.Download_Upload == 'upload']
df_Karnataka_4G_CELLONE_upload = df_Karnataka_4G_CELLONE[df_Karnataka_4G_CELLONE.Download_Upload == 'upload']
df_Karnataka_4G_IDEA_upload = df_Karnataka_4G_IDEA[df_Karnataka_4G_IDEA.Download_Upload == 'upload']
df_Karnataka_4G_VODAFONE_upload = df_Karnataka_4G_VODAFONE[df_Karnataka_4G_VODAFONE.Download_Upload == 'upload']
df_Karnataka_4G_JIO_upload = df_Karnataka_4G_JIO[df_Karnataka_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Karnataka_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Karnataka_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Karnataka_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Karnataka_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Karnataka_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Karnataka  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Karnataka_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Karnataka_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Karnataka_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Karnataka_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Karnataka_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Karnataka  4G download plotting
                                                                                                                                                          
df_Karnataka_4G_AIRTEL_download = df_Karnataka_4G_AIRTEL[df_Karnataka_4G_AIRTEL.Download_Upload == 'download']
df_Karnataka_4G_CELLONE_download = df_Karnataka_4G_CELLONE[df_Karnataka_4G_CELLONE.Download_Upload == 'download']
df_Karnataka_4G_IDEA_download = df_Karnataka_4G_IDEA[df_Karnataka_4G_IDEA.Download_Upload == 'download']
df_Karnataka_4G_VODAFONE_download = df_Karnataka_4G_VODAFONE[df_Karnataka_4G_VODAFONE.Download_Upload == 'download']
df_Karnataka_4G_JIO_download = df_Karnataka_4G_JIO[df_Karnataka_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Karnataka_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Karnataka_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Karnataka_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Karnataka_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Karnataka_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Karnataka  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Karnataka_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Karnataka_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Karnataka_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Karnataka_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Karnataka_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                   
                                                      
# [11] Kerala 




print("\n---: [11]  Kerala operation :-------")
df_Kerala = df[df.Service_Area == 'Kerala']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kerala.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kerala.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Kerala 

techno_Kerala = df_Kerala.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Kerala)
print("-------------------------------")
count = 0
for row in range(len(techno_Kerala)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Kerala 3G operation

print("\n---: convert to  Kerala-3G operation :-------")
df_Kerala_3G = df_Kerala[df_Kerala.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kerala_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kerala_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Kerala 3G

df_Kerala_3G_sp = df_Kerala_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Kerala_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Kerala_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Kerala_3G_sp_AIRTEL
# df_Kerala_3G_sp_CELLONE                 
# df_Kerala_3G_sp_IDEA                     
# df_Kerala_3G_sp_VODAFONE   

print("\n---:  Kerala-3G operation  :-------")

df_Kerala_3G_AIRTEL = df_Kerala_3G[df_Kerala_3G.Service_provider == 'AIRTEL']
df_Kerala_3G_CELLONE = df_Kerala_3G[df_Kerala_3G.Service_provider == 'CELLONE']
df_Kerala_3G_IDEA = df_Kerala_3G[df_Kerala_3G.Service_provider == 'IDEA']
df_Kerala_3G_VODAFONE = df_Kerala_3G[df_Kerala_3G.Service_provider == 'VODAFONE']

# [1-A]  Kerala  3G upload plotting

df_Kerala_3G_AIRTEL_upload = df_Kerala_3G_AIRTEL[df_Kerala_3G_AIRTEL.Download_Upload == 'upload']
df_Kerala_3G_CELLONE_upload = df_Kerala_3G_CELLONE[df_Kerala_3G_CELLONE.Download_Upload == 'upload']
df_Kerala_3G_IDEA_upload = df_Kerala_3G_IDEA[df_Kerala_3G_IDEA.Download_Upload == 'upload']
df_Kerala_3G_VODAFONE_upload = df_Kerala_3G_VODAFONE[df_Kerala_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Kerala_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kerala_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kerala_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kerala_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Kerala  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kerala_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Kerala_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Kerala_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Kerala_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Kerala  3G download plotting

                                                                                                                                                          
df_Kerala_3G_AIRTEL_download = df_Kerala_3G_AIRTEL[df_Kerala_3G_AIRTEL.Download_Upload == 'download']
df_Kerala_3G_CELLONE_download = df_Kerala_3G_CELLONE[df_Kerala_3G_CELLONE.Download_Upload == 'download']
df_Kerala_3G_IDEA_download = df_Kerala_3G_IDEA[df_Kerala_3G_IDEA.Download_Upload == 'download']
df_Kerala_3G_VODAFONE_download = df_Kerala_3G_VODAFONE[df_Kerala_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Kerala_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kerala_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kerala_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kerala_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Kerala  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kerala_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Kerala_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Kerala_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Kerala_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Kerala 4G operation

print("\n---: convert to  Kerala-4G operation :-------")
df_Kerala_4G = df_Kerala[df_Kerala.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kerala_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kerala_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Kerala 4G

df_Kerala_4G_sp = df_Kerala_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Kerala_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Kerala_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Kerala_4G_sp_AIRTEL
# df_Kerala_4G_sp_CELLONE                 
# df_Kerala_4G_sp_IDEA                     
# df_Kerala_4G_sp_VODAFONE 
# df_Kerala_4G_sp_JIO  

print("\n---:  Kerala-4G operation  :-------")

df_Kerala_4G_AIRTEL = df_Kerala_4G[df_Kerala_4G.Service_provider == 'AIRTEL']
df_Kerala_4G_CELLONE = df_Kerala_4G[df_Kerala_4G.Service_provider == 'CELLONE']
df_Kerala_4G_IDEA = df_Kerala_4G[df_Kerala_4G.Service_provider == 'IDEA']
df_Kerala_4G_VODAFONE = df_Kerala_4G[df_Kerala_4G.Service_provider == 'VODAFONE']
df_Kerala_4G_JIO = df_Kerala_4G[df_Kerala_4G.Service_provider == 'JIO']

#  Kerala  4G upload plotting

df_Kerala_4G_AIRTEL_upload = df_Kerala_4G_AIRTEL[df_Kerala_4G_AIRTEL.Download_Upload == 'upload']
df_Kerala_4G_CELLONE_upload = df_Kerala_4G_CELLONE[df_Kerala_4G_CELLONE.Download_Upload == 'upload']
df_Kerala_4G_IDEA_upload = df_Kerala_4G_IDEA[df_Kerala_4G_IDEA.Download_Upload == 'upload']
df_Kerala_4G_VODAFONE_upload = df_Kerala_4G_VODAFONE[df_Kerala_4G_VODAFONE.Download_Upload == 'upload']
df_Kerala_4G_JIO_upload = df_Kerala_4G_JIO[df_Kerala_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Kerala_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kerala_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kerala_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kerala_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Kerala_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Kerala  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kerala_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Kerala_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Kerala_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Kerala_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Kerala_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Kerala  4G download plotting
                                                                                                                                                          
df_Kerala_4G_AIRTEL_download = df_Kerala_4G_AIRTEL[df_Kerala_4G_AIRTEL.Download_Upload == 'download']
df_Kerala_4G_CELLONE_download = df_Kerala_4G_CELLONE[df_Kerala_4G_CELLONE.Download_Upload == 'download']
df_Kerala_4G_IDEA_download = df_Kerala_4G_IDEA[df_Kerala_4G_IDEA.Download_Upload == 'download']
df_Kerala_4G_VODAFONE_download = df_Kerala_4G_VODAFONE[df_Kerala_4G_VODAFONE.Download_Upload == 'download']
df_Kerala_4G_JIO_download = df_Kerala_4G_JIO[df_Kerala_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Kerala_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kerala_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kerala_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kerala_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Kerala_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Kerala  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kerala_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Kerala_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Kerala_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Kerala_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Kerala_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                      
                                                               
# [12] Kolkata 




print("\n---: [12]  Kolkata operation :-------")
df_Kolkata = df[df.Service_Area == 'Kolkata']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kolkata.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kolkata.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Kolkata 

techno_Kolkata = df_Kolkata.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Kolkata)
print("-------------------------------")
count = 0
for row in range(len(techno_Kolkata)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Kolkata 3G operation

print("\n---: convert to  Kolkata-3G operation :-------")
df_Kolkata_3G = df_Kolkata[df_Kolkata.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kolkata_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kolkata_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Kolkata 3G

df_Kolkata_3G_sp = df_Kolkata_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Kolkata_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Kolkata_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Kolkata_3G_sp_AIRTEL
# df_Kolkata_3G_sp_CELLONE                 
# df_Kolkata_3G_sp_IDEA                     
# df_Kolkata_3G_sp_VODAFONE   

print("\n---:  Kolkata-3G operation  :-------")

df_Kolkata_3G_AIRTEL = df_Kolkata_3G[df_Kolkata_3G.Service_provider == 'AIRTEL']
df_Kolkata_3G_CELLONE = df_Kolkata_3G[df_Kolkata_3G.Service_provider == 'CELLONE']
df_Kolkata_3G_IDEA = df_Kolkata_3G[df_Kolkata_3G.Service_provider == 'IDEA']
df_Kolkata_3G_VODAFONE = df_Kolkata_3G[df_Kolkata_3G.Service_provider == 'VODAFONE']

# [1-A]  Kolkata  3G upload plotting

df_Kolkata_3G_AIRTEL_upload = df_Kolkata_3G_AIRTEL[df_Kolkata_3G_AIRTEL.Download_Upload == 'upload']
df_Kolkata_3G_CELLONE_upload = df_Kolkata_3G_CELLONE[df_Kolkata_3G_CELLONE.Download_Upload == 'upload']
df_Kolkata_3G_IDEA_upload = df_Kolkata_3G_IDEA[df_Kolkata_3G_IDEA.Download_Upload == 'upload']
df_Kolkata_3G_VODAFONE_upload = df_Kolkata_3G_VODAFONE[df_Kolkata_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Kolkata_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kolkata_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kolkata_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kolkata_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Kolkata  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kolkata_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Kolkata_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Kolkata_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Kolkata_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Kolkata  3G download plotting

                                                                                                                                                          
df_Kolkata_3G_AIRTEL_download = df_Kolkata_3G_AIRTEL[df_Kolkata_3G_AIRTEL.Download_Upload == 'download']
df_Kolkata_3G_CELLONE_download = df_Kolkata_3G_CELLONE[df_Kolkata_3G_CELLONE.Download_Upload == 'download']
df_Kolkata_3G_IDEA_download = df_Kolkata_3G_IDEA[df_Kolkata_3G_IDEA.Download_Upload == 'download']
df_Kolkata_3G_VODAFONE_download = df_Kolkata_3G_VODAFONE[df_Kolkata_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Kolkata_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kolkata_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kolkata_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kolkata_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Kolkata  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kolkata_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Kolkata_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Kolkata_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Kolkata_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Kolkata 4G operation

print("\n---: convert to  Kolkata-4G operation :-------")
df_Kolkata_4G = df_Kolkata[df_Kolkata.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Kolkata_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Kolkata_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Kolkata 4G

df_Kolkata_4G_sp = df_Kolkata_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Kolkata_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Kolkata_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Kolkata_4G_sp_AIRTEL
# df_Kolkata_4G_sp_CELLONE                 
# df_Kolkata_4G_sp_IDEA                     
# df_Kolkata_4G_sp_VODAFONE 
# df_Kolkata_4G_sp_JIO  

print("\n---:  Kolkata-4G operation  :-------")

df_Kolkata_4G_AIRTEL = df_Kolkata_4G[df_Kolkata_4G.Service_provider == 'AIRTEL']
df_Kolkata_4G_CELLONE = df_Kolkata_4G[df_Kolkata_4G.Service_provider == 'CELLONE']
df_Kolkata_4G_IDEA = df_Kolkata_4G[df_Kolkata_4G.Service_provider == 'IDEA']
df_Kolkata_4G_VODAFONE = df_Kolkata_4G[df_Kolkata_4G.Service_provider == 'VODAFONE']
df_Kolkata_4G_JIO = df_Kolkata_4G[df_Kolkata_4G.Service_provider == 'JIO']

#  Kolkata  4G upload plotting

df_Kolkata_4G_AIRTEL_upload = df_Kolkata_4G_AIRTEL[df_Kolkata_4G_AIRTEL.Download_Upload == 'upload']
df_Kolkata_4G_CELLONE_upload = df_Kolkata_4G_CELLONE[df_Kolkata_4G_CELLONE.Download_Upload == 'upload']
df_Kolkata_4G_IDEA_upload = df_Kolkata_4G_IDEA[df_Kolkata_4G_IDEA.Download_Upload == 'upload']
df_Kolkata_4G_VODAFONE_upload = df_Kolkata_4G_VODAFONE[df_Kolkata_4G_VODAFONE.Download_Upload == 'upload']
df_Kolkata_4G_JIO_upload = df_Kolkata_4G_JIO[df_Kolkata_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Kolkata_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kolkata_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kolkata_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kolkata_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Kolkata_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Kolkata  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kolkata_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Kolkata_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Kolkata_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Kolkata_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Kolkata_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Kolkata  4G download plotting
                                                                                                                                                          
df_Kolkata_4G_AIRTEL_download = df_Kolkata_4G_AIRTEL[df_Kolkata_4G_AIRTEL.Download_Upload == 'download']
df_Kolkata_4G_CELLONE_download = df_Kolkata_4G_CELLONE[df_Kolkata_4G_CELLONE.Download_Upload == 'download']
df_Kolkata_4G_IDEA_download = df_Kolkata_4G_IDEA[df_Kolkata_4G_IDEA.Download_Upload == 'download']
df_Kolkata_4G_VODAFONE_download = df_Kolkata_4G_VODAFONE[df_Kolkata_4G_VODAFONE.Download_Upload == 'download']
df_Kolkata_4G_JIO_download = df_Kolkata_4G_JIO[df_Kolkata_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Kolkata_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Kolkata_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Kolkata_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Kolkata_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Kolkata_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Kolkata  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Kolkata_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Kolkata_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Kolkata_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Kolkata_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Kolkata_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                     
                                                            
# [13] Madhya Pradesh 




print("\n---: [13]  Madhya_Pradesh operation :-------")
df_Madhya_Pradesh = df[df.Service_Area == 'Madhya Pradesh']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Madhya_Pradesh.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Madhya_Pradesh.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Madhya_Pradesh 

techno_Madhya_Pradesh = df_Madhya_Pradesh.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Madhya_Pradesh)
print("-------------------------------")
count = 0
for row in range(len(techno_Madhya_Pradesh)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Madhya_Pradesh 3G operation

print("\n---: convert to  Madhya_Pradesh-3G operation :-------")
df_Madhya_Pradesh_3G = df_Madhya_Pradesh[df_Madhya_Pradesh.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Madhya_Pradesh_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Madhya_Pradesh_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Madhya_Pradesh 3G

df_Madhya_Pradesh_3G_sp = df_Madhya_Pradesh_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Madhya_Pradesh_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Madhya_Pradesh_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Madhya_Pradesh_3G_sp_AIRTEL
# df_Madhya_Pradesh_3G_sp_CELLONE                 
# df_Madhya_Pradesh_3G_sp_IDEA                     
# df_Madhya_Pradesh_3G_sp_VODAFONE   

print("\n---:  Madhya_Pradesh-3G operation  :-------")

df_Madhya_Pradesh_3G_AIRTEL = df_Madhya_Pradesh_3G[df_Madhya_Pradesh_3G.Service_provider == 'AIRTEL']
df_Madhya_Pradesh_3G_CELLONE = df_Madhya_Pradesh_3G[df_Madhya_Pradesh_3G.Service_provider == 'CELLONE']
df_Madhya_Pradesh_3G_IDEA = df_Madhya_Pradesh_3G[df_Madhya_Pradesh_3G.Service_provider == 'IDEA']
df_Madhya_Pradesh_3G_VODAFONE = df_Madhya_Pradesh_3G[df_Madhya_Pradesh_3G.Service_provider == 'VODAFONE']

# [1-A]  Madhya_Pradesh  3G upload plotting

df_Madhya_Pradesh_3G_AIRTEL_upload = df_Madhya_Pradesh_3G_AIRTEL[df_Madhya_Pradesh_3G_AIRTEL.Download_Upload == 'upload']
df_Madhya_Pradesh_3G_CELLONE_upload = df_Madhya_Pradesh_3G_CELLONE[df_Madhya_Pradesh_3G_CELLONE.Download_Upload == 'upload']
df_Madhya_Pradesh_3G_IDEA_upload = df_Madhya_Pradesh_3G_IDEA[df_Madhya_Pradesh_3G_IDEA.Download_Upload == 'upload']
df_Madhya_Pradesh_3G_VODAFONE_upload = df_Madhya_Pradesh_3G_VODAFONE[df_Madhya_Pradesh_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Madhya_Pradesh_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Madhya_Pradesh_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Madhya_Pradesh_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Madhya_Pradesh_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Madhya_Pradesh  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Madhya_Pradesh_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Madhya_Pradesh_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Madhya_Pradesh_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Madhya_Pradesh_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Madhya_Pradesh  3G download plotting

                                                                                                                                                          
df_Madhya_Pradesh_3G_AIRTEL_download = df_Madhya_Pradesh_3G_AIRTEL[df_Madhya_Pradesh_3G_AIRTEL.Download_Upload == 'download']
df_Madhya_Pradesh_3G_CELLONE_download = df_Madhya_Pradesh_3G_CELLONE[df_Madhya_Pradesh_3G_CELLONE.Download_Upload == 'download']
df_Madhya_Pradesh_3G_IDEA_download = df_Madhya_Pradesh_3G_IDEA[df_Madhya_Pradesh_3G_IDEA.Download_Upload == 'download']
df_Madhya_Pradesh_3G_VODAFONE_download = df_Madhya_Pradesh_3G_VODAFONE[df_Madhya_Pradesh_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Madhya_Pradesh_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Madhya_Pradesh_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Madhya_Pradesh_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Madhya_Pradesh_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Madhya_Pradesh  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Madhya_Pradesh_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Madhya_Pradesh_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Madhya_Pradesh_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Madhya_Pradesh_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Madhya_Pradesh 4G operation

print("\n---: convert to  Madhya_Pradesh-4G operation :-------")
df_Madhya_Pradesh_4G = df_Madhya_Pradesh[df_Madhya_Pradesh.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Madhya_Pradesh_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Madhya_Pradesh_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Madhya_Pradesh 4G

df_Madhya_Pradesh_4G_sp = df_Madhya_Pradesh_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Madhya_Pradesh_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Madhya_Pradesh_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Madhya_Pradesh_4G_sp_AIRTEL
# df_Madhya_Pradesh_4G_sp_CELLONE                 
# df_Madhya_Pradesh_4G_sp_IDEA                     
# df_Madhya_Pradesh_4G_sp_VODAFONE 
# df_Madhya_Pradesh_4G_sp_JIO  

print("\n---:  Madhya_Pradesh-4G operation  :-------")

df_Madhya_Pradesh_4G_AIRTEL = df_Madhya_Pradesh_4G[df_Madhya_Pradesh_4G.Service_provider == 'AIRTEL']
df_Madhya_Pradesh_4G_CELLONE = df_Madhya_Pradesh_4G[df_Madhya_Pradesh_4G.Service_provider == 'CELLONE']
df_Madhya_Pradesh_4G_IDEA = df_Madhya_Pradesh_4G[df_Madhya_Pradesh_4G.Service_provider == 'IDEA']
df_Madhya_Pradesh_4G_VODAFONE = df_Madhya_Pradesh_4G[df_Madhya_Pradesh_4G.Service_provider == 'VODAFONE']
df_Madhya_Pradesh_4G_JIO = df_Madhya_Pradesh_4G[df_Madhya_Pradesh_4G.Service_provider == 'JIO']

#  Madhya_Pradesh  4G upload plotting

df_Madhya_Pradesh_4G_AIRTEL_upload = df_Madhya_Pradesh_4G_AIRTEL[df_Madhya_Pradesh_4G_AIRTEL.Download_Upload == 'upload']
df_Madhya_Pradesh_4G_CELLONE_upload = df_Madhya_Pradesh_4G_CELLONE[df_Madhya_Pradesh_4G_CELLONE.Download_Upload == 'upload']
df_Madhya_Pradesh_4G_IDEA_upload = df_Madhya_Pradesh_4G_IDEA[df_Madhya_Pradesh_4G_IDEA.Download_Upload == 'upload']
df_Madhya_Pradesh_4G_VODAFONE_upload = df_Madhya_Pradesh_4G_VODAFONE[df_Madhya_Pradesh_4G_VODAFONE.Download_Upload == 'upload']
df_Madhya_Pradesh_4G_JIO_upload = df_Madhya_Pradesh_4G_JIO[df_Madhya_Pradesh_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Madhya_Pradesh_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Madhya_Pradesh_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Madhya_Pradesh_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Madhya_Pradesh_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Madhya_Pradesh_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Madhya_Pradesh  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Madhya_Pradesh_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Madhya_Pradesh_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Madhya_Pradesh_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Madhya_Pradesh_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Madhya_Pradesh_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Madhya_Pradesh  4G download plotting
                                                                                                                                                          
df_Madhya_Pradesh_4G_AIRTEL_download = df_Madhya_Pradesh_4G_AIRTEL[df_Madhya_Pradesh_4G_AIRTEL.Download_Upload == 'download']
df_Madhya_Pradesh_4G_CELLONE_download = df_Madhya_Pradesh_4G_CELLONE[df_Madhya_Pradesh_4G_CELLONE.Download_Upload == 'download']
df_Madhya_Pradesh_4G_IDEA_download = df_Madhya_Pradesh_4G_IDEA[df_Madhya_Pradesh_4G_IDEA.Download_Upload == 'download']
df_Madhya_Pradesh_4G_VODAFONE_download = df_Madhya_Pradesh_4G_VODAFONE[df_Madhya_Pradesh_4G_VODAFONE.Download_Upload == 'download']
df_Madhya_Pradesh_4G_JIO_download = df_Madhya_Pradesh_4G_JIO[df_Madhya_Pradesh_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Madhya_Pradesh_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Madhya_Pradesh_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Madhya_Pradesh_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Madhya_Pradesh_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Madhya_Pradesh_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Madhya_Pradesh  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Madhya_Pradesh_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Madhya_Pradesh_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Madhya_Pradesh_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Madhya_Pradesh_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Madhya_Pradesh_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                              
                                       
# [14] Maharashtra 




print("\n---: [14]  Maharastra operation :-------")
df_Maharastra = df[df.Service_Area == 'Maharashtra']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Maharastra.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Maharastra.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Maharastra 

techno_Maharastra = df_Maharastra.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Maharastra)
print("-------------------------------")
count = 0
for row in range(len(techno_Maharastra)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Maharastra 3G operation

print("\n---: convert to  Maharastra-3G operation :-------")
df_Maharastra_3G = df_Maharastra[df_Maharastra.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Maharastra_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Maharastra_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Maharastra 3G

df_Maharastra_3G_sp = df_Maharastra_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Maharastra_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Maharastra_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Maharastra_3G_sp_AIRTEL
# df_Maharastra_3G_sp_CELLONE                 
# df_Maharastra_3G_sp_IDEA                     
# df_Maharastra_3G_sp_VODAFONE   

print("\n---:  Maharastra-3G operation  :-------")

df_Maharastra_3G_AIRTEL = df_Maharastra_3G[df_Maharastra_3G.Service_provider == 'AIRTEL']
df_Maharastra_3G_CELLONE = df_Maharastra_3G[df_Maharastra_3G.Service_provider == 'CELLONE']
df_Maharastra_3G_IDEA = df_Maharastra_3G[df_Maharastra_3G.Service_provider == 'IDEA']
df_Maharastra_3G_VODAFONE = df_Maharastra_3G[df_Maharastra_3G.Service_provider == 'VODAFONE']

# [1-A]  Maharastra  3G upload plotting

df_Maharastra_3G_AIRTEL_upload = df_Maharastra_3G_AIRTEL[df_Maharastra_3G_AIRTEL.Download_Upload == 'upload']
df_Maharastra_3G_CELLONE_upload = df_Maharastra_3G_CELLONE[df_Maharastra_3G_CELLONE.Download_Upload == 'upload']
df_Maharastra_3G_IDEA_upload = df_Maharastra_3G_IDEA[df_Maharastra_3G_IDEA.Download_Upload == 'upload']
df_Maharastra_3G_VODAFONE_upload = df_Maharastra_3G_VODAFONE[df_Maharastra_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Maharastra_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Maharastra_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Maharastra_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Maharastra_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Maharastra  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Maharastra_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Maharastra_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Maharastra_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Maharastra_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Maharastra  3G download plotting

                                                                                                                                                          
df_Maharastra_3G_AIRTEL_download = df_Maharastra_3G_AIRTEL[df_Maharastra_3G_AIRTEL.Download_Upload == 'download']
df_Maharastra_3G_CELLONE_download = df_Maharastra_3G_CELLONE[df_Maharastra_3G_CELLONE.Download_Upload == 'download']
df_Maharastra_3G_IDEA_download = df_Maharastra_3G_IDEA[df_Maharastra_3G_IDEA.Download_Upload == 'download']
df_Maharastra_3G_VODAFONE_download = df_Maharastra_3G_VODAFONE[df_Maharastra_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Maharastra_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Maharastra_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Maharastra_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Maharastra_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Maharastra  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Maharastra_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Maharastra_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Maharastra_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Maharastra_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Maharastra 4G operation

print("\n---: convert to  Maharastra-4G operation :-------")
df_Maharastra_4G = df_Maharastra[df_Maharastra.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Maharastra_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Maharastra_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Maharastra 4G

df_Maharastra_4G_sp = df_Maharastra_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Maharastra_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Maharastra_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Maharastra_4G_sp_AIRTEL
# df_Maharastra_4G_sp_CELLONE                 
# df_Maharastra_4G_sp_IDEA                     
# df_Maharastra_4G_sp_VODAFONE 
# df_Maharastra_4G_sp_JIO  

print("\n---:  Maharastra-4G operation  :-------")

df_Maharastra_4G_AIRTEL = df_Maharastra_4G[df_Maharastra_4G.Service_provider == 'AIRTEL']
df_Maharastra_4G_CELLONE = df_Maharastra_4G[df_Maharastra_4G.Service_provider == 'CELLONE']
df_Maharastra_4G_IDEA = df_Maharastra_4G[df_Maharastra_4G.Service_provider == 'IDEA']
df_Maharastra_4G_VODAFONE = df_Maharastra_4G[df_Maharastra_4G.Service_provider == 'VODAFONE']
df_Maharastra_4G_JIO = df_Maharastra_4G[df_Maharastra_4G.Service_provider == 'JIO']

#  Maharastra  4G upload plotting

df_Maharastra_4G_AIRTEL_upload = df_Maharastra_4G_AIRTEL[df_Maharastra_4G_AIRTEL.Download_Upload == 'upload']
df_Maharastra_4G_CELLONE_upload = df_Maharastra_4G_CELLONE[df_Maharastra_4G_CELLONE.Download_Upload == 'upload']
df_Maharastra_4G_IDEA_upload = df_Maharastra_4G_IDEA[df_Maharastra_4G_IDEA.Download_Upload == 'upload']
df_Maharastra_4G_VODAFONE_upload = df_Maharastra_4G_VODAFONE[df_Maharastra_4G_VODAFONE.Download_Upload == 'upload']
df_Maharastra_4G_JIO_upload = df_Maharastra_4G_JIO[df_Maharastra_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Maharastra_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Maharastra_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Maharastra_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Maharastra_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Maharastra_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Maharastra  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Maharastra_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Maharastra_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Maharastra_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Maharastra_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Maharastra_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Maharastra  4G download plotting
                                                                                                                                                          
df_Maharastra_4G_AIRTEL_download = df_Maharastra_4G_AIRTEL[df_Maharastra_4G_AIRTEL.Download_Upload == 'download']
df_Maharastra_4G_CELLONE_download = df_Maharastra_4G_CELLONE[df_Maharastra_4G_CELLONE.Download_Upload == 'download']
df_Maharastra_4G_IDEA_download = df_Maharastra_4G_IDEA[df_Maharastra_4G_IDEA.Download_Upload == 'download']
df_Maharastra_4G_VODAFONE_download = df_Maharastra_4G_VODAFONE[df_Maharastra_4G_VODAFONE.Download_Upload == 'download']
df_Maharastra_4G_JIO_download = df_Maharastra_4G_JIO[df_Maharastra_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Maharastra_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Maharastra_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Maharastra_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Maharastra_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Maharastra_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Maharastra  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Maharastra_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Maharastra_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Maharastra_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Maharastra_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Maharastra_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                 
                                                
# [15] Mumbai 




print("\n---: [15]  Mumbai operation :-------")
df_Mumbai = df[df.Service_Area == 'Mumbai']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Mumbai.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Mumbai.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Mumbai 

techno_Mumbai = df_Mumbai.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Mumbai)
print("-------------------------------")
count = 0
for row in range(len(techno_Mumbai)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Mumbai 3G operation

print("\n---: convert to  Mumbai-3G operation :-------")
df_Mumbai_3G = df_Mumbai[df_Mumbai.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Mumbai_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Mumbai_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Mumbai 3G

df_Mumbai_3G_sp = df_Mumbai_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Mumbai_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Mumbai_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Mumbai_3G_sp_AIRTEL
# df_Mumbai_3G_sp_CELLONE                 
# df_Mumbai_3G_sp_IDEA                     
# df_Mumbai_3G_sp_VODAFONE   

print("\n---:  Mumbai-3G operation  :-------")

df_Mumbai_3G_AIRTEL = df_Mumbai_3G[df_Mumbai_3G.Service_provider == 'AIRTEL']
df_Mumbai_3G_CELLONE = df_Mumbai_3G[df_Mumbai_3G.Service_provider == 'CELLONE']
df_Mumbai_3G_IDEA = df_Mumbai_3G[df_Mumbai_3G.Service_provider == 'IDEA']
df_Mumbai_3G_VODAFONE = df_Mumbai_3G[df_Mumbai_3G.Service_provider == 'VODAFONE']

# [1-A]  Mumbai  3G upload plotting

df_Mumbai_3G_AIRTEL_upload = df_Mumbai_3G_AIRTEL[df_Mumbai_3G_AIRTEL.Download_Upload == 'upload']
df_Mumbai_3G_CELLONE_upload = df_Mumbai_3G_CELLONE[df_Mumbai_3G_CELLONE.Download_Upload == 'upload']
df_Mumbai_3G_IDEA_upload = df_Mumbai_3G_IDEA[df_Mumbai_3G_IDEA.Download_Upload == 'upload']
df_Mumbai_3G_VODAFONE_upload = df_Mumbai_3G_VODAFONE[df_Mumbai_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Mumbai_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Mumbai_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Mumbai_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Mumbai_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Mumbai  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Mumbai_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Mumbai_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Mumbai_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Mumbai_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Mumbai  3G download plotting

                                                                                                                                                          
df_Mumbai_3G_AIRTEL_download = df_Mumbai_3G_AIRTEL[df_Mumbai_3G_AIRTEL.Download_Upload == 'download']
df_Mumbai_3G_CELLONE_download = df_Mumbai_3G_CELLONE[df_Mumbai_3G_CELLONE.Download_Upload == 'download']
df_Mumbai_3G_IDEA_download = df_Mumbai_3G_IDEA[df_Mumbai_3G_IDEA.Download_Upload == 'download']
df_Mumbai_3G_VODAFONE_download = df_Mumbai_3G_VODAFONE[df_Mumbai_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Mumbai_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Mumbai_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Mumbai_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Mumbai_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Mumbai  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Mumbai_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Mumbai_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Mumbai_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Mumbai_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Mumbai 4G operation

print("\n---: convert to  Mumbai-4G operation :-------")
df_Mumbai_4G = df_Mumbai[df_Mumbai.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Mumbai_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Mumbai_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Mumbai 4G

df_Mumbai_4G_sp = df_Mumbai_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Mumbai_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Mumbai_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Mumbai_4G_sp_AIRTEL
# df_Mumbai_4G_sp_CELLONE                 
# df_Mumbai_4G_sp_IDEA                     
# df_Mumbai_4G_sp_VODAFONE 
# df_Mumbai_4G_sp_JIO  

print("\n---:  Mumbai-4G operation  :-------")

df_Mumbai_4G_AIRTEL = df_Mumbai_4G[df_Mumbai_4G.Service_provider == 'AIRTEL']
df_Mumbai_4G_CELLONE = df_Mumbai_4G[df_Mumbai_4G.Service_provider == 'CELLONE']
df_Mumbai_4G_IDEA = df_Mumbai_4G[df_Mumbai_4G.Service_provider == 'IDEA']
df_Mumbai_4G_VODAFONE = df_Mumbai_4G[df_Mumbai_4G.Service_provider == 'VODAFONE']
df_Mumbai_4G_JIO = df_Mumbai_4G[df_Mumbai_4G.Service_provider == 'JIO']

#  Mumbai  4G upload plotting

df_Mumbai_4G_AIRTEL_upload = df_Mumbai_4G_AIRTEL[df_Mumbai_4G_AIRTEL.Download_Upload == 'upload']
df_Mumbai_4G_CELLONE_upload = df_Mumbai_4G_CELLONE[df_Mumbai_4G_CELLONE.Download_Upload == 'upload']
df_Mumbai_4G_IDEA_upload = df_Mumbai_4G_IDEA[df_Mumbai_4G_IDEA.Download_Upload == 'upload']
df_Mumbai_4G_VODAFONE_upload = df_Mumbai_4G_VODAFONE[df_Mumbai_4G_VODAFONE.Download_Upload == 'upload']
df_Mumbai_4G_JIO_upload = df_Mumbai_4G_JIO[df_Mumbai_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Mumbai_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Mumbai_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Mumbai_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Mumbai_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Mumbai_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Mumbai  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Mumbai_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Mumbai_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Mumbai_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Mumbai_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Mumbai_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Mumbai  4G download plotting
                                                                                                                                                          
df_Mumbai_4G_AIRTEL_download = df_Mumbai_4G_AIRTEL[df_Mumbai_4G_AIRTEL.Download_Upload == 'download']
df_Mumbai_4G_CELLONE_download = df_Mumbai_4G_CELLONE[df_Mumbai_4G_CELLONE.Download_Upload == 'download']
df_Mumbai_4G_IDEA_download = df_Mumbai_4G_IDEA[df_Mumbai_4G_IDEA.Download_Upload == 'download']
df_Mumbai_4G_VODAFONE_download = df_Mumbai_4G_VODAFONE[df_Mumbai_4G_VODAFONE.Download_Upload == 'download']
df_Mumbai_4G_JIO_download = df_Mumbai_4G_JIO[df_Mumbai_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Mumbai_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Mumbai_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Mumbai_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Mumbai_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Mumbai_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Mumbai  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Mumbai_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Mumbai_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Mumbai_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Mumbai_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Mumbai_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                      
                                                               
# [16] North East




print("\n---: [16]  North_East operation :-------")
df_North_East = df[df.Service_Area == 'North East']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_North_East.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_North_East.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  North_East 

techno_North_East = df_North_East.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_North_East)
print("-------------------------------")
count = 0
for row in range(len(techno_North_East)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  North_East 3G operation

print("\n---: convert to  North_East-3G operation :-------")
df_North_East_3G = df_North_East[df_North_East.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_North_East_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_North_East_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  North_East 3G

df_North_East_3G_sp = df_North_East_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_North_East_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_North_East_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_North_East_3G_sp_AIRTEL
# df_North_East_3G_sp_CELLONE                 
# df_North_East_3G_sp_IDEA                     
# df_North_East_3G_sp_VODAFONE   

print("\n---:  North_East-3G operation  :-------")

df_North_East_3G_AIRTEL = df_North_East_3G[df_North_East_3G.Service_provider == 'AIRTEL']
df_North_East_3G_CELLONE = df_North_East_3G[df_North_East_3G.Service_provider == 'CELLONE']
df_North_East_3G_IDEA = df_North_East_3G[df_North_East_3G.Service_provider == 'IDEA']
df_North_East_3G_VODAFONE = df_North_East_3G[df_North_East_3G.Service_provider == 'VODAFONE']

# [1-A]  North_East  3G upload plotting

df_North_East_3G_AIRTEL_upload = df_North_East_3G_AIRTEL[df_North_East_3G_AIRTEL.Download_Upload == 'upload']
df_North_East_3G_CELLONE_upload = df_North_East_3G_CELLONE[df_North_East_3G_CELLONE.Download_Upload == 'upload']
df_North_East_3G_IDEA_upload = df_North_East_3G_IDEA[df_North_East_3G_IDEA.Download_Upload == 'upload']
df_North_East_3G_VODAFONE_upload = df_North_East_3G_VODAFONE[df_North_East_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_North_East_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_North_East_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_North_East_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_North_East_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  North_East  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_North_East_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_North_East_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_North_East_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_North_East_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  North_East  3G download plotting

                                                                                                                                                          
df_North_East_3G_AIRTEL_download = df_North_East_3G_AIRTEL[df_North_East_3G_AIRTEL.Download_Upload == 'download']
df_North_East_3G_CELLONE_download = df_North_East_3G_CELLONE[df_North_East_3G_CELLONE.Download_Upload == 'download']
df_North_East_3G_IDEA_download = df_North_East_3G_IDEA[df_North_East_3G_IDEA.Download_Upload == 'download']
df_North_East_3G_VODAFONE_download = df_North_East_3G_VODAFONE[df_North_East_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_North_East_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_North_East_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_North_East_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_North_East_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  North_East  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_North_East_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_North_East_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_North_East_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_North_East_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  North_East 4G operation

print("\n---: convert to  North_East-4G operation :-------")
df_North_East_4G = df_North_East[df_North_East.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_North_East_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_North_East_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  North_East 4G

df_North_East_4G_sp = df_North_East_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_North_East_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_North_East_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_North_East_4G_sp_AIRTEL
# df_North_East_4G_sp_CELLONE                 
# df_North_East_4G_sp_IDEA                     
# df_North_East_4G_sp_VODAFONE 
# df_North_East_4G_sp_JIO  

print("\n---:  North_East-4G operation  :-------")

df_North_East_4G_AIRTEL = df_North_East_4G[df_North_East_4G.Service_provider == 'AIRTEL']
df_North_East_4G_CELLONE = df_North_East_4G[df_North_East_4G.Service_provider == 'CELLONE']
df_North_East_4G_IDEA = df_North_East_4G[df_North_East_4G.Service_provider == 'IDEA']
df_North_East_4G_VODAFONE = df_North_East_4G[df_North_East_4G.Service_provider == 'VODAFONE']
df_North_East_4G_JIO = df_North_East_4G[df_North_East_4G.Service_provider == 'JIO']

#  North_East  4G upload plotting

df_North_East_4G_AIRTEL_upload = df_North_East_4G_AIRTEL[df_North_East_4G_AIRTEL.Download_Upload == 'upload']
df_North_East_4G_CELLONE_upload = df_North_East_4G_CELLONE[df_North_East_4G_CELLONE.Download_Upload == 'upload']
df_North_East_4G_IDEA_upload = df_North_East_4G_IDEA[df_North_East_4G_IDEA.Download_Upload == 'upload']
df_North_East_4G_VODAFONE_upload = df_North_East_4G_VODAFONE[df_North_East_4G_VODAFONE.Download_Upload == 'upload']
df_North_East_4G_JIO_upload = df_North_East_4G_JIO[df_North_East_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_North_East_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_North_East_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_North_East_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_North_East_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_North_East_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  North_East  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_North_East_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_North_East_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_North_East_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_North_East_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_North_East_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  North_East  4G download plotting
                                                                                                                                                          
df_North_East_4G_AIRTEL_download = df_North_East_4G_AIRTEL[df_North_East_4G_AIRTEL.Download_Upload == 'download']
df_North_East_4G_CELLONE_download = df_North_East_4G_CELLONE[df_North_East_4G_CELLONE.Download_Upload == 'download']
df_North_East_4G_IDEA_download = df_North_East_4G_IDEA[df_North_East_4G_IDEA.Download_Upload == 'download']
df_North_East_4G_VODAFONE_download = df_North_East_4G_VODAFONE[df_North_East_4G_VODAFONE.Download_Upload == 'download']
df_North_East_4G_JIO_download = df_North_East_4G_JIO[df_North_East_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_North_East_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_North_East_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_North_East_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_North_East_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_North_East_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  North_East  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_North_East_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_North_East_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_North_East_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_North_East_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_North_East_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                    
                                                         
# [17] Orissa 




print("\n---: [17]  Orissa operation :-------")

df_Orissa = df[df.Service_Area == 'Orissa']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Orissa.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Orissa.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Orissa 

techno_Orissa = df_Orissa.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Orissa)
print("-------------------------------")
count = 0
for row in range(len(techno_Orissa)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Orissa 3G operation

print("\n---: convert to  Orissa-3G operation :-------")
df_Orissa_3G = df_Orissa[df_Orissa.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Orissa_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Orissa_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Orissa 3G

df_Orissa_3G_sp = df_Orissa_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Orissa_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Orissa_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Orissa_3G_sp_AIRTEL
# df_Orissa_3G_sp_CELLONE                 
# df_Orissa_3G_sp_IDEA                     
# df_Orissa_3G_sp_VODAFONE   

print("\n---:  Orissa-3G operation  :-------")

df_Orissa_3G_AIRTEL = df_Orissa_3G[df_Orissa_3G.Service_provider == 'AIRTEL']
df_Orissa_3G_CELLONE = df_Orissa_3G[df_Orissa_3G.Service_provider == 'CELLONE']
df_Orissa_3G_IDEA = df_Orissa_3G[df_Orissa_3G.Service_provider == 'IDEA']
df_Orissa_3G_VODAFONE = df_Orissa_3G[df_Orissa_3G.Service_provider == 'VODAFONE']

# [1-A]  Orissa  3G upload plotting

df_Orissa_3G_AIRTEL_upload = df_Orissa_3G_AIRTEL[df_Orissa_3G_AIRTEL.Download_Upload == 'upload']
df_Orissa_3G_CELLONE_upload = df_Orissa_3G_CELLONE[df_Orissa_3G_CELLONE.Download_Upload == 'upload']
df_Orissa_3G_IDEA_upload = df_Orissa_3G_IDEA[df_Orissa_3G_IDEA.Download_Upload == 'upload']
df_Orissa_3G_VODAFONE_upload = df_Orissa_3G_VODAFONE[df_Orissa_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Orissa_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Orissa_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Orissa_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Orissa_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Orissa  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Orissa_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Orissa_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Orissa_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Orissa_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Orissa  3G download plotting

                                                                                                                                                          
df_Orissa_3G_AIRTEL_download = df_Orissa_3G_AIRTEL[df_Orissa_3G_AIRTEL.Download_Upload == 'download']
df_Orissa_3G_CELLONE_download = df_Orissa_3G_CELLONE[df_Orissa_3G_CELLONE.Download_Upload == 'download']
df_Orissa_3G_IDEA_download = df_Orissa_3G_IDEA[df_Orissa_3G_IDEA.Download_Upload == 'download']
df_Orissa_3G_VODAFONE_download = df_Orissa_3G_VODAFONE[df_Orissa_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Orissa_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Orissa_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Orissa_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Orissa_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Orissa  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Orissa_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Orissa_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Orissa_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Orissa_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Orissa 4G operation

print("\n---: convert to  Orissa-4G operation :-------")
df_Orissa_4G = df_Orissa[df_Orissa.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Orissa_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Orissa_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Orissa 4G

df_Orissa_4G_sp = df_Orissa_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Orissa_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Orissa_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Orissa_4G_sp_AIRTEL
# df_Orissa_4G_sp_CELLONE                 
# df_Orissa_4G_sp_IDEA                     
# df_Orissa_4G_sp_VODAFONE 
# df_Orissa_4G_sp_JIO  

print("\n---:  Orissa-4G operation  :-------")

df_Orissa_4G_AIRTEL = df_Orissa_4G[df_Orissa_4G.Service_provider == 'AIRTEL']
df_Orissa_4G_CELLONE = df_Orissa_4G[df_Orissa_4G.Service_provider == 'CELLONE']
df_Orissa_4G_IDEA = df_Orissa_4G[df_Orissa_4G.Service_provider == 'IDEA']
df_Orissa_4G_VODAFONE = df_Orissa_4G[df_Orissa_4G.Service_provider == 'VODAFONE']
df_Orissa_4G_JIO = df_Orissa_4G[df_Orissa_4G.Service_provider == 'JIO']

#  Orissa  4G upload plotting

df_Orissa_4G_AIRTEL_upload = df_Orissa_4G_AIRTEL[df_Orissa_4G_AIRTEL.Download_Upload == 'upload']
df_Orissa_4G_CELLONE_upload = df_Orissa_4G_CELLONE[df_Orissa_4G_CELLONE.Download_Upload == 'upload']
df_Orissa_4G_IDEA_upload = df_Orissa_4G_IDEA[df_Orissa_4G_IDEA.Download_Upload == 'upload']
df_Orissa_4G_VODAFONE_upload = df_Orissa_4G_VODAFONE[df_Orissa_4G_VODAFONE.Download_Upload == 'upload']
df_Orissa_4G_JIO_upload = df_Orissa_4G_JIO[df_Orissa_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Orissa_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Orissa_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Orissa_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Orissa_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Orissa_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Orissa  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Orissa_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Orissa_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Orissa_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Orissa_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Orissa_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Orissa  4G download plotting
                                                                                                                                                          
df_Orissa_4G_AIRTEL_download = df_Orissa_4G_AIRTEL[df_Orissa_4G_AIRTEL.Download_Upload == 'download']
df_Orissa_4G_CELLONE_download = df_Orissa_4G_CELLONE[df_Orissa_4G_CELLONE.Download_Upload == 'download']
df_Orissa_4G_IDEA_download = df_Orissa_4G_IDEA[df_Orissa_4G_IDEA.Download_Upload == 'download']
df_Orissa_4G_VODAFONE_download = df_Orissa_4G_VODAFONE[df_Orissa_4G_VODAFONE.Download_Upload == 'download']
df_Orissa_4G_JIO_download = df_Orissa_4G_JIO[df_Orissa_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Orissa_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Orissa_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Orissa_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Orissa_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Orissa_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Orissa  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Orissa_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Orissa_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Orissa_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Orissa_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Orissa_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                      
                                                               
# [18] Punjab




print("\n---: [18]  Punjab operation :-------")

df_Punjab = df[df.Service_Area == 'Punjab']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Punjab.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Punjab.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Punjab 

techno_Punjab = df_Punjab.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Punjab)
print("-------------------------------")
count = 0
for row in range(len(techno_Punjab)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Punjab 3G operation

print("\n---: convert to  Punjab-3G operation :-------")
df_Punjab_3G = df_Punjab[df_Punjab.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Punjab_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Punjab_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Punjab 3G

df_Punjab_3G_sp = df_Punjab_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Punjab_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Punjab_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Punjab_3G_sp_AIRTEL
# df_Punjab_3G_sp_CELLONE                 
# df_Punjab_3G_sp_IDEA                     
# df_Punjab_3G_sp_VODAFONE   

print("\n---:  Punjab-3G operation  :-------")

df_Punjab_3G_AIRTEL = df_Punjab_3G[df_Punjab_3G.Service_provider == 'AIRTEL']
df_Punjab_3G_CELLONE = df_Punjab_3G[df_Punjab_3G.Service_provider == 'CELLONE']
df_Punjab_3G_IDEA = df_Punjab_3G[df_Punjab_3G.Service_provider == 'IDEA']
df_Punjab_3G_VODAFONE = df_Punjab_3G[df_Punjab_3G.Service_provider == 'VODAFONE']

# [1-A]  Punjab  3G upload plotting

df_Punjab_3G_AIRTEL_upload = df_Punjab_3G_AIRTEL[df_Punjab_3G_AIRTEL.Download_Upload == 'upload']
df_Punjab_3G_CELLONE_upload = df_Punjab_3G_CELLONE[df_Punjab_3G_CELLONE.Download_Upload == 'upload']
df_Punjab_3G_IDEA_upload = df_Punjab_3G_IDEA[df_Punjab_3G_IDEA.Download_Upload == 'upload']
df_Punjab_3G_VODAFONE_upload = df_Punjab_3G_VODAFONE[df_Punjab_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Punjab_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Punjab_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Punjab_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Punjab_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Punjab  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Punjab_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Punjab_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Punjab_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Punjab_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Punjab  3G download plotting

                                                                                                                                                          
df_Punjab_3G_AIRTEL_download = df_Punjab_3G_AIRTEL[df_Punjab_3G_AIRTEL.Download_Upload == 'download']
df_Punjab_3G_CELLONE_download = df_Punjab_3G_CELLONE[df_Punjab_3G_CELLONE.Download_Upload == 'download']
df_Punjab_3G_IDEA_download = df_Punjab_3G_IDEA[df_Punjab_3G_IDEA.Download_Upload == 'download']
df_Punjab_3G_VODAFONE_download = df_Punjab_3G_VODAFONE[df_Punjab_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Punjab_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Punjab_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Punjab_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Punjab_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Punjab  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Punjab_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Punjab_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Punjab_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Punjab_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Punjab 4G operation

print("\n---: convert to  Punjab-4G operation :-------")
df_Punjab_4G = df_Punjab[df_Punjab.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Punjab_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Punjab_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Punjab 4G

df_Punjab_4G_sp = df_Punjab_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Punjab_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Punjab_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Punjab_4G_sp_AIRTEL
# df_Punjab_4G_sp_CELLONE                 
# df_Punjab_4G_sp_IDEA                     
# df_Punjab_4G_sp_VODAFONE 
# df_Punjab_4G_sp_JIO  

print("\n---:  Punjab-4G operation  :-------")

df_Punjab_4G_AIRTEL = df_Punjab_4G[df_Punjab_4G.Service_provider == 'AIRTEL']
df_Punjab_4G_CELLONE = df_Punjab_4G[df_Punjab_4G.Service_provider == 'CELLONE']
df_Punjab_4G_IDEA = df_Punjab_4G[df_Punjab_4G.Service_provider == 'IDEA']
df_Punjab_4G_VODAFONE = df_Punjab_4G[df_Punjab_4G.Service_provider == 'VODAFONE']
df_Punjab_4G_JIO = df_Punjab_4G[df_Punjab_4G.Service_provider == 'JIO']

#  Punjab  4G upload plotting

df_Punjab_4G_AIRTEL_upload = df_Punjab_4G_AIRTEL[df_Punjab_4G_AIRTEL.Download_Upload == 'upload']
df_Punjab_4G_CELLONE_upload = df_Punjab_4G_CELLONE[df_Punjab_4G_CELLONE.Download_Upload == 'upload']
df_Punjab_4G_IDEA_upload = df_Punjab_4G_IDEA[df_Punjab_4G_IDEA.Download_Upload == 'upload']
df_Punjab_4G_VODAFONE_upload = df_Punjab_4G_VODAFONE[df_Punjab_4G_VODAFONE.Download_Upload == 'upload']
df_Punjab_4G_JIO_upload = df_Punjab_4G_JIO[df_Punjab_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Punjab_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Punjab_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Punjab_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Punjab_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Punjab_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Punjab  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Punjab_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Punjab_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Punjab_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Punjab_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Punjab_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Punjab  4G download plotting
                                                                                                                                                          
df_Punjab_4G_AIRTEL_download = df_Punjab_4G_AIRTEL[df_Punjab_4G_AIRTEL.Download_Upload == 'download']
df_Punjab_4G_CELLONE_download = df_Punjab_4G_CELLONE[df_Punjab_4G_CELLONE.Download_Upload == 'download']
df_Punjab_4G_IDEA_download = df_Punjab_4G_IDEA[df_Punjab_4G_IDEA.Download_Upload == 'download']
df_Punjab_4G_VODAFONE_download = df_Punjab_4G_VODAFONE[df_Punjab_4G_VODAFONE.Download_Upload == 'download']
df_Punjab_4G_JIO_download = df_Punjab_4G_JIO[df_Punjab_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Punjab_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Punjab_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Punjab_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Punjab_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Punjab_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Punjab  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Punjab_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Punjab_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Punjab_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Punjab_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Punjab_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                       
                                                                  
# [19] Rajasthan 




print("\n---: [19]  Rajasthan operation :-------")

df_Rajasthan = df[df.Service_Area == 'Rajasthan']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Rajasthan.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Rajasthan.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Rajasthan 

techno_Rajasthan = df_Rajasthan.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Rajasthan)
print("-------------------------------")
count = 0
for row in range(len(techno_Rajasthan)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Rajasthan 3G operation

print("\n---: convert to  Rajasthan-3G operation :-------")
df_Rajasthan_3G = df_Rajasthan[df_Rajasthan.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Rajasthan_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Rajasthan_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Rajasthan 3G

df_Rajasthan_3G_sp = df_Rajasthan_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Rajasthan_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Rajasthan_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Rajasthan_3G_sp_AIRTEL
# df_Rajasthan_3G_sp_CELLONE                 
# df_Rajasthan_3G_sp_IDEA                     
# df_Rajasthan_3G_sp_VODAFONE   

print("\n---:  Rajasthan-3G operation  :-------")

df_Rajasthan_3G_AIRTEL = df_Rajasthan_3G[df_Rajasthan_3G.Service_provider == 'AIRTEL']
df_Rajasthan_3G_CELLONE = df_Rajasthan_3G[df_Rajasthan_3G.Service_provider == 'CELLONE']
df_Rajasthan_3G_IDEA = df_Rajasthan_3G[df_Rajasthan_3G.Service_provider == 'IDEA']
df_Rajasthan_3G_VODAFONE = df_Rajasthan_3G[df_Rajasthan_3G.Service_provider == 'VODAFONE']

# [1-A]  Rajasthan  3G upload plotting

df_Rajasthan_3G_AIRTEL_upload = df_Rajasthan_3G_AIRTEL[df_Rajasthan_3G_AIRTEL.Download_Upload == 'upload']
df_Rajasthan_3G_CELLONE_upload = df_Rajasthan_3G_CELLONE[df_Rajasthan_3G_CELLONE.Download_Upload == 'upload']
df_Rajasthan_3G_IDEA_upload = df_Rajasthan_3G_IDEA[df_Rajasthan_3G_IDEA.Download_Upload == 'upload']
df_Rajasthan_3G_VODAFONE_upload = df_Rajasthan_3G_VODAFONE[df_Rajasthan_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Rajasthan_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Rajasthan_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Rajasthan_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Rajasthan_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Rajasthan  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Rajasthan_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Rajasthan_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Rajasthan_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Rajasthan_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Rajasthan  3G download plotting

                                                                                                                                                          
df_Rajasthan_3G_AIRTEL_download = df_Rajasthan_3G_AIRTEL[df_Rajasthan_3G_AIRTEL.Download_Upload == 'download']
df_Rajasthan_3G_CELLONE_download = df_Rajasthan_3G_CELLONE[df_Rajasthan_3G_CELLONE.Download_Upload == 'download']
df_Rajasthan_3G_IDEA_download = df_Rajasthan_3G_IDEA[df_Rajasthan_3G_IDEA.Download_Upload == 'download']
df_Rajasthan_3G_VODAFONE_download = df_Rajasthan_3G_VODAFONE[df_Rajasthan_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Rajasthan_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Rajasthan_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Rajasthan_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Rajasthan_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Rajasthan  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Rajasthan_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Rajasthan_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Rajasthan_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Rajasthan_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Rajasthan 4G operation

print("\n---: convert to  Rajasthan-4G operation :-------")
df_Rajasthan_4G = df_Rajasthan[df_Rajasthan.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Rajasthan_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Rajasthan_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Rajasthan 4G

df_Rajasthan_4G_sp = df_Rajasthan_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Rajasthan_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Rajasthan_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Rajasthan_4G_sp_AIRTEL
# df_Rajasthan_4G_sp_CELLONE                 
# df_Rajasthan_4G_sp_IDEA                     
# df_Rajasthan_4G_sp_VODAFONE 
# df_Rajasthan_4G_sp_JIO  

print("\n---:  Rajasthan-4G operation  :-------")

df_Rajasthan_4G_AIRTEL = df_Rajasthan_4G[df_Rajasthan_4G.Service_provider == 'AIRTEL']
df_Rajasthan_4G_CELLONE = df_Rajasthan_4G[df_Rajasthan_4G.Service_provider == 'CELLONE']
df_Rajasthan_4G_IDEA = df_Rajasthan_4G[df_Rajasthan_4G.Service_provider == 'IDEA']
df_Rajasthan_4G_VODAFONE = df_Rajasthan_4G[df_Rajasthan_4G.Service_provider == 'VODAFONE']
df_Rajasthan_4G_JIO = df_Rajasthan_4G[df_Rajasthan_4G.Service_provider == 'JIO']

#  Rajasthan  4G upload plotting

df_Rajasthan_4G_AIRTEL_upload = df_Rajasthan_4G_AIRTEL[df_Rajasthan_4G_AIRTEL.Download_Upload == 'upload']
df_Rajasthan_4G_CELLONE_upload = df_Rajasthan_4G_CELLONE[df_Rajasthan_4G_CELLONE.Download_Upload == 'upload']
df_Rajasthan_4G_IDEA_upload = df_Rajasthan_4G_IDEA[df_Rajasthan_4G_IDEA.Download_Upload == 'upload']
df_Rajasthan_4G_VODAFONE_upload = df_Rajasthan_4G_VODAFONE[df_Rajasthan_4G_VODAFONE.Download_Upload == 'upload']
df_Rajasthan_4G_JIO_upload = df_Rajasthan_4G_JIO[df_Rajasthan_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Rajasthan_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Rajasthan_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Rajasthan_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Rajasthan_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Rajasthan_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Rajasthan  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Rajasthan_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Rajasthan_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Rajasthan_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Rajasthan_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Rajasthan_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Rajasthan  4G download plotting
                                                                                                                                                          
df_Rajasthan_4G_AIRTEL_download = df_Rajasthan_4G_AIRTEL[df_Rajasthan_4G_AIRTEL.Download_Upload == 'download']
df_Rajasthan_4G_CELLONE_download = df_Rajasthan_4G_CELLONE[df_Rajasthan_4G_CELLONE.Download_Upload == 'download']
df_Rajasthan_4G_IDEA_download = df_Rajasthan_4G_IDEA[df_Rajasthan_4G_IDEA.Download_Upload == 'download']
df_Rajasthan_4G_VODAFONE_download = df_Rajasthan_4G_VODAFONE[df_Rajasthan_4G_VODAFONE.Download_Upload == 'download']
df_Rajasthan_4G_JIO_download = df_Rajasthan_4G_JIO[df_Rajasthan_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Rajasthan_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Rajasthan_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Rajasthan_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Rajasthan_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Rajasthan_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Rajasthan  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Rajasthan_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Rajasthan_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Rajasthan_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Rajasthan_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Rajasthan_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                   
                                                      
# [20] Tamil Nadu  




print("\n---: [20]  Tamil_Nadu operation :-------")

df_Tamil_Nadu = df[df.Service_Area == 'Tamil Nadu']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Tamil_Nadu.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Tamil_Nadu.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  Tamil_Nadu 

techno_Tamil_Nadu = df_Tamil_Nadu.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_Tamil_Nadu)
print("-------------------------------")
count = 0
for row in range(len(techno_Tamil_Nadu)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  Tamil_Nadu 3G operation

print("\n---: convert to  Tamil_Nadu-3G operation :-------")
df_Tamil_Nadu_3G = df_Tamil_Nadu[df_Tamil_Nadu.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Tamil_Nadu_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Tamil_Nadu_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Tamil_Nadu 3G

df_Tamil_Nadu_3G_sp = df_Tamil_Nadu_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_Tamil_Nadu_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Tamil_Nadu_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Tamil_Nadu_3G_sp_AIRTEL
# df_Tamil_Nadu_3G_sp_CELLONE                 
# df_Tamil_Nadu_3G_sp_IDEA                     
# df_Tamil_Nadu_3G_sp_VODAFONE   

print("\n---:  Tamil_Nadu-3G operation  :-------")

df_Tamil_Nadu_3G_AIRTEL = df_Tamil_Nadu_3G[df_Tamil_Nadu_3G.Service_provider == 'AIRTEL']
df_Tamil_Nadu_3G_CELLONE = df_Tamil_Nadu_3G[df_Tamil_Nadu_3G.Service_provider == 'CELLONE']
df_Tamil_Nadu_3G_IDEA = df_Tamil_Nadu_3G[df_Tamil_Nadu_3G.Service_provider == 'IDEA']
df_Tamil_Nadu_3G_VODAFONE = df_Tamil_Nadu_3G[df_Tamil_Nadu_3G.Service_provider == 'VODAFONE']

# [1-A]  Tamil_Nadu  3G upload plotting

df_Tamil_Nadu_3G_AIRTEL_upload = df_Tamil_Nadu_3G_AIRTEL[df_Tamil_Nadu_3G_AIRTEL.Download_Upload == 'upload']
df_Tamil_Nadu_3G_CELLONE_upload = df_Tamil_Nadu_3G_CELLONE[df_Tamil_Nadu_3G_CELLONE.Download_Upload == 'upload']
df_Tamil_Nadu_3G_IDEA_upload = df_Tamil_Nadu_3G_IDEA[df_Tamil_Nadu_3G_IDEA.Download_Upload == 'upload']
df_Tamil_Nadu_3G_VODAFONE_upload = df_Tamil_Nadu_3G_VODAFONE[df_Tamil_Nadu_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Tamil_Nadu_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Tamil_Nadu_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Tamil_Nadu_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Tamil_Nadu_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  Tamil_Nadu  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Tamil_Nadu_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Tamil_Nadu_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Tamil_Nadu_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Tamil_Nadu_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  Tamil_Nadu  3G download plotting

                                                                                                                                                          
df_Tamil_Nadu_3G_AIRTEL_download = df_Tamil_Nadu_3G_AIRTEL[df_Tamil_Nadu_3G_AIRTEL.Download_Upload == 'download']
df_Tamil_Nadu_3G_CELLONE_download = df_Tamil_Nadu_3G_CELLONE[df_Tamil_Nadu_3G_CELLONE.Download_Upload == 'download']
df_Tamil_Nadu_3G_IDEA_download = df_Tamil_Nadu_3G_IDEA[df_Tamil_Nadu_3G_IDEA.Download_Upload == 'download']
df_Tamil_Nadu_3G_VODAFONE_download = df_Tamil_Nadu_3G_VODAFONE[df_Tamil_Nadu_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_Tamil_Nadu_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Tamil_Nadu_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Tamil_Nadu_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Tamil_Nadu_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  Tamil_Nadu  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Tamil_Nadu_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Tamil_Nadu_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Tamil_Nadu_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Tamil_Nadu_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  Tamil_Nadu 4G operation

print("\n---: convert to  Tamil_Nadu-4G operation :-------")
df_Tamil_Nadu_4G = df_Tamil_Nadu[df_Tamil_Nadu.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_Tamil_Nadu_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_Tamil_Nadu_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  Tamil_Nadu 4G

df_Tamil_Nadu_4G_sp = df_Tamil_Nadu_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_Tamil_Nadu_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_Tamil_Nadu_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_Tamil_Nadu_4G_sp_AIRTEL
# df_Tamil_Nadu_4G_sp_CELLONE                 
# df_Tamil_Nadu_4G_sp_IDEA                     
# df_Tamil_Nadu_4G_sp_VODAFONE 
# df_Tamil_Nadu_4G_sp_JIO  

print("\n---:  Tamil_Nadu-4G operation  :-------")

df_Tamil_Nadu_4G_AIRTEL = df_Tamil_Nadu_4G[df_Tamil_Nadu_4G.Service_provider == 'AIRTEL']
df_Tamil_Nadu_4G_CELLONE = df_Tamil_Nadu_4G[df_Tamil_Nadu_4G.Service_provider == 'CELLONE']
df_Tamil_Nadu_4G_IDEA = df_Tamil_Nadu_4G[df_Tamil_Nadu_4G.Service_provider == 'IDEA']
df_Tamil_Nadu_4G_VODAFONE = df_Tamil_Nadu_4G[df_Tamil_Nadu_4G.Service_provider == 'VODAFONE']
df_Tamil_Nadu_4G_JIO = df_Tamil_Nadu_4G[df_Tamil_Nadu_4G.Service_provider == 'JIO']

#  Tamil_Nadu  4G upload plotting

df_Tamil_Nadu_4G_AIRTEL_upload = df_Tamil_Nadu_4G_AIRTEL[df_Tamil_Nadu_4G_AIRTEL.Download_Upload == 'upload']
df_Tamil_Nadu_4G_CELLONE_upload = df_Tamil_Nadu_4G_CELLONE[df_Tamil_Nadu_4G_CELLONE.Download_Upload == 'upload']
df_Tamil_Nadu_4G_IDEA_upload = df_Tamil_Nadu_4G_IDEA[df_Tamil_Nadu_4G_IDEA.Download_Upload == 'upload']
df_Tamil_Nadu_4G_VODAFONE_upload = df_Tamil_Nadu_4G_VODAFONE[df_Tamil_Nadu_4G_VODAFONE.Download_Upload == 'upload']
df_Tamil_Nadu_4G_JIO_upload = df_Tamil_Nadu_4G_JIO[df_Tamil_Nadu_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_Tamil_Nadu_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Tamil_Nadu_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Tamil_Nadu_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Tamil_Nadu_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Tamil_Nadu_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  Tamil_Nadu  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Tamil_Nadu_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_Tamil_Nadu_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_Tamil_Nadu_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_Tamil_Nadu_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_Tamil_Nadu_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  Tamil_Nadu  4G download plotting
                                                                                                                                                          
df_Tamil_Nadu_4G_AIRTEL_download = df_Tamil_Nadu_4G_AIRTEL[df_Tamil_Nadu_4G_AIRTEL.Download_Upload == 'download']
df_Tamil_Nadu_4G_CELLONE_download = df_Tamil_Nadu_4G_CELLONE[df_Tamil_Nadu_4G_CELLONE.Download_Upload == 'download']
df_Tamil_Nadu_4G_IDEA_download = df_Tamil_Nadu_4G_IDEA[df_Tamil_Nadu_4G_IDEA.Download_Upload == 'download']
df_Tamil_Nadu_4G_VODAFONE_download = df_Tamil_Nadu_4G_VODAFONE[df_Tamil_Nadu_4G_VODAFONE.Download_Upload == 'download']
df_Tamil_Nadu_4G_JIO_download = df_Tamil_Nadu_4G_JIO[df_Tamil_Nadu_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_Tamil_Nadu_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_Tamil_Nadu_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_Tamil_Nadu_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_Tamil_Nadu_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_Tamil_Nadu_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  Tamil_Nadu  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_Tamil_Nadu_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_Tamil_Nadu_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_Tamil_Nadu_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_Tamil_Nadu_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_Tamil_Nadu_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                 
                                                
# [21] UP East 




print("\n---: [21]  UP_East operation :-------")

df_UP_East = df[df.Service_Area == 'UP East']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_East.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_East.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  UP_East 

techno_UP_East = df_UP_East.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_UP_East)
print("-------------------------------")
count = 0
for row in range(len(techno_UP_East)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  UP_East 3G operation

print("\n---: convert to  UP_East-3G operation :-------")
df_UP_East_3G = df_UP_East[df_UP_East.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_East_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_East_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  UP_East 3G

df_UP_East_3G_sp = df_UP_East_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_UP_East_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_UP_East_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_UP_East_3G_sp_AIRTEL
# df_UP_East_3G_sp_CELLONE                 
# df_UP_East_3G_sp_IDEA                     
# df_UP_East_3G_sp_VODAFONE   

print("\n---:  UP_East-3G operation  :-------")

df_UP_East_3G_AIRTEL = df_UP_East_3G[df_UP_East_3G.Service_provider == 'AIRTEL']
df_UP_East_3G_CELLONE = df_UP_East_3G[df_UP_East_3G.Service_provider == 'CELLONE']
df_UP_East_3G_IDEA = df_UP_East_3G[df_UP_East_3G.Service_provider == 'IDEA']
df_UP_East_3G_VODAFONE = df_UP_East_3G[df_UP_East_3G.Service_provider == 'VODAFONE']

# [1-A]  UP_East  3G upload plotting

df_UP_East_3G_AIRTEL_upload = df_UP_East_3G_AIRTEL[df_UP_East_3G_AIRTEL.Download_Upload == 'upload']
df_UP_East_3G_CELLONE_upload = df_UP_East_3G_CELLONE[df_UP_East_3G_CELLONE.Download_Upload == 'upload']
df_UP_East_3G_IDEA_upload = df_UP_East_3G_IDEA[df_UP_East_3G_IDEA.Download_Upload == 'upload']
df_UP_East_3G_VODAFONE_upload = df_UP_East_3G_VODAFONE[df_UP_East_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_UP_East_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_East_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_East_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_East_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  UP_East  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_East_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_UP_East_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_UP_East_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_UP_East_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  UP_East  3G download plotting

                                                                                                                                                          
df_UP_East_3G_AIRTEL_download = df_UP_East_3G_AIRTEL[df_UP_East_3G_AIRTEL.Download_Upload == 'download']
df_UP_East_3G_CELLONE_download = df_UP_East_3G_CELLONE[df_UP_East_3G_CELLONE.Download_Upload == 'download']
df_UP_East_3G_IDEA_download = df_UP_East_3G_IDEA[df_UP_East_3G_IDEA.Download_Upload == 'download']
df_UP_East_3G_VODAFONE_download = df_UP_East_3G_VODAFONE[df_UP_East_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_UP_East_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_East_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_East_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_East_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  UP_East  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_East_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_UP_East_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_UP_East_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_UP_East_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  UP_East 4G operation

print("\n---: convert to  UP_East-4G operation :-------")
df_UP_East_4G = df_UP_East[df_UP_East.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_East_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_East_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  UP_East 4G

df_UP_East_4G_sp = df_UP_East_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_UP_East_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_UP_East_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_UP_East_4G_sp_AIRTEL
# df_UP_East_4G_sp_CELLONE                 
# df_UP_East_4G_sp_IDEA                     
# df_UP_East_4G_sp_VODAFONE 
# df_UP_East_4G_sp_JIO  

print("\n---:  UP_East-4G operation  :-------")

df_UP_East_4G_AIRTEL = df_UP_East_4G[df_UP_East_4G.Service_provider == 'AIRTEL']
df_UP_East_4G_CELLONE = df_UP_East_4G[df_UP_East_4G.Service_provider == 'CELLONE']
df_UP_East_4G_IDEA = df_UP_East_4G[df_UP_East_4G.Service_provider == 'IDEA']
df_UP_East_4G_VODAFONE = df_UP_East_4G[df_UP_East_4G.Service_provider == 'VODAFONE']
df_UP_East_4G_JIO = df_UP_East_4G[df_UP_East_4G.Service_provider == 'JIO']

#  UP_East  4G upload plotting

df_UP_East_4G_AIRTEL_upload = df_UP_East_4G_AIRTEL[df_UP_East_4G_AIRTEL.Download_Upload == 'upload']
df_UP_East_4G_CELLONE_upload = df_UP_East_4G_CELLONE[df_UP_East_4G_CELLONE.Download_Upload == 'upload']
df_UP_East_4G_IDEA_upload = df_UP_East_4G_IDEA[df_UP_East_4G_IDEA.Download_Upload == 'upload']
df_UP_East_4G_VODAFONE_upload = df_UP_East_4G_VODAFONE[df_UP_East_4G_VODAFONE.Download_Upload == 'upload']
df_UP_East_4G_JIO_upload = df_UP_East_4G_JIO[df_UP_East_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_UP_East_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_East_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_East_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_East_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_UP_East_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  UP_East  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_East_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_UP_East_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_UP_East_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_UP_East_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_UP_East_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  UP_East  4G download plotting
                                                                                                                                                          
df_UP_East_4G_AIRTEL_download = df_UP_East_4G_AIRTEL[df_UP_East_4G_AIRTEL.Download_Upload == 'download']
df_UP_East_4G_CELLONE_download = df_UP_East_4G_CELLONE[df_UP_East_4G_CELLONE.Download_Upload == 'download']
df_UP_East_4G_IDEA_download = df_UP_East_4G_IDEA[df_UP_East_4G_IDEA.Download_Upload == 'download']
df_UP_East_4G_VODAFONE_download = df_UP_East_4G_VODAFONE[df_UP_East_4G_VODAFONE.Download_Upload == 'download']
df_UP_East_4G_JIO_download = df_UP_East_4G_JIO[df_UP_East_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_UP_East_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_East_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_East_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_East_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_UP_East_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  UP_East  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_East_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_UP_East_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_UP_East_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_UP_East_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_UP_East_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                     
                                                            
# [22] UP West 




print("\n---: [22]  UP_West operation :-------")

df_UP_West = df[df.Service_Area == 'UP West']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_West.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_West.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  UP_West 

techno_UP_West = df_UP_West.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_UP_West)
print("-------------------------------")
count = 0
for row in range(len(techno_UP_West)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  UP_West 3G operation

print("\n---: convert to  UP_West-3G operation :-------")
df_UP_West_3G = df_UP_West[df_UP_West.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_West_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_West_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  UP_West 3G

df_UP_West_3G_sp = df_UP_West_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_UP_West_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_UP_West_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_UP_West_3G_sp_AIRTEL
# df_UP_West_3G_sp_CELLONE                 
# df_UP_West_3G_sp_IDEA                     
# df_UP_West_3G_sp_VODAFONE   

print("\n---:  UP_West-3G operation  :-------")

df_UP_West_3G_AIRTEL = df_UP_West_3G[df_UP_West_3G.Service_provider == 'AIRTEL']
df_UP_West_3G_CELLONE = df_UP_West_3G[df_UP_West_3G.Service_provider == 'CELLONE']
df_UP_West_3G_IDEA = df_UP_West_3G[df_UP_West_3G.Service_provider == 'IDEA']
df_UP_West_3G_VODAFONE = df_UP_West_3G[df_UP_West_3G.Service_provider == 'VODAFONE']

# [1-A]  UP_West  3G upload plotting

df_UP_West_3G_AIRTEL_upload = df_UP_West_3G_AIRTEL[df_UP_West_3G_AIRTEL.Download_Upload == 'upload']
df_UP_West_3G_CELLONE_upload = df_UP_West_3G_CELLONE[df_UP_West_3G_CELLONE.Download_Upload == 'upload']
df_UP_West_3G_IDEA_upload = df_UP_West_3G_IDEA[df_UP_West_3G_IDEA.Download_Upload == 'upload']
df_UP_West_3G_VODAFONE_upload = df_UP_West_3G_VODAFONE[df_UP_West_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_UP_West_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_West_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_West_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_West_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  UP_West  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_West_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_UP_West_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_UP_West_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_UP_West_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  UP_West  3G download plotting

                                                                                                                                                          
df_UP_West_3G_AIRTEL_download = df_UP_West_3G_AIRTEL[df_UP_West_3G_AIRTEL.Download_Upload == 'download']
df_UP_West_3G_CELLONE_download = df_UP_West_3G_CELLONE[df_UP_West_3G_CELLONE.Download_Upload == 'download']
df_UP_West_3G_IDEA_download = df_UP_West_3G_IDEA[df_UP_West_3G_IDEA.Download_Upload == 'download']
df_UP_West_3G_VODAFONE_download = df_UP_West_3G_VODAFONE[df_UP_West_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_UP_West_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_West_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_West_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_West_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  UP_West  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_West_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_UP_West_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_UP_West_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_UP_West_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  UP_West 4G operation

print("\n---: convert to  UP_West-4G operation :-------")
df_UP_West_4G = df_UP_West[df_UP_West.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UP_West_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UP_West_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  UP_West 4G

df_UP_West_4G_sp = df_UP_West_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_UP_West_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_UP_West_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_UP_West_4G_sp_AIRTEL
# df_UP_West_4G_sp_CELLONE                 
# df_UP_West_4G_sp_IDEA                     
# df_UP_West_4G_sp_VODAFONE 
# df_UP_West_4G_sp_JIO  

print("\n---:  UP_West-4G operation  :-------")

df_UP_West_4G_AIRTEL = df_UP_West_4G[df_UP_West_4G.Service_provider == 'AIRTEL']
df_UP_West_4G_CELLONE = df_UP_West_4G[df_UP_West_4G.Service_provider == 'CELLONE']
df_UP_West_4G_IDEA = df_UP_West_4G[df_UP_West_4G.Service_provider == 'IDEA']
df_UP_West_4G_VODAFONE = df_UP_West_4G[df_UP_West_4G.Service_provider == 'VODAFONE']
df_UP_West_4G_JIO = df_UP_West_4G[df_UP_West_4G.Service_provider == 'JIO']

#  UP_West  4G upload plotting

df_UP_West_4G_AIRTEL_upload = df_UP_West_4G_AIRTEL[df_UP_West_4G_AIRTEL.Download_Upload == 'upload']
df_UP_West_4G_CELLONE_upload = df_UP_West_4G_CELLONE[df_UP_West_4G_CELLONE.Download_Upload == 'upload']
df_UP_West_4G_IDEA_upload = df_UP_West_4G_IDEA[df_UP_West_4G_IDEA.Download_Upload == 'upload']
df_UP_West_4G_VODAFONE_upload = df_UP_West_4G_VODAFONE[df_UP_West_4G_VODAFONE.Download_Upload == 'upload']
df_UP_West_4G_JIO_upload = df_UP_West_4G_JIO[df_UP_West_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_UP_West_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_West_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_West_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_West_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_UP_West_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  UP_West  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_West_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_UP_West_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_UP_West_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_UP_West_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_UP_West_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  UP_West  4G download plotting
                                                                                                                                                          
df_UP_West_4G_AIRTEL_download = df_UP_West_4G_AIRTEL[df_UP_West_4G_AIRTEL.Download_Upload == 'download']
df_UP_West_4G_CELLONE_download = df_UP_West_4G_CELLONE[df_UP_West_4G_CELLONE.Download_Upload == 'download']
df_UP_West_4G_IDEA_download = df_UP_West_4G_IDEA[df_UP_West_4G_IDEA.Download_Upload == 'download']
df_UP_West_4G_VODAFONE_download = df_UP_West_4G_VODAFONE[df_UP_West_4G_VODAFONE.Download_Upload == 'download']
df_UP_West_4G_JIO_download = df_UP_West_4G_JIO[df_UP_West_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_UP_West_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_UP_West_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_UP_West_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_UP_West_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_UP_West_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  UP_West  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_UP_West_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_UP_West_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_UP_West_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_UP_West_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_UP_West_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                                     
                                        
                                                                                
# [23] West Bengal  





print("\n---: [23]  West_Bengal operation :-------")

df_West_Bengal = df[df.Service_Area == 'West Bengal']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_West_Bengal.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_West_Bengal.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

# available technologies in  West_Bengal 

techno_West_Bengal = df_West_Bengal.groupby(['technology'])[['signal_strength']].count()
print("---------------------------------")
print("\t Available techonologies : ")
print("-------------------------------")
print(techno_West_Bengal)
print("-------------------------------")
count = 0
for row in range(len(techno_West_Bengal)): 
        count = count+1
print("total no. of available technologies = ",count)        
print("-----------------------------\n") 

#  West_Bengal 3G operation

print("\n---: convert to  West_Bengal-3G operation :-------")
df_West_Bengal_3G = df_West_Bengal[df_West_Bengal.technology == '3G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_West_Bengal_3G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_West_Bengal_3G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  West_Bengal 3G

df_West_Bengal_3G_sp = df_West_Bengal_3G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names  : ")
print("-------------------------------")
print(df_West_Bengal_3G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_West_Bengal_3G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_West_Bengal_3G_sp_AIRTEL
# df_West_Bengal_3G_sp_CELLONE                 
# df_West_Bengal_3G_sp_IDEA                     
# df_West_Bengal_3G_sp_VODAFONE   

print("\n---:  West_Bengal-3G operation  :-------")

df_West_Bengal_3G_AIRTEL = df_West_Bengal_3G[df_West_Bengal_3G.Service_provider == 'AIRTEL']
df_West_Bengal_3G_CELLONE = df_West_Bengal_3G[df_West_Bengal_3G.Service_provider == 'CELLONE']
df_West_Bengal_3G_IDEA = df_West_Bengal_3G[df_West_Bengal_3G.Service_provider == 'IDEA']
df_West_Bengal_3G_VODAFONE = df_West_Bengal_3G[df_West_Bengal_3G.Service_provider == 'VODAFONE']

# [1-A]  West_Bengal  3G upload plotting

df_West_Bengal_3G_AIRTEL_upload = df_West_Bengal_3G_AIRTEL[df_West_Bengal_3G_AIRTEL.Download_Upload == 'upload']
df_West_Bengal_3G_CELLONE_upload = df_West_Bengal_3G_CELLONE[df_West_Bengal_3G_CELLONE.Download_Upload == 'upload']
df_West_Bengal_3G_IDEA_upload = df_West_Bengal_3G_IDEA[df_West_Bengal_3G_IDEA.Download_Upload == 'upload']
df_West_Bengal_3G_VODAFONE_upload = df_West_Bengal_3G_VODAFONE[df_West_Bengal_3G_VODAFONE.Download_Upload == 'upload']

x1 = np.arange(0,len(df_West_Bengal_3G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_West_Bengal_3G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_West_Bengal_3G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_West_Bengal_3G_VODAFONE_upload['Data_Speed.Kbps.']))

plt.title('[1-A]  West_Bengal  3G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_West_Bengal_3G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_West_Bengal_3G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_West_Bengal_3G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_West_Bengal_3G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')

plt.legend()
plt.show()                

#[1-B]  West_Bengal  3G download plotting

                                                                                                                                                          
df_West_Bengal_3G_AIRTEL_download = df_West_Bengal_3G_AIRTEL[df_West_Bengal_3G_AIRTEL.Download_Upload == 'download']
df_West_Bengal_3G_CELLONE_download = df_West_Bengal_3G_CELLONE[df_West_Bengal_3G_CELLONE.Download_Upload == 'download']
df_West_Bengal_3G_IDEA_download = df_West_Bengal_3G_IDEA[df_West_Bengal_3G_IDEA.Download_Upload == 'download']
df_West_Bengal_3G_VODAFONE_download = df_West_Bengal_3G_VODAFONE[df_West_Bengal_3G_VODAFONE.Download_Upload == 'download']

x1 = np.arange(0,len(df_West_Bengal_3G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_West_Bengal_3G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_West_Bengal_3G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_West_Bengal_3G_VODAFONE_download['Data_Speed.Kbps.']))

plt.title('[1-B]  West_Bengal  3G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_West_Bengal_3G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_West_Bengal_3G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_West_Bengal_3G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_West_Bengal_3G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')

plt.legend()
plt.show() 

#  West_Bengal 4G operation

print("\n---: convert to  West_Bengal-4G operation :-------")
df_West_Bengal_4G = df_West_Bengal[df_West_Bengal.technology == '4G']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_West_Bengal_4G.shape)

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_West_Bengal_4G.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# print service providers in  West_Bengal 4G

df_West_Bengal_4G_sp = df_West_Bengal_4G.groupby(['Service_provider'])[['technology']].count()
print("---------------------------------")
print("\t Service provider names : ")
print("-------------------------------")
print(df_West_Bengal_4G_sp)
print("-------------------------------")
count = 0
for row in range(len(df_West_Bengal_4G_sp)): 
        count = count+1
print("total no. of service provider = ",count)        
print("-----------------------------\n")                                                                              
 
# df_West_Bengal_4G_sp_AIRTEL
# df_West_Bengal_4G_sp_CELLONE                 
# df_West_Bengal_4G_sp_IDEA                     
# df_West_Bengal_4G_sp_VODAFONE 
# df_West_Bengal_4G_sp_JIO  

print("\n---:  West_Bengal-4G operation  :-------")

df_West_Bengal_4G_AIRTEL = df_West_Bengal_4G[df_West_Bengal_4G.Service_provider == 'AIRTEL']
df_West_Bengal_4G_CELLONE = df_West_Bengal_4G[df_West_Bengal_4G.Service_provider == 'CELLONE']
df_West_Bengal_4G_IDEA = df_West_Bengal_4G[df_West_Bengal_4G.Service_provider == 'IDEA']
df_West_Bengal_4G_VODAFONE = df_West_Bengal_4G[df_West_Bengal_4G.Service_provider == 'VODAFONE']
df_West_Bengal_4G_JIO = df_West_Bengal_4G[df_West_Bengal_4G.Service_provider == 'JIO']

#  West_Bengal  4G upload plotting

df_West_Bengal_4G_AIRTEL_upload = df_West_Bengal_4G_AIRTEL[df_West_Bengal_4G_AIRTEL.Download_Upload == 'upload']
df_West_Bengal_4G_CELLONE_upload = df_West_Bengal_4G_CELLONE[df_West_Bengal_4G_CELLONE.Download_Upload == 'upload']
df_West_Bengal_4G_IDEA_upload = df_West_Bengal_4G_IDEA[df_West_Bengal_4G_IDEA.Download_Upload == 'upload']
df_West_Bengal_4G_VODAFONE_upload = df_West_Bengal_4G_VODAFONE[df_West_Bengal_4G_VODAFONE.Download_Upload == 'upload']
df_West_Bengal_4G_JIO_upload = df_West_Bengal_4G_JIO[df_West_Bengal_4G_JIO.Download_Upload == 'upload']

x1 = np.arange(0,len(df_West_Bengal_4G_AIRTEL_upload['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_West_Bengal_4G_CELLONE_upload['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_West_Bengal_4G_IDEA_upload['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_West_Bengal_4G_VODAFONE_upload['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_West_Bengal_4G_JIO_upload['Data_Speed.Kbps.']))

plt.title('[1-C]  West_Bengal  4G upload plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_West_Bengal_4G_AIRTEL_upload['Data_Speed.Kbps.'],
            label="[1] AIRTEL - upload",
            marker='*')

plt.scatter(x2,
            df_West_Bengal_4G_CELLONE_upload['Data_Speed.Kbps.'],
            label="[2] CELLONE - upload",
            marker='+')
            
plt.scatter(x3,
            df_West_Bengal_4G_IDEA_upload['Data_Speed.Kbps.'],
            label="[3] IDEA - upload",
            marker='^')

plt.scatter(x4,
            df_West_Bengal_4G_VODAFONE_upload['Data_Speed.Kbps.'],
            label="[4] VODAFONE - upload",
            marker='o')
            
plt.scatter(x5,
            df_West_Bengal_4G_JIO_upload['Data_Speed.Kbps.'],
            label="[5] JIO - upload",
            marker='1')            

plt.legend()
plt.show()                


#  West_Bengal  4G download plotting
                                                                                                                                                          
df_West_Bengal_4G_AIRTEL_download = df_West_Bengal_4G_AIRTEL[df_West_Bengal_4G_AIRTEL.Download_Upload == 'download']
df_West_Bengal_4G_CELLONE_download = df_West_Bengal_4G_CELLONE[df_West_Bengal_4G_CELLONE.Download_Upload == 'download']
df_West_Bengal_4G_IDEA_download = df_West_Bengal_4G_IDEA[df_West_Bengal_4G_IDEA.Download_Upload == 'download']
df_West_Bengal_4G_VODAFONE_download = df_West_Bengal_4G_VODAFONE[df_West_Bengal_4G_VODAFONE.Download_Upload == 'download']
df_West_Bengal_4G_JIO_download = df_West_Bengal_4G_JIO[df_West_Bengal_4G_JIO.Download_Upload == 'download']

x1 = np.arange(0,len(df_West_Bengal_4G_AIRTEL_download['Data_Speed.Kbps.']))
x2 = np.arange(0,len(df_West_Bengal_4G_CELLONE_download['Data_Speed.Kbps.']))
x3 = np.arange(0,len(df_West_Bengal_4G_IDEA_download['Data_Speed.Kbps.']))
x4 = np.arange(0,len(df_West_Bengal_4G_VODAFONE_download['Data_Speed.Kbps.']))
x5 = np.arange(0,len(df_West_Bengal_4G_JIO_download['Data_Speed.Kbps.']))

plt.title('[1-D]  West_Bengal  4G download plotting')
plt.xlabel("Number of observations ----->")
plt.ylabel("Data_Speed ( in Kbps.) ----->")

plt.scatter(x1,
            df_West_Bengal_4G_AIRTEL_download['Data_Speed.Kbps.'],
            label="[1] AIRTEL - download",
            marker='*')

plt.scatter(x2,
            df_West_Bengal_4G_CELLONE_download['Data_Speed.Kbps.'],
            label="[2] CELLONE - download",
            marker='+')
            
plt.scatter(x3,
            df_West_Bengal_4G_IDEA_download['Data_Speed.Kbps.'],
            label="[3] IDEA - download",
            marker='^')

plt.scatter(x4,
            df_West_Bengal_4G_VODAFONE_download['Data_Speed.Kbps.'],
            label="[4] VODAFONE - download",
            marker='o')
            
plt.scatter(x5,
            df_West_Bengal_4G_JIO_download['Data_Speed.Kbps.'],
            label="[5] JIO - download",
            marker='1')            

plt.legend()
plt.show()                                 