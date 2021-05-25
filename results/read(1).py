#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:41:26 2021

@author: lijingyi
"""

"""
Created on Tue Apr 13 19:00:56 2021

@author: lijingyi
"""
import os
import numpy as np
import xarray as xr
import netCDF4
from netCDF4 import Dataset
import csv
import matplotlib.pylab as plt
nc_obj=Dataset('/Users/lijingyi/Desktop/OSCAR-master/results/scen_Out_ljy.nc')
#%%

def output_csv(data,filename,filepath='./'):
    '''
    输出到csv的函数
    '''
    file = open(filepath+filename,'w',newline='')
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()
# %%
path = r'/Users/lijingyi/Desktop/OSCAR-master/results/'
D_CO2=[]
year=[]
D_Tg=[]

    #%%

for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_0.nc') as TMP:
        data = TMP.load()
for file in os.listdir(path):
    tem_D_CO2_AIM = data['D_CO2'].values
    tem_year_AIM = data['year'].values
    tem_D_Tg_AIM = data ['D_Tg'].values
    year=tem_year_AIM.tolist()
 
for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_1.nc') as TMP:
        data = TMP.load()
for file in os.listdir(path):
    tem_D_CO2_IMAGE = data['D_CO2'].values
    tem_D_Tg_IMAGE = data ['D_Tg'].values

for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_2.nc') as TMP:
        data = TMP.load()
for file in os.listdir(path):
    tem_D_CO2_MESSAGE = data['D_CO2'].values
    tem_D_Tg_MESSAGE = data ['D_Tg'].values

for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_3.nc') as TMP:
        data = TMP.load()
for file in os.listdir(path):
    tem_D_CO2_REMIND = data['D_CO2'].values
    tem_D_Tg_REMIND = data ['D_Tg'].values

for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_4.nc') as TMP:
        data = TMP.load()
for file in os.listdir(path):
    tem_D_CO2_WITCH = data['D_CO2'].values
    tem_D_Tg_WITCH = data ['D_Tg'].values
#%%
tem_D_CO2_mean_AIM = np.nanmean(tem_D_CO2_AIM, axis=1)
tem_D_CO2_std_AIM = np.nanstd(tem_D_CO2_AIM, axis=1)
tem_D_Tg_mean_AIM = np.nanmean(tem_D_Tg_AIM, axis=1)
tem_D_Tg_std_AIM = np.nanstd(tem_D_Tg_AIM, axis=1)

tem_D_CO2_mean_IMAGE = np.nanmean(tem_D_CO2_IMAGE, axis=1)
tem_D_CO2_std_IMAGE = np.nanstd(tem_D_CO2_IMAGE, axis=1)
tem_D_Tg_mean_IMAGE = np.nanmean(tem_D_Tg_IMAGE, axis=1)
tem_D_Tg_std_IMGE = np.nanstd(tem_D_Tg_IMAGE, axis=1)

tem_D_CO2_mean_MESSAGE = np.nanmean(tem_D_CO2_MESSAGE, axis=1)
tem_D_CO2_std_MESSAGE = np.nanstd(tem_D_CO2_MESSAGE, axis=1)
tem_D_Tg_mean_MESSAGE_ = np.nanmean(tem_D_Tg_MESSAGE, axis=1)
tem_D_Tg_std_MESSAGE = np.nanstd(tem_D_Tg_MESSAGE, axis=1)

tem_D_CO2_mean_REMIND = np.nanmean(tem_D_CO2_REMIND, axis=1)
tem_D_CO2_std_REMIND = np.nanstd(tem_D_CO2_REMIND, axis=1)
tem_D_Tg_mean_REMIND = np.nanmean(tem_D_Tg_REMIND, axis=1)
tem_D_Tg_std_REMIND = np.nanstd(tem_D_Tg_REMIND, axis=1)

tem_D_CO2_mean_WITCH = np.nanmean(tem_D_CO2_WITCH, axis=1)
tem_D_CO2_std_WITCH = np.nanstd(tem_D_CO2_WITCH, axis=1)
tem_D_Tg_mean_WITCH = np.nanmean(tem_D_Tg_WITCH, axis=1)
tem_D_Tg_std_WITCH = np.nanstd(tem_D_Tg_WITCH, axis=1)

#%%

tem_D_CO2_std_AIM_1 = np.nanstd(tem_D_CO2_AIM[:,1]-tem_D_CO2_AIM[:,0])
tem_D_CO2_mean_AIM_1 = tem_D_CO2_mean_AIM[:,1]-tem_D_CO2_mean_AIM[:,0]

tem_D_CO2_std_IMAGE_1 = np.nanstd(tem_D_CO2_IMAGE[:,1]-tem_D_CO2_IMAGE[:,0])
tem_D_CO2_mean_IMAGE_1 = tem_D_CO2_mean_AIM[:,1]-tem_D_CO2_mean_IMAGE[:,0]

tem_D_CO2_std_MESSAGE_1 = np.nanstd(tem_D_CO2_MESSAGE[:,1]-tem_D_CO2_MESSAGE[:,0])
tem_D_CO2_mean_MESSAGE_1 = tem_D_CO2_mean_MESSAGE[:,1]-tem_D_CO2_mean_MESSAGE[:,0]

tem_D_CO2_std_REMIND_1 = np.nanstd(tem_D_CO2_REMIND[:,1]-tem_D_CO2_REMIND[:,0])
tem_D_CO2_mean_REMIND_1 = tem_D_CO2_mean_REMIND[:,1]-tem_D_CO2_mean_REMIND[:,0]

tem_D_CO2_std_WITCH_1 = np.nanstd(tem_D_CO2_WITCH[:,1]-tem_D_CO2_WITCH[:,0])
tem_D_CO2_mean_WITCH_1 = tem_D_CO2_mean_WITCH[:,1]-tem_D_CO2_mean_WITCH[:,0]
#%%
'''scenario_line=['--','-']
for i in range(2):
    plt.plot(year,tem_D_CO2_mean_AIM[:,i],label='tem_D_CO2_mean_AIM', linestyle=scenario_line[i],color='#FF0000')
    plt.fill_between(year, tem_D_CO2_mean_AIM[:,i] - tem_D_CO2_std_AIM[:,i], tem_D_CO2_mean_AIM[:,i] + tem_D_CO2_std_AIM[:,i], color='#FF0000', alpha=0.1)
    
    plt.plot(year,tem_D_CO2_mean_IMAGE[:,i],label='tem_D_CO2_mean_IMAGE', linestyle=scenario_line[i],color='#0000FF')
    plt.fill_between(year, tem_D_CO2_mean_IMAGE[:,i] - tem_D_CO2_std_IMAGE[:,i], tem_D_CO2_mean_IMAGE[:,i] + tem_D_CO2_std_IMAGE[:,i], color='#0000FF', alpha=0.1)

    plt.plot(year,tem_D_CO2_mean_MESSAGE[:,i],label='tem_D_CO2_mean_MESSAGE', linestyle=scenario_line[i],color='#00FF00')
    plt.fill_between(year, tem_D_CO2_mean_MESSAGE[:,i] - tem_D_CO2_std_MESSAGE[:,i], tem_D_CO2_mean_MESSAGE[:,i] + tem_D_CO2_std_MESSAGE[:,i], color='#00FF00', alpha=0.1)
    
    plt.plot(year,tem_D_CO2_mean_REMIND[:,i],label='tem_D_CO2_mean_REMIND', linestyle=scenario_line[i],color='yellow')
    plt.fill_between(year, tem_D_CO2_mean_REMIND[:,i] - tem_D_CO2_std_REMIND[:,i], tem_D_CO2_mean_REMIND[:,i] + tem_D_CO2_std_REMIND[:,i], color='#00FF00', alpha=0.1)
    
    plt.plot(year,tem_D_CO2_mean_WITCH[:,i],label='tem_D_CO2_mean_WITCH', linestyle=scenario_line[i],color='orange')
    plt.fill_between(year, tem_D_CO2_mean_WITCH[:,i] - tem_D_CO2_std_WITCH[:,i], tem_D_CO2_mean_WITCH[:,i] + tem_D_CO2_std_WITCH[:,i], color='#00FF00', alpha=0.1)
    
    plt.legend(loc="upper left") 
    plt.xlabel("year")
    plt.ylabel("D_CO2")
    plt.xlim([2014,2100])
    #plt.ylim([160,200])
    #plt.savefig('./'+'test_models'+'.svg', format='svg') 
    '''
# %%

scenario_line=['--','-']

plt.plot(year,tem_D_CO2_mean_AIM[:,1]-tem_D_CO2_mean_AIM[:,0],label='tem_D_CO2_mean_AIM', linestyle='-',color='#FF0000')
plt.fill_between(year, tem_D_CO2_mean_AIM_1 - tem_D_CO2_std_AIM_1, tem_D_CO2_mean_AIM_1 + tem_D_CO2_std_AIM_1, color='#FF0000', alpha=0.1)

plt.plot(year,tem_D_CO2_mean_IMAGE[:,1]-tem_D_CO2_mean_IMAGE[:,0],label='tem_D_CO2_mean_IMAGE', linestyle='-',color='#0000FF')
plt.fill_between(year, tem_D_CO2_mean_IMAGE_1 - tem_D_CO2_std_IMAGE_1, tem_D_CO2_mean_IMAGE_1 + tem_D_CO2_std_IMAGE_1, color='#0000FF', alpha=0.1)

#plt.plot(year,tem_D_CO2_mean_MESSAGE[:,1]-tem_D_CO2_mean_MESSAGE[:,0],label='tem_D_CO2_mean_MESSAGE', linestyle='-',color='#00FF00')
#plt.fill_between(year, tem_D_CO2_mean_MESSAGE_1 - tem_D_CO2_std_MESSAGE_1, tem_D_CO2_mean_MESSAGE_1 + tem_D_CO2_std_MESSAGE_1, color='#00FF00', alpha=0.1)

plt.plot(year,tem_D_CO2_mean_REMIND[:,1]-tem_D_CO2_mean_REMIND[:,0],label='tem_D_CO2_mean_REMIND', linestyle='-',color='yellow')
plt.fill_between(year, tem_D_CO2_mean_REMIND_1 - tem_D_CO2_std_REMIND_1, tem_D_CO2_mean_REMIND_1 + tem_D_CO2_std_REMIND_1, color='yellow', alpha=0.1)

plt.plot(year,tem_D_CO2_mean_WITCH[:,1]-tem_D_CO2_mean_WITCH[:,0],label='tem_D_CO2_mean_WITCH', linestyle='-',color='orange')
plt.fill_between(year, tem_D_CO2_mean_WITCH_1 - tem_D_CO2_std_WITCH_1, tem_D_CO2_mean_WITCH_1 + tem_D_CO2_std_WITCH_1, color='orange', alpha=0.1)


plt.legend(loc="upper left") 
plt.xlabel("year")
plt.ylabel("D_CO2")
plt.xlim([2014,2100])
plt.ylim([0,120])
plt.savefig('./'+'test_models_2'+'.svg', format='svg') 

