#!/usr/bin/env python

from netCDF4 import Dataset

#############################

def netcdf_get_var(datafile, field):
    """Read netCDF file"""
    dd = Dataset(datafile, 'r')
    var = dd.variables[field][:]
    return var


def netcdf_list_keys(datafile):
    """List fields in netCDF file"""
    dd = Dataset(datafile, 'r')
    print(dd.variables.keys())


#############################

if __name__ == "__main__":

    pass

#    datapath = '../data'
#    datafile = '%s/TS_FV2_ANN.nc'%(datapath)

#    netcdf_list_keys(datafile)

#    lat = netcdf_get_var(datafile, 'lat')
#    print(lat)

#############################
### === END OF SCRIPT === ###
#############################
