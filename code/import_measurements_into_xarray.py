import xarray as xr
import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt



# Read the sensor mapping from the CSV file
sensor_mapping_df = pd.read_csv('../data/table_Sensors.csv')
metgeo = pd.read_csv('../data/Location_File.csv')
meas = pd.read_csv('../data/my_measurements.csv')

meas['time'] = pd.to_datetime(meas['dt'])


# Create a dictionary mapping sensorID to sensor names
names = dict(zip(sensor_mapping_df['SensorID'], sensor_mapping_df['symbol']))

# Replace the sensorID integers with their corresponding names
meas['name'] = meas['sensorid'].replace(names)




#meas_pivoted = meas.pivot(index='time', columns='sensorid', values='value')
meas_pivoted = meas.pivot(index='time', columns='name', values='value')


ds = meas_pivoted.to_xarray()


mapUnits = dict(zip(sensor_mapping_df['symbol'], sensor_mapping_df['unit']))
mapLongName = dict(zip(sensor_mapping_df['symbol'], sensor_mapping_df['en_name']))
mapDecimals = dict(zip(sensor_mapping_df['symbol'], sensor_mapping_df['decimal_num']))
loc = dict(zip(metgeo['stNo'], metgeo['station_nm']))
_lat = dict(zip(metgeo['stNo'], metgeo['latt']))
_lon = dict(zip(metgeo['stNo'], metgeo['long']))




for varname in ds: 
    #print(varname, mapUnits[varname], mapLongName[varname])
    ds[varname].attrs['units'] = mapUnits[varname]
    ds[varname].attrs['long_name'] = mapLongName[varname]
    ds[varname].attrs['decimals'] = mapDecimals[varname]


   
ds.attrs['station_name'] = loc[meas['stno'].unique()[0]]
ds.attrs['lat'] = _lat[meas['stno'].unique()[0]]
ds.attrs['lon'] = _lon[meas['stno'].unique()[0]]
ds.attrs['date_created'] = str(dt.datetime.now())
try: 
    ds.attrs['created by'] =  "{}, on {}".format(os.getlogin(), os.name) # POSIX stands for "Portable Operating System Interface for Unix."
except:
    pass
ds.attrs['xarray version'] = xr.__version__


print(ds)

ds.to_netcdf('../output/my_measurements.nc', unlimited_dims='time')