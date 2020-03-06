##################
#ES2 Project 1
#receiver.py
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 1
#We worked alone on this part.
#################
#This segment of code orients the microbit radio to channel 9, then displays a happy face to indicate it is ready to begin transmissions.
#When A is pressed, it begins transmitting a string containing the time, acc x, acc y, and acc z values separated by a comma every 10 ms.
#At this point, we run the pendulum, then the transmissions end when the A button is pressed again.
#The square indicates that it has finished transmitting.
import microbit as mb
import radio

radio.on()  # Turn on radio
radio.config(channel=9, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging

while not mb.button_a.is_pressed():
#     if true, every 10 ms, it generates a string with time elapsed
#     and acceleration in X, Y and Z, in that order
    t = str((mb.running_time ()))
    x = str((mb.accelerometer.get_x()))
    y = str((mb.accelerometer.get_y()))
    z = str((mb.accelerometer.get_z()))
    transmission = (t + ',' + x + ',' + y + ',' + z)
    radio.send (transmission)
    mb.sleep (15)

mb.display.show(mb.Image.SQUARE)  # Display Square when program ends
