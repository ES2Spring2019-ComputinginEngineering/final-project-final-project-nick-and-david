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
            Time_axis_name = row[0]
            Out_axis_name = row[2]
            line_count += 1
        else:
            Time[index] = float(row[0])
            Input[index] = float(row[1])
            Output[index] = float(row[2])
            index += 1
            line_count += 1
            
    return Time, Input, Output,Time_axis_name, Out_axis_name

def graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    #plt.plot(Time, Input, 'b.', label='Input')
    plt.plot(Time, function(Time, *popt), 'g-',label='Transfer Function')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name)
    plt.legend()
    plt.ylim(0,900)
    plt.xlim(0,1000)
    plt.minorticks_on()
    plt.grid()
    plt.show()
    
    
def graphData(Time, Input, Output, Time_axis_name, Out_axis_name):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name)
    plt.legend()
    plt.ylim(0,900)
    plt.xlim(0,1000)
    plt.minorticks_on()
    plt.grid()
    plt.show()

file = 'NewMotorData.csv'
Time, Input, Output,Time_axis_name, Out_axis_name =  readDatafile(file)
RPM_filt = sig.medfilt(Output,kernel_size=5)

#def Filter(Output)

def function(Time, K, T):
    return K-K*np.exp(-Time/T)

n = 24
popt, pcov = curve_fit(function, Time, Output,bounds=(n,1000))

graphData(Time, Input, Output, Time_axis_name, Out_axis_name)
graphDataTF(Time, Input, RPM_filt, Time_axis_name, Out_axis_name)
print('The step response is:',popt[0],'(1-e^(-t/'+str(popt[1])+')')
