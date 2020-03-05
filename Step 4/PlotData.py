# -*- coding: utf-8 -*-
#INSERT HEADER

import numpy as np
import math
import matplotlib.pyplot as plt
import csv
import scipy.signal as sig

def average (array):
    # takes an array and finds the average distance between indices of said array
    # used to calculate average period length 
    differences = []
    arraylist = list(array)
    i = 1
    while i < len(arraylist):
        differences.append (arraylist[i] - arraylist[i-1])
        i += 1
    else:
        array2 = np.array(differences)
        return (np.average(array2))
    
#REMEMBER TO COMMENT (AND LIKE AND SUBSCRIBE AND SMASH THAT BELL)
def parsedata (filename, lowerbound, upperbound):
    t=[] 
    x=[]
    y=[]
    theta = []
    with open(filename, 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            if not(len(row[0]) == 0): 
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
        theta_array = np.array(theta)
        theta_filt = sig.medfilt(theta_array)
        theta_peaks,_ = sig.find_peaks (theta_filt, distance=25)
        time = np.array(t)
        time_peaks = time[theta_peaks]
        results = [time, x, y, theta, average(time_peaks)]
        return results


def graphdata ():
    lemgths = [19,17,15,13,11]
    periods = []
    
    parseddata = parsedata ('19DATAPENDULUM.csv',10,18)
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta')
    
    parseddata = parsedata ('17DATAPENDULUM.csv',10,18)
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta')
    
    parseddata = parsedata ('15DATAPENDULUM.csv',10,18)
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3]     
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta')
    
    parseddata = parsedata ('13DATAPENDULUM.csv',12,18)
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta')
    
    parseddata = parsedata ('11DATAPENDULUM.csv',10,18)
    t = parseddata [0]
    x = parseddata [1]
    y = parseddata [2]
    theta = parseddata [3] 
    periods.append(parseddata [4])
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = [9,6],sharex=True)
    ax1.plot(t, x)
    ax1.set_title('Time vs X-Acc')
    ax2.plot(t, y, 'tab:orange')
    ax2.set_title('Time vs Y-Acc')
    ax3.plot(t,theta)
    ax3.set_title('Time vs Theta')
    
    plt.figure()
    plt.plot(lemgths, periods)
    plt.plot(lemgths, periods, 'b.')
    plt.show()
    
# MAIN SCRIPT (REEEEEEE)
    
graphdata ()
