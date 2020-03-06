# -*- coding: utf-8 -*-
##################
#ES2 Project 1
#Step 4
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 6
#We worked alone on this part.
#################

import numpy as np
import math
import matplotlib.pyplot as plt
import csv
import scipy.signal as sig

def average (array):
    # The function average takes an array and finds the average distance between indices of said array
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
    
def parsedata (filename):
    #The function parsedata takes one parameter, the filename, and parses the csv file into lists of time, acc x, accy, and theta values.
    #It takes the acceleration values at each point in time to calculate the instantaneous theta and appends it to the list of theta values. 
    #It then uses Scipy Signal Library functions to pick out the peaks every 25 data points, and records the timestamp of each peak
    #It then averages it out to calculate the average period.
    #It returns a list of lists containing the time, x acc, y acc, theta, and the average period.
    t=[] 
    x=[]
    y=[]
    theta = []
    with open(filename, 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            if not(len(row[0]) == 0): 
                seconds = float(row[0])/1000
                t.append(seconds) 
                x_accel = float(row[1])
                x.append(x_accel/1000*386.2)
                y_accel = float(row[2])/1000*386.2
                y.append(y_accel/1000*386.2)
                z_accel = float(row[3])
                x_angle = math.atan2(x_accel,math.sqrt((y_accel ** 2) + (z_accel ** 2)))
                theta.append (x_angle) 
        theta_array = np.array(theta)
        theta_filt = sig.medfilt(theta_array)
        theta_peaks,_ = sig.find_peaks (theta_filt, distance=25)
        time = np.array(t)
        time_peaks = time[theta_peaks]
        results = [time, x, y, theta, average(time_peaks)]
        return results

def graphdata ():
    #The function graphdata takes no parameters, and calls the returned lists of parsedata to graph time vs x acc, y acc, and theta, respectively.
    #It graphs the subplots: Time vs x acc, Time vs y acc, and Time vs theta for each data set. 
    #It appends each length's average period to the list periods, and lastly, uses it for graphing Length vs Period
    lemgths = [19,17,15,13,11]
    periods = []
    
    parseddata = parsedata ('19DATAPENDULUM.csv')
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc, Length = 19"')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc, Length = 19"')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta, Length = 19"')
    
    parseddata = parsedata ('17DATAPENDULUM.csv')
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc, Length = 17"')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc, Length = 17"')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta, Length = 17"')
    
    parseddata = parsedata ('15DATAPENDULUM.csv')
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3]     
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc, Length = 15"')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc, Length = 15"')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta, Length = 15"')
    
    parseddata = parsedata ('13DATAPENDULUM.csv')
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc, Length = 13"')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc, Length = 13"')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta, Length = 13"')
    
    parseddata = parsedata ('11DATAPENDULUM.csv')
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc, Length = 11"')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc, Length = 11"')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta, Length = 11"')

    
    plt.figure()
    plt.title('Length vs. Average Period Time')
    plt.plot(lemgths, periods)
    plt.plot(lemgths, periods, 'b.')
    plt.xlabel('Length (in)')
    plt.ylabel('Time (sec)')
    plt.show()
    
# MAIN SCRIPT
    
graphdata ()
