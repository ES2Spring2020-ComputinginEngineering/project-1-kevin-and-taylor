# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:04:23 2020

@author: kevin
"""

#STEP 5 BOIZZZZZZ

import numpy as np
import math
import matplotlib.pyplot as plt

def update_system (pos, vel, time1, time2):
    dt = time2-time1
    accNext = (386 / 11) * math.sin(pos)    
    velNext = vel + (accNext * dt)
    posNext = pos + (vel * dt) + ((accNext * (dt ** 2)) / 2)
    return posNext,velNext, accNext

def print_system(time,pos,vel,acc):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel)
    print("ACCELERATION: ", acc, "\n")
    
def simulate (length):
    pos = [math.pi/3]
    vel = [0]
    acc = [334/length]
    time = np.arange(15,step = 1)
    for i in range (1, len(time)):
        posNext, velNext, accNext = update_system (pos[i-1],vel[i-1],time[i-1],time[i])
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        print_system(time[i],pos[i],vel[i],acc[i])
    plt.plot(time,acc)
    plt.show()
    plt.plot(time,vel)
    plt.show()
    plt.plot(time,pos)
    plt.show()
    return

simulate(11)

#def update_system(acc,pos,vel,time1,time2):
#    # position and velocity update below
#    dt = time2-time1
#    posNext = pos+vel*dt
#    velNext = vel+acc*dt
#    return posNext,velNext
#
#def print_system(time,pos,vel):
#    print("TIME:     ", time)
#    print("POSITION: ", pos)
#    print("VELOCITY: ", vel, "\n")
#
## initial conditions
#pos = [0]
#vel = [0]
#acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
#time = np.linspace(0,20,21)
#print_system(time[0],pos[0],vel[0])
#
#i = 1
#while i < len(time):
#    # update position and velocity using previous values and time step
#    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
#    pos.append(posNext)
#    vel.append(velNext)
#    print_system(time[i],pos[i],vel[i])
#    i += 1