#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:58:34 2019

@author: DRFricke
"""

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
from scipy import stats

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

def graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name, Period):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.', label='Input')
    plt.plot(Time[1:], Y_t, 'k', label='Step Response')
    plt.plot(Time[Period[:3]], Output[Period[:3]], 'b.', label='Period')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name)
    plt.legend()
    plt.ylim(0,1.3*(np.max(Output)))
    plt.xlim(0,np.max(Time))
    plt.minorticks_on()
    plt.grid()
    plt.show()
    
    
def graphData(Time, Input, Output, Time_axis_name, Out_axis_name,Period):
    plt.figure()
    plt.plot(Time, Output, 'r.', label='Output')
    plt.plot(Time, Input, 'b.',Time[Period[:3]], Output[Period[:3]], 'b.', label='Period')
    plt.ylabel(Out_axis_name)
    plt.xlabel(Time_axis_name+', Milliseconds')
    plt.legend()
    plt.ylim(0,1.3*(np.max(Output)))
    plt.xlim(0,np.max(Time))
    plt.minorticks_on()
    plt.grid()
    plt.show()

file = 'SecordMotorData.csv'
Time, Input, Output,Time_axis_name, Out_axis_name =  readDatafile(file)
RPM_filt = sig.medfilt(Output,kernel_size=5)


SteadyState, _ = stats.mode(Output)
OSR = (np.max(Output)-SteadyState)/SteadyState
Zeta = -float(np.log(OSR)/np.sqrt(np.pi**2 + np.log(OSR)**2))
Phi = float(np.arccos(np.sqrt(1-Zeta**2)))
K_dc = SteadyState/Input[1:]
Period, _ = sig.find_peaks(Output)

Delta_Period = Time[Period[1]]-Time[Period[0]]
Omega_d = (2*np.pi)/Delta_Period
Y_t = K_dc*Input[1:]*(1-(1/(np.sqrt(1-Zeta**2)))*np.exp(-Zeta*Omega_d*Time[1:])*np.cos(Omega_d*Time[1:]-Phi))
Optimize_OG = np.sum(np.sqrt((Y_t - Output[1:])**2))

#Check this out!

count = 0

for i in range(50):
    Delta_Period_Opt = Time[Period[1]+i]-Time[Period[0]]
    Omega_d_Opt = (2*np.pi)/Delta_Period_Opt
    Y_t_Opt = K_dc*Input[1:]*(1-(1/(np.sqrt(1-Zeta**2)))*np.exp(-Zeta*Omega_d_Opt*Time[1:])*np.cos(Omega_d_Opt*Time[1:]-Phi))
    Optimize = np.sum(np.sqrt((Y_t_Opt - Output[1:])**2))
    if Optimize < Optimize_OG:
        Y_t = Y_t_Opt
        Optimize_OG = Optimize
        count = count + 1
        
print(count)

#Find best point!

graphData(Time, Input, Output, Time_axis_name, Out_axis_name, Period)
graphDataTF(Time, Input, RPM_filt, Time_axis_name, Out_axis_name, Period)
#print('The step response is:',popt[0],'(1-e^(-t/'+str(popt[1])+')')
