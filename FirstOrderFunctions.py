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

def yesOrNo(message):                           #requires the user to input 1 or 2 as fits from the question
    while True:
        answer = input(message)
        if answer != '1' and answer != '2':
            print('Please type either 1 or 2')
        elif answer == '1' or answer == '2':
            break
    return answer


def readDatafiletext(filename):                 #parses data for use later from a text file
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
    Output = np.array(output_list)
    total_row = len(time_list)
    Input = np.ones((total_row,))
    Time_axis_name = 'Time (milliseconds)'
    Out_axis_name = 'Output'
    return Time, Output, Input, Time_axis_name, Out_axis_name


def readDatafilecsv(file):                          #parses data for use later from a csv file
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


def graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name, popt):      #graphs the data with the curve printed on the graph
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
    
    
def graphData(Time, Input, Output, Time_axis_name, Out_axis_name):               #graphs the data without the curve
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


def functionGrowth(Time, K, T):                                                    #function for first order growth for use in the curvefit function
    return K-K*np.exp(-Time/T)
