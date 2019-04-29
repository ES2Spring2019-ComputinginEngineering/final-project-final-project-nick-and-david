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

def order_input():
    order = input("Please enter the order of your function: (1) for first order, or (2) for second order: ")
    if order != '1' and order != '2':
        print('Please type either 1 or 2')
        order_input()
    return order

def readDatafiletext(filename):
    fin = open(filename)
    time_list = []
    output_list = []
    for line in fin:
        a = line.strip()
        c = a.split(',')
        time, output = c
        time_list.append(float(time))
        output_list.append(int(output))
    Time = np.array(time_list)
    Output = np.array(temp_list)
    total_row = len(time_list)
    Input = np.ones((total_row,))
    Time_axis_name = 'Time (milliseconds)'
    Out_axis_name = 'Output'
    return Time, Output, Input, Time_axis_name, Out_axis_name

def readDatafilecsv(file):
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

def graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name, popt):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    plt.plot(Time, functionGrowth(Time, *popt), 'g-',label='Step Response')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name)
    plt.legend()
    plt.ylim(0,1.3*(np.max(Output)))
    plt.xlim(0,np.max(Time))
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
    plt.ylim(0,1.3*(np.max(Output)))
    plt.xlim(0,np.max(Time))
    plt.minorticks_on()
    plt.grid()
    plt.show()

def functionGrowth(Time, K, T):
    return K-K*np.exp(-Time/T)

def functionDecay(Time, K, T):
    return K*np.exp(-Time/T)

def Filter(Output,Kernel):
    Output_filt = sig.medfilt(Output,kernel_size=Kernel)
    return Output_filt

def Print():
    print('The step response is:',round(popt[0],3),'(1-e^(-t/'+str(round(popt[1]),3)+'),3)')

#graphData(Time, Input, Output, Time_axis_name, Out_axis_name)
#graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name)

