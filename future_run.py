#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:30:56 2021

@author: lijingyi
"""


import xarray as xr
from time import perf_counter
import numpy as np


from core_fct.fct_loadP import load_all_param
from core_fct.fct_loadD import load_all_hist,load_all_scen
from core_fct.fct_genMC import generate_config, generate_drivers
from core_fct.fct_genD import create_hist_drivers, create_scen_drivers
from core_fct.fct_process import OSCAR


nMC = nMC_hist = nMC_scen = 3#20  ##模特卡罗模拟次数
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

Out_scen = model(Ini_scen, Par, For_scen,var_keep=var_keep)  
filename = 'base'
Out_scen.to_netcdf('results/' + 'scen_' + '_Out_scen.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_scen})


#%%
For_scen
For_scen.Eff
For_scen.Eff.sel(config=0)
For_scen.Eff.sel(config=0).sel(scen='RCP2.6')

import matplotlib.pylab as plt
plt.plot(Out_scen.D_Tg.mean('config'))

