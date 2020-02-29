##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately
path = "C:/Users/kevin/Desktop/school/es2/project-1-kevin-and-taylor/Step 3"
fin = open("data_capture_19.txt","w")
# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=9, length =100)

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
        fin.write('REEEEEEEEEEEEEEEEEEEEEEEEEE')
        print (incoming)
        mb.display.show(mb.Image.HEART, delay=10, clear=True, wait=False)
    if incoming == 'finish': #Transmission over
        fin.write ('finish')
        fin.close ()
        mb.display.show(mb.Image.CONFUSED)
