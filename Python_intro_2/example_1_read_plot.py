#!/usr/bin/env python

from numpy import *
import matplotlib.pyplot as plt
import csv

###########################

def read_data(datafile):
    """
    Read year and temperature data from CSV file.
    Data is returned in two separate lists.
    """
    
    year = []
    temp = []

    with open(datafile) as inf:

        for line in inf:

            parts = line.split(',')

            year.append(int(parts[0]))

            try:
                temp.append(float(parts[1]))
            except: 
                temp.append(None)

    return year, temp


#############################

def lineplot(year, temp, unit='degC'):
    """Plot temperature as function of time"""

    
    plt.plot(year, temp, '-k')

    ## Ticks on x-axis
    ticks = linspace(1880,2020,8)
    plt.xticks(ticks)

    ## Range of x-axis 
    plt.xlim(1880,2020)

    ## Title and labels
    plt.title('Global annual mean temperature')

    plt.xlabel('Year')

    if unit == 'degC':
        plt.ylabel('Temperature [$^\circ$C]')
    elif unit == 'degF':
        plt.ylabel('Temperature [$^\circ$F]')
    elif unit == 'K':
        plt.ylabel('Temperature [K]')
    else: 
        plt.ylabel('Temperature')

    ## Show grid 
    plt.grid(True)

    ## Show figure
    plt.show()


#############################


if __name__ == "__main__":

    unit = 'degF'

    dataPath = '../data'

    dataFile = '%s/fake_timeseries_temp_%s.csv'%(dataPath, unit)


    year, temp = read_data(dataFile)



    lineplot(year, temp, unit=unit)
    

#############################
### === END OF SCRIPT === ###
#############################
