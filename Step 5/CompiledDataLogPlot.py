# -*- coding: utf-8 -*-
##################
#ES2 Project 1
#CompiledDataLogPlot.py
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 0.5
#We worked alone on this part.
#################
#This code creates lists of the periods we calculated for 5 lengths at each stage of the experiment
#Theoretical, Data Collection, Simulation, and Dampened Simulation data sets will be compared and analyzed.
import matplotlib.pyplot as plt
import matplotlib.patches as patch
lengthslist = [11,13,15,17,19]
theolist = [1.06037,1.15275,1.23825,1.311822,1.39360]
datalist = [1.10844,1.17314,1.25214,1.35933,1.43367]
simulist = [1.13825,1.23745,1.3292,1.415,1.496]
dampsimulist = [1.10773,1.174,1.265,1.3497,1.4307]
#This code graphs each set of periods to their respective lengths and generates a log-log graph with colored lines and a legend.
plt.figure(figsize=(9,6))
plt.plot(lengthslist,theolist,'r-',lengthslist,datalist,'k-',lengthslist,simulist,'g-',lengthslist,dampsimulist,'b-')
red = patch.Patch(color='red',label = 'Theoretical')
black = patch.Patch(color='k',label = 'Collected Data')
green = patch.Patch(color='g',label = 'Simulation')
blue = patch.Patch(color='b',label = 'Dampened Simulation')
plt.legend(handles=[red, black, green, blue])
plt.xscale('log')
plt.yscale('log')
plt.title('Compiled Data of Lengths vs Periods')
plt.xlabel ('Lengths (in)')
plt.ylabel ('Periods (s)')
plt.show()
 