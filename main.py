import start1 as s1
import start_second1 as s2
import numpy as np
from scipy.optimize import curve_fit


file = input("Please enter your file name (without csv or txt): ")
filetype = input('Is your file a (.csv) or (.txt)?: ')
filename = file + filetype

if filetype == '.csv':
    Time, Input, Output,Time_axis_name, Out_axis_name = s1.readDatafilecsv(filename)
    if np.min(Output) < 0:
        print('Since some of the output data was negative, the data was normalized.')
        Input = Input/np.max(Output)
        Output = (Output + abs(np.min(Output)))
        Output = Output/(np.max(Output)-np.min(Output))
        
    if np.min(Time) > 0:
         print('Since some of the time data did not start at 0, the data was normalized.')
         Time = Time - np.min(Time)

elif filetype == '.txt':
    Time, Output, Input, Time_axis_name, Out_axis_name = s1.readDatafiletext(filename)
else:
    print("unsupported data type")

s1.graphData(Time, Input, Output, Time_axis_name, Out_axis_name)

filter = input('Please enter whether you would like to filter your data: 1=yes 2=no: ')
if filter == '1':
    output_filt = s2.Filter(Output, Time, Input, Time_axis_name, Out_axis_name)
elif filter == '2':
    output_filt = Output

order = s1.order_input()

if order == '1':
    datatype = input("Please enter whether this is growth or decay: (1) for growth, or (2) for decay: ")
    if datatype == '1':
        order = 1.1
    elif datatype == '2':
        order = 1.2

if order == 1.1:
    #Function = functionGrowth(Time, K, T)
    popt, pcov = curve_fit(s1.functionGrowth, Time, Output, bounds=(.1, 10000000))
    s1.graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name, popt)
    print('The step response is:',round(popt[0],2),'(1-e^(-t/'+str(round(popt[1],2))+')')
    order1 = 1.1
    
elif order == 1.2:
    #s1.functionDecay(Time, K, T)
    popt, pcov = curve_fit(s1.functionDecay, Time, Output, bounds=(.1, 10000000))
    s1.graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name, popt)
    print('The step response is:',round(popt[0],2),'(e^(-t/'+str(round(popt[1],2))+')')
    order1 = 1.2
    
elif order == '2':
    Zeta, Phi, K_dc, Period, Omega_d, Y_t, Optimize_OG, n = s2.EstimateSecondOrderCurve(Output, Input, Time)
    s2.graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name, Period, Y_t, n)
    optimize = input('Would you like to optimize this curve? 1=yes 2=no: ')
    if optimize == '1':
        Y_t, n = s2.OptimizeCurve(Output, Period, K_dc, Input, Zeta, Omega_d, Time, Phi, Optimize_OG, n)
        s2.graphDataTF(Time, Input, Output, Time_axis_name, Out_axis_name, Period, Y_t,n)

if order1 == 1.1 or 1.2:
    print('Does this curve fit the data?')
    answer = input('Yes(y) or No (n):')
    if answer.lower() == 'y':
        print('Great!')
    elif answer.lower() == 'n':
        print("Changing boundaries for the time constant and K_dc can often improve proformance.")
        n1 = input('Time constant minimum? (Change based on previous results): ')
        n2 = input('Time constant maximum?: ')
        m1 = input('Steady State value minimum?: ')
        m2 = input('Steady State value maximum?: ')
        if order == 1.1:
            popt, pcov = curve_fit(s1.functionGrowth, Time, Output,bounds=([m1,n1],[m2,n2]))
            s1.graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name, popt)
            print('The step response is:',round(popt[0],2),'(1-e^(-t/'+str(round(popt[1],2))+')')
        elif order == 1.2:
            popt, pcov = curve_fit(s1.functionDecay, Time, Output, bounds=([m1,n1],[m2,n2]))
            s1.graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name, popt)
            print('The step response is:',round(popt[0],2),'(e^(-t/'+str(round(popt[1],2))+')')
        