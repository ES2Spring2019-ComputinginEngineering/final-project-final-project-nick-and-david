import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.optimize import curve_fit

fin = open('newtemperature_data19.txt')                  #insert number of data file

time_list = []
temp_list = []

for line in fin:
    a = line.strip()
    c = a.split(',')
    time, temp = c
    time_list.append(float(time))
    temp_list.append(int(temp))


Time = np.array(time_list)
Output = np.array(temp_list)
total_row = len(time_list)
Input = np.zeros((total_row,))
Time_axis_name = 'Time (milliseconds)'
Out_axis_name = 'Degrees (celsius)'


def graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    #plt.plot(Time, function(Time, *popt), 'g-',label='Transfer Function')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name)
    plt.legend()
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
    plt.minorticks_on()
    plt.grid()
    plt.show()


def function(Time, K, T):
    return K-K*np.exp(-Time/T)

#n = 24
popt, pcov = curve_fit(function, Time, Output) #bounds=(n,1000)         insert bounds if needed

graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name)
#graphDataTF(Time, Input, Outputfilt, Time_axis_name, Out_axis_name)        #if filtering is needed
print('The step response is:',popt[0],'(1-e^(-t/'+str(popt[1])+')')
