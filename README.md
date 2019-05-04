# Auto-Parsing Step Responses

Step responses can be found in many systems, including living biological systems and non-living mechanical systems. This project sets out to automatically produce a function that represents this step response for both first and second order (underdamped) step responses given inputted data.

## Instructions

- Make sure your data file is included in the same folder as the rest of the python files.
- Run main.py and follow prompts to input filenames and answer questions about your data.
- Make sure that when you input file name, first only include the name (ie for data.csv, type 'data' only), then type the data type (ie '.csv').
- If you follow all prompts, a graph of the data with the generated function will be included, and the step response will be printed.
- Included are some example data files that could be run.

## File List

- ArduinoTempCollectionProgram.ino contains a program that can be run on an Arduino microprocessor to collect temperature data.
- FirstOrderFunctions.py contains all functions related to the parsing of data, graphing of data, and curve-fitting of data for the first order step response.
- LightData.txt contains data collected from the micro:Bit's light sensor as a text document.
- MBTempData.txt conatins data collected from the micro:Bit's temperature sensor as a text document.
- MicroBitLightCollectionProgram.py contains the program that can be run on the micro:Bit to collect light data and write it to a text document.
- MicroBitTempCollectionProgram.py contains the program that can be run on the micro:Bit to collect temperature data and write it to a text document.
- MotorData.csv contains data collected from a suspected first order step response for a DC motor recorded by an Arduino. (.csv file)
- PhotoresistorData.csv contains data from a photoresistor sensor in an automatic night-light as a .csv file.
- SecOrdMotorData1.csv contains data from a second order response of a DC motor collected through an Arduino microprocessor.
- SecondOrderFunctions.py contains all functions related to the parsing of data, graphing of data, curve-fitting of data, and optimization of this curve for the second order step response.
- SecordMotorData.csv contains additional data from a second order response of a DC motor system collected through an Arduino microprocessor.
- TemperatureData.csv contains data of a temperature response collected through an Arduino microprocessor running the file ArduinoTempCollectionProgram.ino .
- main.py is the driver of all aforementioned functions. The data included in this repository can be run through this driver.

## Features

This project involved many key python tools including SciPy methods, NumPy, and matplotlib. It also used microprocessors (the Micro:bit and the Arduino) to collect data for use in this project. Some of the most notable methods applied in this project were singal processing (filtering of data), importation of data from files, the fitting of curves to data, and microcontroller-based data collection.

The user is allowed to manipulate the curve produced to better fit their data manually. This allows the user to manually change bounds for variables (for first order responses), such as the Kdc value, repeatedly until the user is satisfied with the results. 

One of the more interesting functions included in this code is the automatic optimization of the second order curves. For second order responses, the user has the option to allow the system to automatically better fit the curve to the data, as the system tries to find the best period from the data. In both the first and second order optimization functions, the user can view the correlation between the curve and the data at all steps of the process so as to find the curve that best fits their data.

The user is also able to use data in either a .csv or .txt format so long as it is formatted correctly (time, input, output for .csv files, and time, output for text files).

Crucial to this project was the SciPy.optimize library. This library contained the curvefit function that was used to take in an 'empty' function and return a curve that fit the data according to this function.
