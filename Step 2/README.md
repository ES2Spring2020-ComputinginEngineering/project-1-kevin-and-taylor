# Project1 Part 2 Goes Here

import numpy as np

import matplotlib.pyplot as plt

import math

lengths = [11,13,15,19]

arrlength = np.array (lengths)

def find_time (arrlength):
    arrtime = 2 * math.pi * (np.sqrt (arrlength / 386.22))
    return arrtime 

plt.plot (arrlength, find_time (arrlength))