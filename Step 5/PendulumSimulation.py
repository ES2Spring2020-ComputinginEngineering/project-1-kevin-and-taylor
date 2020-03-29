# -*- coding: utf-8 -*-
##################
#ES2 Project 1
#Step 5
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 5
#We received feedback from Professor Cross during office hours
#################

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

def update_system (pos, vel, time1, time2, length):
    # update_system takes 5 inputs: current position and velocity, current time, next time, and length
    # it calculates the next acceleration, velocity and position in that order using physics equations
    # it then returns these values
    dt = time2-time1
    accNext = (-386 / length) * math.sin(pos)    
    velNext = vel + (accNext * dt)
    posNext = pos + (velNext * dt) 
    return posNext,velNext, accNext

def average (array):
    # average takes an array and finds the average distance between indices of said array
    # It is used to calculate average period length 
    differences = []
    arraylist = list(array)
    i = 1
    while i < len(arraylist):
        differences.append (arraylist[i] - arraylist[i-1])
        i += 1
    else:
        array2 = np.array(differences)
        return (np.average(array2))
    
def simulate (length):
    # simulate takes one imput: the length of the pendulum in inches
    # it initializes lists for position, velocity and acceleration, and generates an array of time values
    # it then calls update_system for each value in time, and appends the results to pos, vel, and acc
    # the function then plots pos, vel, and acc with respect to time
    # the function finds the peaks in position, and the associated times
    # it calls average to find the average length of time between these peaks, and prints it
    pos = [math.pi/3]
    vel = [0]
    acc = [334/length]
    time = np.arange(15,step = .001)
    for i in range (1, len(time)):
        posNext, velNext, accNext = update_system (pos[i-1],vel[i-1],time[i-1],time[i], length)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
    print ('Simulation for length = ' + str(length) + ' in')
    plt.plot(time,acc)
    plt.title('Acceleration vs Time')
    plt.xlabel('Time (sec)')
    plt.ylabel('Acceleration (rad/sec^2)')
    plt.show()
    plt.plot(time,vel)
    plt.title('Velocity vs Time')
    plt.xlabel('Time (sec)')
    plt.ylabel('Velocity (rad/sec)')
    plt.show()
    plt.plot(time,pos)    
    plt.title('Position vs Time')
    plt.xlabel('Time (sec)')
    plt.ylabel('Position')
    plt.show()
    pos_peaks,_ = sig.find_peaks (pos)
    peak_time = time[pos_peaks]
    period = average(peak_time)
    print('Period = ' + str(period) + ' sec')
    return

#MAIN SCRIPT
    
simulate(11)
#simulate(13)
#simulate(15)
#simulate(17)
#simulate(19)
