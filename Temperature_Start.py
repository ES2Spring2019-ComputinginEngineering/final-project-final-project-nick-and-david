import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.optimize import curve_fit



fin = open('temperature_data.txt')                  #insert number of data file

time_list = []
light_list = []

for line in fin:
    a = line.strip()                                  #unpacks data from file
    c = a.split(',')
    time, light = c
    time_list.append(int(time)/1000)
    light_list.append(int(light))
Time = np.array(time_list)
light = np.array(light_list)

total_row = len(time_list)
