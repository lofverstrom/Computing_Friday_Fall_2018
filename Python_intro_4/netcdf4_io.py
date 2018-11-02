#!/usr/bin/env python

from netCDF4 import Dataset

#############################

class netcdf4_io:

    def __init__(self, inFile):
        """
        Read netCDF files
        
        Input: Path to netCDF data file
        Output: no output returned

        Example:
        data = netcdf_io(inFile)
        lat = data.lat
        """

        self.dFile = Dataset(inFile, 'r')

        ## Define useful variables 
        try: self.lat = self.dFile.variables['lat']
        except: pass

        try: self.lon = self.dFile.variables['lon']
        except: pass

        try: self.time = self.dFile.variables['time']
        except: pass


    def close(self):
        """Close data file"""
        self.dFile.close()


    def list_keys(self):
        """List fields in dataset"""
        return self.dFile.variables.keys()


    def get_field(self, Field):
        """Get field from netCDF file"""

        return self.dFile.variables[Field]

        
