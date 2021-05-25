
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
For_scen_ljy = For_scen.copy(deep=True)

#%%
def replace_basic(nMC, driver_bas):
    for i in range(nMC):
        For_scen_ljy.sel(scen = 'RCP2.6').sel(config = i)[driver_bas].values[:] = For_scen_ljy.sel(scen = 'RCP4.5').sel(config = i)[driver_bas].values[:]
        For_scen_ljy.sel(scen = 'RCP6.0').sel(config = i)[driver_bas].values[:] = For_scen_ljy.sel(scen = 'RCP4.5').sel(config = i)[driver_bas].values[:]
        For_scen_ljy.sel(scen = 'RCP8.5').sel(config = i)[driver_bas].values[:] = For_scen_ljy.sel(scen = 'RCP4.5').sel(config = i)[driver_bas].values[:]
    return For_scen_ljy

For_scen_ljy=replace_basic(nMC, 'E_Xhalo')
For_scen_ljy=replace_basic(nMC, 'E_NOX')
For_scen_ljy=replace_basic(nMC, 'E_CO')
For_scen_ljy=replace_basic(nMC, 'E_VOC')
For_scen_ljy=replace_basic(nMC, 'E_NH3')
For_scen_ljy=replace_basic(nMC, 'E_OC')

        
        
# %%替换function
def replace(number,filekey, Scen, nMC, driver):
    for i in range(nMC):
        ran = np.random.randint(0,number)
        ran = 0
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
plt.plot(For_scen_ljy.mean('config').Eff.sel(scen='RCP2.6').sum('reg_land'))
# plt.plot(For_scen_ljy.mean('config').Eff.sel(scen='RCP4.5').sum('reg_land'))
plt.plot(For_scen_ljy.mean('config').Eff.sel(scen='RCP6.0').sum('reg_land'))
# plt.plot(For_scen_ljy.mean('config').Eff.sel(scen='RCP8.5').sum('reg_land'))


# %%
Out_scen = model(Ini_scen, Par, For_scen_ljy,var_keep=var_keep)  
filename = 'base'
Out_scen.to_netcdf('results/' + 'scen_Out_ljy_0.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_scen})

'''
#%%
plt.plot(Out_scen.D_Tg.mean('config'))
plt.plot(Out_scen.D_CO2.mean('config'))
#%%
plt.plot(Out_scen.D_Tg.mean('config').sel(scen='RCP2.6'))
plt.plot(Out_scen.D_Tg.mean('config').sel(scen='RCP4.5'))
plt.plot(Out_scen.D_Tg.mean('config').sel(scen='RCP6.0'))
plt.plot(Out_scen.D_Tg.mean('config').sel(scen='RCP8.5'))
'''
# %%

# 区域1减排量增加0.001

filename_list = ['','ASIA','LAM','MEA','OECD','REF']
#reg_land = 1
for reg_land in [1,2,3,4,5]:
    #for emi in ['Eff','E_CH4','E_N2O','E_BC','E_SO2']:
    for emi in ['Eff']:
        For_scen_tmp =  For_scen_ljy.copy(deep=True)
        temp_0=For_scen_tmp[emi].sel(reg_land=reg_land).sel(scen='RCP4.5').values-For_scen_tmp[emi].sel(reg_land=reg_land).sel(scen='RCP2.6').values
        temp_1=For_scen_tmp[emi].sel(reg_land=reg_land).sel(scen='RCP2.6')+temp_0/1000
        For_scen_tmp[emi].sel(scen = 'RCP2.6').sel(reg_land=reg_land).values[:] = temp_1.values
   
    Out_scen = model(Ini_scen, Par, For_scen_tmp,var_keep=var_keep)  
    filename =filename_list[reg_land]
    Out_scen.to_netcdf('results/' + filename + 'scen_Out_tmp_0_Eff.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_scen})
    



