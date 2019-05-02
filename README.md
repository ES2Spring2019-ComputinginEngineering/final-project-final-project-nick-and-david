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
- SecOrdMotorData1.csv 
- SecondOrderFunctions.py contains all functions related to the parsing of data, graphing of data, curve-fitting of data, and optimization of this curve for the second order step response.
- SecordMotorData.csv 
- TemperatureData.csv 
- main.py is the driver of all aforementioned functions. The data included in this repository can be run through this driver.

## Features
descriptions of any key design choices (for example what methods your applied) and what libraries or functions were important in the design.







## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
