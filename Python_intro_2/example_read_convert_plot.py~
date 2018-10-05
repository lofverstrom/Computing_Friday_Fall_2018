#!/usr/bin/env python

from numpy import *
import matplotlib.pyplot as plt
import csv

from temperature_converter import * 

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




def read_data_convert(datafile, convert=False, 
                      unit_in='degF', unit_out='degC'):

    """
    Example of reading from CSV file and converting 
    temperature data to different unit on the fly
    """

    year = []
    temp = []

    with open(datafile) as inf:
        for line in inf:

            parts = line.split(',')

            year.append(int(parts[0]))

            try: 
                if convert is True:
                    if unit_in == 'degF' and unit_out == 'degC':
                        try: 
                            temp.append(F2C(float(parts[1])))
                        except: 
                            temp.append(None)

                    elif unit_in == 'degF' and unit_out == 'K':
                        try: 
                            temp.append(F2K(float(parts[1])))
                        except: 
                            temp.append(None)

                    elif unit_in == 'degC' and unit_out == 'degF':
                        try: 
                            temp.append(C2F(float(parts[1])))
                        except: 
                            temp.append(None)

                    elif unit_in == 'degC' and unit_out == 'K':
                        try: 
                            temp.append(C2K(float(parts[1])))
                        except: 
                            temp.append(None)

                    elif unit_in == 'K' and unit_out == 'degC':
                        try: 
                            temp.append(K2C(float(parts[1])))
                        except: 
                            temp.append(None)

                    elif unit_in == 'K' and unit_out == 'degF':
                        try: 
                            temp.append(K2F(float(parts[1])))
                        except: 
                            temp.append(None)

                    else:
                        print('Unsupported unit combination (%s and %s)'%(unit_in, unit_out))
                        print('Will not convert to different unit!')
                        temp.append(float(parts[1]))

                else:
                    temp.append(float(parts[1]))

            except: 
                temp.append(None)


    return year, temp, unit_out




def write_data(time, temperature, unit='degC', outfile=None):
    """
    Write data to CSV file 
    """

    if outfile is not None:
        outfile = outfile
    else:
        outfile = 'data/mock_timeseries_temp_%s.csv'%unit


    ndec = 3 ## Number of decimals to write

    write_to_file = True ## Set automatically in script

    with open(outfile, mode='w') as ofile:
        write_2_file = csv.writer(ofile, 
                                  delimiter=',', 
                                  quotechar='"', 
                                  quoting=csv.QUOTE_MINIMAL)
    

        for ii in range(len(time)):
            if unit == 'degC':
                try: 
                    temp = float(temperature[ii])
                    write_to_file = True
                except: pass


            elif unit == 'K':
                try: 
                    temp = C2K(float(temperature[ii]))
                    write = True                    
                except: write_to_file = False


            elif unit == 'degF':
                try:
                    temp = C2F(float(temperature[ii]))
                    write_to_file = True
                except: write_to_file = False

            else: 
                print('\nOBS!! unit "%s" is not supported!'%unit)
                print('Will not change unit\n')


            if write_to_file: 
                write_2_file.writerow([time[ii], round(temp,ndec)])



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
#    unit = 'degC'

    dataPath = '../data'

    dataFile = '%s/fake_timeseries_temp_%s.csv'%(dataPath, unit)


    year, temp = read_data(dataFile)

#    year, temp, unit = read_data_convert(dataFile, convert=True,
#                                         unit_in=unit, unit_out='K')



    lineplot(year, temp, unit=unit)
    

#############################
### === END OF SCRIPT === ###
#############################
