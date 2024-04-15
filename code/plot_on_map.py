import xarray as xr
import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np




ds = xr.open_dataset('../output/my_measurements.nc') # ../output/my_measurements.nc


plt.close('all')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8))


quantities = ['TAir (max)', 'TAir (min)' ,'TAir (av)' ]
# Create a figure and two subplots


#UPPER PANEL
for q in quantities:
    ds[q].plot(label=q, alpha =.35, ax=ax1)
    if q=='TAir (av)':
        ds[q].rolling(time=15, center=True).mean().plot(label='rolling mean', ax=ax1)
 
#LOWER PANEL
clim = ds['TAir (av)'].groupby('time.month')    
anomaly = clim - clim.mean('time')
anomaly.plot( alpha=0.15, ax=ax2)
anomaly.where(anomaly>10).plot(label='monthly anomaly', alpha=0.9, color='red', ax=ax2)    
ax2.set_ylim(-15, 15)


# Function to update ax2 when ax1 x-axis limits change
def update_ax2(*args):
    ax2.set_xlim(ax1.get_xlim())

def update_ax1(*args):
    ax1.set_xlim(ax2.get_xlim())    

# Connect the xlim_changed event of ax1 to the update function for ax2
ax1.callbacks.connect('xlim_changed', update_ax2)
ax2.callbacks.connect('xlim_changed', update_ax1)

ax1.grid()
ax2.grid()
ax1.legend()
plt.show()
