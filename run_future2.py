#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:09:10 2021

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


# %%替换function
def replace(number,filekey, Scen, nMC, driver):
    for i in range(nMC):
        ran = np.random.randint(0,number)
        filename = 'scen_data/' + filekey + str(ran) + '.csv'
        data = pd.read_csv(filename)
        temp = data.values.T
        For_scen_ljy.sel(scen = Scen).sel(config = i)[driver].values[:] = temp
    return For_scen_ljy
#CO2
For_scen_ljy = replace(5,'CD_NDC', 'RCP2.6', nMC, 'Eff')
For_scen_ljy = replace(5,'CD_NP', 'RCP4.5', nMC, 'Eff')
For_scen_ljy = replace(6,'AD_NDC', 'RCP6.0', nMC, 'Eff')
For_scen_ljy = replace(6,'AD_NP', 'RCP8.5', nMC, 'Eff')
#BC
For_scen_ljy = replace(5,'CD_BC_NDC', 'RCP2.6', nMC, 'E_BC')
For_scen_ljy = replace(5,'CD_BC_NP', 'RCP4.5', nMC, 'E_BC')
For_scen_ljy = replace(4,'AD_BC_NDC', 'RCP6.0', nMC, 'E_BC')
For_scen_ljy = replace(4,'AD_BC_NP', 'RCP8.5', nMC, 'E_BC')
#CH4
For_scen_ljy = replace(5,'CD_CH4_NDC', 'RCP2.6', nMC, 'E_CH4')
For_scen_ljy = replace(5,'CD_CH4_NP', 'RCP4.5', nMC, 'E_CH4')
For_scen_ljy = replace(6,'AD_CH4_NDC', 'RCP6.0', nMC, 'E_CH4')
For_scen_ljy = replace(6,'AD_CH4_NP', 'RCP8.5', nMC, 'E_CH4')
#N2O
For_scen_ljy = replace(5,'CD_N2O_NDC', 'RCP2.6', nMC, 'E_N2O')
For_scen_ljy = replace(5,'CD_N2O_NP', 'RCP4.5', nMC, 'E_N2O')
For_scen_ljy = replace(6,'AD_N2O_NDC', 'RCP6.0', nMC, 'E_N2O')
For_scen_ljy = replace(6,'AD_N2O_NP', 'RCP8.5', nMC, 'E_N2O')
#SO2
For_scen_ljy = replace(5,'CD_SO2_NDC', 'RCP2.6', nMC, 'E_SO2')
For_scen_ljy = replace(5,'CD_SO2_NP', 'RCP4.5', nMC, 'E_SO2')
For_scen_ljy = replace(5,'AD_SO2_NDC', 'RCP6.0', nMC, 'E_SO2')
For_scen_ljy = replace(5,'AD_SO2_NP', 'RCP8.5', nMC, 'E_SO2')


# %%
Out_scen = model(Ini_scen, Par, For_scen_ljy,var_keep=var_keep)  
filename = 'base'
Out_scen.to_netcdf('results/' + 'scen_Out_ljy.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_scen})

#%%
plt.plot(Out_scen.D_Tg.mean('config'))






