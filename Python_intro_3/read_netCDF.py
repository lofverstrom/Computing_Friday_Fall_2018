#!/usr/bin/env python

from netCDF4 import Dataset

#############################

def netcdf_get_var(datafile, field):
    """Read variable from netCDF file"""
    dd = Dataset(datafile, 'r')
    var = dd.variables[field]
    return var


def netcdf_list_keys(datafile):
    """List fields in netCDF file"""
    dd = Dataset(datafile, 'r')
    print(dd.variables.keys())


#############################

if __name__ == "__main__":

    datapath = '../data'
    datafile = '%s/TS_FV2_ANN.nc'%(datapath)

    netcdf_list_keys(datafile)

    field = 'lat'
    lat = netcdf_get_var(datafile, field)

    ## Print metadata
    print(lat)

    ## Print field
    print(lat[:])

#############################
### === END OF SCRIPT === ###
#############################
