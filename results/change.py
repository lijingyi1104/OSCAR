#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:45:59 2021

@author: lijingyi
"""
import os
import xarray as xr
from time import perf_counter
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import netCDF4
from netCDF4 import Dataset
import csv




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


tem_D_CO2_list = []
tem_D_Tg_list = []
filename_list = ['scen_Out_ljy_0.nc','ASIAscen_Out_tmp_0_Eff.nc','LAMscen_Out_tmp_0_Eff.nc','REFscen_Out_tmp_0_Eff.nc','OECDscen_Out_tmp_0_Eff.nc','MEAscen_Out_tmp_0_Eff.nc']


for filename in filename_list:
    with xr.open_dataset(path+filename) as TMP:
        data = TMP.load()
    tem_D_CO2_list.append(data['D_CO2'].values[...,1]-data['D_CO2'].values[...,0])
    tem_D_Tg_list.append(data['D_Tg'].values[...,1]-data['D_Tg'].values[...,0])
# %%

scen_Out_ljy = tem_D_Tg_list[0]
region_data = np.array(tem_D_Tg_list[1:])

D_region_data = scen_Out_ljy-region_data

alpha_region_data = D_region_data/D_region_data.sum(0)
alpha_region_data = alpha_region_data[:,-1,:]

tem_alpha_region_data = np.nanmean(alpha_region_data, axis=1)
#%%
plt.hist(alpha_region_data[0])










    
    