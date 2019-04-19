#micro:Bit data collection code
#Contributers: David Fricke and Nicolas Ragusa
#This code can be used on a micro:Bit to collect pendulum data

import microbit
import random

a = str(random.randint(1, 100))
while True:
    if microbit.button_b.was_pressed() == True:                         # waits for button_b pressed
        microbit.sleep(5000)                                            # 5 second delay
        time0 = microbit.running_time()
        with open('light_data' + a + '.txt', 'w') as my_file:   # makes file named 1 to 100
            for i in range(3000):
                microbit.display.set_pixel(2, 2, 9)                     # indicator that it is recording data
                microbit.sleep(5)                                      # sleep at 25 milliseconds
                y = str(microbit.display.read_light_level())                 # writes data in folder (only y)
                time1 = microbit.running_time()
                elapsed_time = str(time1-time0)                         # gets the elapsed time from the last data write
                my_file.write(elapsed_time + ', ' + y + '\n')           # writes data, makes new lines
    #microbit.display.set_pixel(2, 2, 0)