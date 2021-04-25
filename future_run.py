#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:30:56 2021

@author: lijingyi
"""


import xarray as xr
from time import perf_counter
import numpy as np
import matplotlib.pylab as plt
import pandas as pd

from core_fct.fct_loadP import load_all_param
from core_fct.fct_loadD import load_all_hist,load_all_scen
from core_fct.fct_genMC import generate_config, generate_drivers
from core_fct.fct_genD import create_hist_drivers, create_scen_drivers
from core_fct.fct_process import OSCAR


nMC = nMC_hist = nMC_scen = 30#20  ##模特卡罗模拟次数
model = OSCAR
LCC = 'gross'
inds = (1750, 1750, 2014, 2100)
mod_region = 'RCP_5reg'
var_keep = ['D_Tg','RF_CO2']
alpha = 0.01#0.001

with xr.open_dataset('parameters/Par.nc') as TMP: Par = TMP.load()
with xr.open_dataset('parameters/hist_Ini.nc') as TMP: Ini_hist = TMP.load()
with xr.open_dataset('parameters/hist_For.nc') as TMP: For_hist = TMP.load()
with xr.open_dataset('parameters/scen_Ini.nc') as TMP: Ini_scen = TMP.load()
with xr.open_dataset('parameters/scen_For.nc') as TMP: For_scen = TMP.load()


# %%
'''
将排放数据替换成自己的
RCP2.6----???NP
'''
For_scen_ljy = For_scen.copy(deep=True)

temp = For_scen.Eff.sel(config=0).sel(scen='RCP2.6').values
print(temp.shape)
temp *= 0
temp[-1]=np.array([1,2,3,3,2,1])
## temp为(87,6)的数组形式

for i in range(nMC):
    # print(i)
    For_scen_ljy.sel(scen='RCP2.6').sel(config=i)['Eff'].values[:] = temp

# %%
Out_scen = model(Ini_scen, Par, For_scen_ljy,var_keep=var_keep)  
filename = 'base'
Out_scen.to_netcdf('results/' + 'scen_Out_ljy.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_scen})

