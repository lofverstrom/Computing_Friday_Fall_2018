#!/usr/bin/env python

from numpy import ndarray
from numpy.ma.core import MaskedArray 

#############################

def F2C(tempF):
    """Convert temperature from deg Fahrenheit to deg Celcius"""

    if type(tempF) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')

    tempC = (tempF - 32.) * 5./9. 

    return tempC



def F2K(tempF):
    """Convert temperature from deg Fahrenheit to Kelvin"""

    if type(tempF) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')

    tempK = ((tempF - 32.) * 5./9.) + 273.15

    return tempK



def C2F(tempC):
    """Convert temperature from deg Celcius to deg Fahrenheit"""
    if type(tempC) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')
    
    tempF = (tempC * 9./5.) + 32.

    return tempF



def C2K(tempC):
    """Convert temperature from deg Celcius to Kelvin"""
    if type(tempC) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')
    
    tempK = tempC + 273.15

    return tempK



def K2C(tempK):
    """Convert temperature from Kelvin to deg Celcius"""
    if type(tempK) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')
    
    tempC = tempK - 273.15

    return tempC



def K2F(tempK):
    """Convert temperature from Kelvin to deg Fahrenheit"""

    if type(tempK) not in [int, float, ndarray, MaskedArray]: 
        raise TypeError('Temperature must be an int, float, or ndarray')

    tempF = ((tempK - 273.15) * 9./5.) + 32.

    return tempF



#############################

if __name__ == "__main__":
    pass

#############################
### === END OF SCRIPT === ###
#############################
