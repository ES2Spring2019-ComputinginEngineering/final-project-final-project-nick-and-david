import start as s1
import start_second as s2
from scipy.optimize import curve_fit


file = input("Please enter your file name (without csv or txt): ")
filetype = input('Is your file a (.csv) or (.txt)?: ')
filename = file + filetype

if filetype == '.csv':
    Time, Input, Output,Time_axis_name, Out_axis_name = s1.readDatafilecsv(filename)
elif filetype == '.txt':
    Time, Output, Input, Time_axis_name, Out_axis_name = s1.text_reader(filename)
else:
    print("unsupported data type")

s1.graphData(Time, Input, Output, Time_axis_name, Out_axis_name)

filter = input('Please enter whether you would like to filter your data: 1=yes 2=no: ')
if filter == 1
    output_filt = s2.Filter(Output)
elif filter == 2:
    output_filt = output

order = s1.order_input()

if order == 1:
    datatype = input("Please enter whether this is growth or decay: (1) for growth, or (2) for decay: ")
            if datatype == 1:
                order = 1.1
            elif datatype == 2:
                order = 1.2

if order == 1.1:
    s1.funtiongrowth()
    n = 24
    popt, pcov = curve_fit(functiongrowth, Time, Output,bounds=(n,1000))
    s1.graphDataTF(Time, Input, output_filt, Time_axis_name, Out_axis_name)
    print('The step response is:',popt[0],'(1-e^(-t/'+str(popt[1])+')')
elif order == 1.2:
    x=1
    #decay
elif order == 2:
    x=1
    #second order
