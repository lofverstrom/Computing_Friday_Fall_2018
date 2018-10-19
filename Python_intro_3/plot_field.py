#!/usr/bin/env python

from sys import exit
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from read_netCDF import *
from temperature_converter import K2C

#############################

def plot_field_basic(lat, lon, var):

    ## Set map project
    m = Basemap(projection=proj,
                llcrnrlat=-90,
                urcrnrlat=90,
                llcrnrlon=0,
                urcrnrlon=360,
                resolution='l')


    ## Set no color levels
    levels = 10

    ## Make plot
    ## This is potentially dangerous; 
    ## see better practice in example 2
    lons, lats = np.meshgrid(lon, lat)
    cf = m.contourf(lons, lats, var, levels)


    ## Draw coastline
    m.drawcoastlines()

    ## Show figure
    plt.show()





def plot_field_slightly_more_advanced(lat, lon, var, proj='ortho'):

    if proj == 'ortho':
        plt.title("Full Disk Orthographic Projection")

        m = Basemap(projection=proj,
                    lon_0=-105, lat_0=40,
                    resolution='c')


    elif proj == 'cyl':
        plt.title("Cylindrical Projection")

        m = Basemap(projection=proj,
                    llcrnrlat=-90,
                    urcrnrlat=90,
                    llcrnrlon=0,
                    urcrnrlon=360,
                    resolution='c')

    else: 
        print('Projection %s is currently not supported'%proj)
        sys.exit()


    ## Convert lat/lon to map coordinates
    lons, lats = np.meshgrid(lon, lat)
    x, y = m(lons, lats)



    ## Set colormap "bwr" (blue-white-red)
    cmap = plt.cm.bwr


    ## Set no color intervals, alt define exact intervals
#    levels = 10
    levels = [-30., -25., -20., -15., -10., -5., 
               5., 10., 15., 20., 25., 30.]


    ## Create figure
    cf = m.contourf(x, y, var, levels, cmap=cmap, extend='both')


    ## Add colorbar
    try: 
        cbar = m.colorbar(cf, ticks=levels)
    except: 
        cbar = m.colorbar(cf)    
    else:
        pass
    


    ## Draw coastline
    m.drawcoastlines()


    ## Draw parallels and meridians.
    m.drawparallels(np.arange(-90.,120.,30.))
    m.drawmeridians(np.arange(0.,420.,60.))


    ## Show plot
    plt.show()



#############################

if __name__ == "__main__":

    datafile = '../data/TS_FV2_ANN.nc'

#    netcdf_list_keys(datafile)
    
    lat = netcdf_get_var(datafile, 'lat')
    lon = netcdf_get_var(datafile, 'lon')

    TS = netcdf_get_var(datafile, 'TS')

    print(type(TS))

#    TS = K2C(TS)

#    print(np.shape(TS))

    ###

    ## Exempel 1
#    plot_field_basic(lat, lon, TS[0,:,:])


    ## Exempel 2
#    proj = 'cyl'
#    proj = 'ortho'
#    plot_field_slightly_more_advance(lat, lon, TS[0,:,:], proj=proj)

#############################
### === END OF SCRIPT === ###
#############################
