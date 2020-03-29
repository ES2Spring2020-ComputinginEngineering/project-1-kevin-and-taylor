# -*- coding: utf-8 -*-
##################
#ES2 Project 1
#receiver.py
#NAME: Taylor Kishinami, Kevin Zhang
#HOURS NEEDED: 0.25
#We worked alone on this part.
#################

#This segment of code takes the 5 lengths of our pendulum (in inches) and calculates the corresponding theoretical period of each length.
#It uses the function find_time to do so, which takes the array of the lengths as a parameter and returns arrtime, an array of those period times.
#It then plots arrlength vs arrtime to create a graph of Length vs Theoretical period of the pendulum.

import numpy as np

import matplotlib.pyplot as plt

import math

lengths = [11,13,15,17,19]

arrlength = np.array (lengths)

def find_time (arrlength):
    arrtime = 2 * math.pi * (np.sqrt (arrlength / 386.22))
    return arrtime 

plt.plot (arrlength, find_time (arrlength))