#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:34:52 2019

@author: DRFricke
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.optimize import curve_fit

def readDatafile(file):
    csv_file = open(file)
    total_row = sum(1 for row in csv_file) -1
    csv_file.seek(0)
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0
    
    Time = np.zeros((total_row,))
    Input = np.zeros((total_row,))
    Output = np.zeros((total_row,))
    
    
    index = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            Time[index] = float(row[0])
            Input[index] = float(row[1])
            Output[index] = float(row[2])
            index += 1
            line_count += 1
            
    return Time, Input, Output

def graphDataTF(Time, Input, Output):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    plt.plot(Time, function(Time, 20), 'g-',label='Transfer Function')
    plt.ylabel("Motor Speed")
    plt.xlabel("Time (Milliseconds)")
    plt.legend()
    plt.ylim(0,900)
    plt.xlim(0,1000)
    plt.minorticks_on()
    plt.grid()
    plt.show()
    
def graphDatalog(Time, Input, Output):
    plt.figure()
    plt.semilogy(Time, Output, 'r.', label='Output')
    #plt.loglog(Time, function(Time, *popt), 'g-',label='Transfer Function')
    plt.ylabel("Motor Speed")
    plt.xlabel("Time (Milliseconds)")
    plt.legend()
    plt.minorticks_on()
    plt.grid()
    plt.show()
    
def graphData(Time, Input, Output):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    plt.ylabel("Motor Speed")
    plt.xlabel("Time (Milliseconds)")
    plt.legend()
    plt.ylim(0,900)
    plt.xlim(0,1000)
    plt.minorticks_on()
    plt.grid()
    plt.show()

file = 'NewMotorData.csv'
Time, Input, Output =  readDatafile(file)
RPM_filt = sig.medfilt(Output,kernel_size=5)

#def Filter(Output)

def function(Time, T):
    return 660-660*np.exp(-Time/T)


popt, pcov = curve_fit(function, Time[1:15], Output[1:15])

graphData(Time, Input, Output)
graphDataTF(Time, Input, RPM_filt)
graphDatalog(Time, Input, RPM_filt)
print('Transfer Function is:',660,'(1-e^(-t/'+str(popt[0])+')')
