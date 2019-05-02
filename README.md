# Auto-Parsing Step Responses

Step responses can be found in almost any system, including living biological systems and non-living mecanical systems. This project sets out to automatically produce a function that represents this step response for both first and second order step responses given inputted data.

## Instructions

- Make sure your data file is included in the same folder as the rest of the python files.
- Run main.py and follow prompts to input filenames and answer questions about your data.
- Make sure that when you input file name, first only include the name (ie for data.csv, type 'data' only), then type the data type (ie '.csv').
- If you follow all prompts, a graph of the data with the generated function will be included, and the step response will be printed.
- Included are some example data files that could be run.

## File List

- ArduinoTempCollectionProgram.ino contains a program that can be run on an arduino microprocessor to collect temperature data.
- FirstOrderFunctions.py contains all functions related to the parsing of data, graphing of data, and curve-fitting of data for the first order step response.
- LightData.txt contains data collected from the micro:Bit's light sensor as a text document.
- MBTempData.txt conatins data collected from the micro:Bit's temperature sensor as a text document.
- MicroBitLightCollectionProgram.py contains the program that can be run on the micro:Bit to collect light data and write it to a text document.
- MicroBitTempCollectionProgram.py contains the program that can be run on the micro:Bit to collect temperature data and write it to a text document.
- MotorData.csv contains data collected from a DC motor through an arduino the records the output of the motor over time (first order response) as a .csv file.
- PhotoresistorData.csv contains data from a photoresistor sensor in an automatic night-light as a .csv file.
- SecOrdMotorData1.csv contains data from a second order response of a DC motor collected through an arduino microprocessor.
- SecondOrderFunctions.py contains all functions related to the parsing of data, graphing of data, curve-fitting of data, and optimization of this curve for the second order step response.
- SecordMotorData.csv contains additional data from a second order response of a DC motor collected through an arduino microprocessor.
- TemperatureData.csv contains data of a temperature response collected through an arduino microprocessor running the file ArduinoTempCollectionProgram.ino .
- main.py is the driver of all aforementioned functions. The data included in this repository can be run through this driver.

## Features
This project contains many key functions for analyzing the data.
One design choice made was the ability to allow to user to manipulate the curve produced to better fit their data manually. This allows the user to manually change variables (for first order responses) such as the steady state value repeatedly until the user is satisfied with the results. For second order responses, the user has the option to allow the system to automatically optimize the curve to the data. In both cases, the user can view the correlation between the curve and the data at all steps of the process so as to find the curve that best fits their data.

The user is also able to use data in either a .csv or .txt format!

Crucial to this project was the SciPy.optimize library. This library contained the curvefit function that was used to take in an 'empty' function and return and curve that fit the data according to this function.
