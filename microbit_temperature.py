#micro:Bit data collection code
#Contributers: David Fricke and Nicolas Ragusa
#This code can be used on a micro:Bit to collect temperature data

import microbit
import random

a = str(random.randint(1, 100))
while True:
    if microbit.button_a.was_pressed() == True:                         # waits for button_a pressed
        microbit.sleep(3000)                                            # 3 second delay
        time0 = microbit.running_time()
        with open('light_data' + a + '.txt', 'w') as my_file:           # makes file named 1 to 100
            for i in range(3000):
                microbit.display.set_pixel(2, 2, 9)                     # indicator that it is recording data
                microbit.sleep(5)                                       # sleep at 25 milliseconds
                y = str(microbit.temperature())                         # writes data in file
                time1 = microbit.running_time()
                elapsed_time = str(time1-time0)                         # gets the elapsed time from the last data write
                my_file.write(elapsed_time + ', ' + y + '\n')           # writes data, makes new lines
    microbit.display.set_pixel(2, 2, 0)