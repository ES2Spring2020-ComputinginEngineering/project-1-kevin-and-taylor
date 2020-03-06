##################
#ES2 Project 1
#receiver.py
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 3
#We received help from Andrew on Piazza.
#################
#This segment of code tunes into the same channel as the pendulum logger microbit. 
#It takes the string transmission recieved via radio and uses function plot to transform the string parameter 'transmission' into a tuple for the MU plotter.
#While it is waiting for transmission input, it displays a square. When it is recieving, it displays a heart every 10 ms (for each incoming message)
#After it has stopped recieving transmissions, it displays a confused face. 
import microbit as mb
import radio

# Change the channel if other microbits are interfering. (Group number=9)
radio.on()  # Turn on radio
radio.config(channel=9, length =100)

def plot (transmission):
    # function takes the transmission as an input, and converts it to a tuple
    # transmission is a string in the format [time, accx, accy, accz]
    # function splits the string at the commas and adds the four values to a list
    # it then converts the list to a tuple and plots it
    transmissionlist = transmission.split (',')
    list2 = []
    for i in range (0,len(transmissionlist)):
        list2.append (float (transmissionlist[i]))
    transmissiontuple = tuple(list2)
    print (transmissiontuple)

# MAIN SCRIPT

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
mb.display.show(mb.Image.SQUARE)

while True:
    incoming = radio.receive() # Read from radio
    if incoming is not None: # message was received
        plot (incoming)
        mb.display.show(mb.Image.HEART, delay=10, clear=True, wait=False)

mb.display.show(mb.Image.CONFUSED) # shows transmission is finished
