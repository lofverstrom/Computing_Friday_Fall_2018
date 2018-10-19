#!/usr/bin/env python

from netCDF4 import Dataset

def netcdf_list_keys(datafile):
    """List fields in netCDF file"""
    dd = Dataset(datafile, 'r')
    print(dd.variables.keys())


def netcdf_get_var(datafile, field):
    """Read netCDF file"""
    dd = Dataset(datafile, 'r')
    var = dd.variables[field]
    return var



if __name__ == "__main__":

    datafile = '../data/TS_FV2_ANN.nc'

    netcdf_list_keys(datafile)

    lat = netcdf_get_var(datafile, 'lat')
    lon = netcdf_get_var(datafile, 'lon')

    print(lon.units)

