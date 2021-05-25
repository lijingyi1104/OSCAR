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

for file in os.listdir(path):
    with xr.open_dataset(path+'scen_Out_ljy_3.nc') as TMP:
        data = TMP.load()


for file in os.listdir(path):
    tem_D_CO2 = data['D_CO2'].values
    tem_year = data['year'].values
    tem_D_Tg = data ['D_Tg'].values
           
    D_CO2=tem_D_CO2.tolist()
    year=tem_year.tolist() 
    D_Tg = tem_D_Tg.tolist()

#%%
def draw_scenario(tem_mean, tem_std, ylabel, file_name):
    scenario_name=['CD-LINKS NDC', 'CD-LINKS_NP','AD_NDC','AD_NP']
    scenario_color=['#FF0000', '#0000FF', '#4682B4', '#87CEFA']
    scenario_linestyle=['--','-',':','-']
    for i in range(len(scenario_name)):
        if i in [2,3,4]:
            continue
        plt.plot(year,tem_mean[:,i],label=scenario_name[i], linestyle=scenario_linestyle[i], color=scenario_color[i])
        plt.fill_between(year, tem_mean[:,i] - tem_std[:,i], tem_mean[:,i] + tem_std[:,i], color=scenario_color[i], alpha=0.1)
    plt.legend(loc="upper left") 
    plt.xlabel("year")
    plt.ylabel(ylabel)
    plt.xlim([2014,2100])
    #plt.ylim([160,200])
    #plt.savefig('./'+file_name+'.svg', format='svg') 
    plt.show()
#%%
#print(tem_D_CO2)
tem_D_CO2_mean = np.nanmean(tem_D_CO2, axis=1)
tem_D_CO2_std = np.nanstd(tem_D_CO2, axis=1)
tem_D_Tg_mean = np.nanmean(tem_D_Tg, axis=1)
tem_D_Tg_std = np.nanstd(tem_D_Tg, axis=1)
#print(tem_D_CO2_mean)

draw_scenario(tem_D_CO2_mean, tem_D_CO2_std, "D_CO2/ppm","D_CO2_AIM")

draw_scenario(tem_D_Tg_mean, tem_D_Tg_std, "D_Tg/K","D_Tg_AIM")




