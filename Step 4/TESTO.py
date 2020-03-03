# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:30:20 2020

@author: kishi
"""

import numpy as np
import math
import matplotlib.pyplot as plt

t=[] 
x=[]
y=[]
z=[]
theta = []

def plotdata (filename, lowerbound, upperbound):
    with open(filename, 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            if not((len(row[0]) == 0) or (len(row[1]) == 0) or (len(row[2]) == 0)): 
                seconds = float(row[0])/1000
                if lowerbound <= seconds <= upperbound:
                    t.append(seconds) 
                    x_accel = float(row[1])
                    x.append(x_accel/1000*386.2)
                    y_accel = float(row[2])/1000*386.2
                    y.append(y_accel/1000*386.2)
                    z_accel = float(row[3])
                    x_angle = math.atan2(x_accel,math.sqrt((y_accel ** 2) + (z_accel ** 2)))
                    theta.append (x_angle) 
    print (filename)
    plt.plot(t,x, marker='o')
    plt.title('Time vs Acceleration X')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration X in/second^2')
    plt.show()
    plt.plot(t,y, marker='o')
    plt.title('Time vs Acceleration Y')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration Y in/second^2')
    plt.show()
    plt.plot(t,theta, marker='o')
    plt.title('Time vs Angle')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Angle (radians)')
    plt.show()

plotdata ("19DATAPENDULUMFINAL.csv",8,12)