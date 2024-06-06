#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import numpy
import numpy as np
from numpy import *
from pandas import Series
import pycwt as wavelet
from pycwt.helpers import find
from sklearn import datasets, linear_model 
from numpy.core.arrayprint import DatetimeFormat
from matplotlib import *
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
from sklearn.model_selection  import train_test_split
from matplotlib.pyplot import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter

def f_1(x, A, B):
 return A * x + B

def calc_corr1(a, b):
    s1 = Series(a)
    s2 = Series(b)
    return s1.corr(s2)
time6090 = [float(l.split()[2]) for l in open("step5-1-specific-Month-4Asymmetry-NHSH6090.txt")]
absNHSH6090 = [float(l.split()[-2]) for l in open("step5-1-specific-Month-4Asymmetry-NHSH6090.txt")]
norNHSH6090 = [float(l.split()[-1]) for l in open("step5-1-specific-Month-4Asymmetry-NHSH6090.txt")]

timeY = [float(l.split()[0]) for l in open("step5-1-specific-Month-4Asymmetry-NLSL1040.txt")]
timeM = [float(l.split()[1]) for l in open("step5-1-specific-Month-4Asymmetry-NLSL1040.txt")]
time1040 = [float(l.split()[2]) for l in open("step5-1-specific-Month-4Asymmetry-NLSL1040.txt")]
absNLSL1040 = [float(l.split()[-2]) for l in open("step5-1-specific-Month-4Asymmetry-NLSL1040.txt")]
norNLSL1040 = [float(l.split()[-1]) for l in open("step5-1-specific-Month-4Asymmetry-NLSL1040.txt")]
#print(timeY[151],timeM[151])
#absNHSH6090 = savgol_filter(absNHSH6090,13, 1, mode='nearest')
#absNLSL1040 = savgol_filter(absNLSL1040,13, 1, mode='nearest')
time609023BM = time6090[0:66]
time609023AM = time6090[66:151]
time609024BM = time6090[151:215]
time609024AM = time6090[215::]
absNHSH609023BM = absNHSH6090[0:66]
absNHSH609023AM = absNHSH6090[66:151]
absNHSH609024BM = absNHSH6090[151:215]
absNHSH609024AM = absNHSH6090[215::]

time104023BM = time1040[0:66]
time104023AM = time1040[66:151]
time104024BM = time1040[151:215]
time104024AM = time1040[215::]
absNLSL104023BM = absNLSL1040[0:66]
absNLSL104023AM = absNLSL1040[66:151]
absNLSL104024BM = absNLSL1040[151:215]
absNLSL104024AM = absNLSL1040[215::]

timeY23BM = timeY[0:66]
timeY23AM = timeY[66:151]
timeY24BM = timeY[151:215]
timeY24AM = timeY[215::]

timeM23BM = timeM[0:66]
timeM23AM = timeM[66:151]
timeM24BM = timeM[151:215]
timeM24AM = timeM[215::]
print("timeY23BM",timeY23BM[0],timeM23BM[0],timeY23BM[-1],timeM23BM[-1])
print("timeY23AM",timeY23AM[0],timeM23AM[0],timeY23AM[-1],timeM23AM[-1])
print("timeY24BM",timeY24BM[0],timeM24BM[0],timeY24BM[-1],timeM24BM[-1])
print("timeY24AM",timeY24AM[0],timeM24AM[0],timeY24AM[-1],timeM24AM[-1])


absNHSH609023BM = savgol_filter(absNHSH609023BM,13, 1, mode='nearest')
absNLSL104023BM = savgol_filter(absNLSL104023BM,13, 1, mode='nearest')
absNHSH609023AM = savgol_filter(absNHSH609023AM,13, 1, mode='nearest')
absNLSL104023AM = savgol_filter(absNLSL104023AM,13, 1, mode='nearest')

fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.09, bottom=0.06, right=0.98, top=0.96, wspace=0.10, hspace=0.08)

ax1 = host_subplot(211)
ax1.scatter(absNHSH609023BM,absNLSL104023BM,c="red",s=3)
#ax1.set_xlabel("Calendar Year",fontsize = 12)
#ax1.invert_yaxis()
ax1lim1 = -0.6
ax1lim2 = 2.1
ay1lim1 = -2.0
ay1lim2 = 5.0
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.axhline(y=0., ls=':', c='k')
#ax1.plot([-40.0,22.0],[0.0,0.0],"gray",lw=1.0,linestyle="--")
#ax1.plot([2001.917,2001.917],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")
#ax1.plot([2009.0,2009.0],[-120.0,120.0],"black",lw=1.0,linestyle="-")
#ax1.plot([2014.333,2014.333],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")

Aabs609023BM, Babs609023BM = optimize.curve_fit(f_1, absNHSH609023BM,absNLSL104023BM)[0]
preabsNLSL104023BM = []
for x1 in absNHSH609023BM:
    y1 = Aabs609023BM*x1 + Babs609023BM
    preabsNLSL104023BM.append(y1)
ax1.plot(absNHSH609023BM, preabsNLSL104023BM,lw=1.5,c="blue")
print("Aabs609023BM= ",Aabs609023BM)
print("Babs609023BM= ",Babs609023BM)
print("abs609023cacl_corrsmooth",calc_corr1(absNHSH609023BM,absNLSL104023BM))
#ax1.text(1996.2,35.0, "cycle23 Correlation Coefficient: -0.273, fitpar: A= -1.279 B= 2558.15 ", fontsize=4.0, va='center',rotation=0.0)
#ax1.text(1996.2,32.5, "cycle24 Correlation Coefficient: -0.132, fitpar: A= -1.109 B= 2242.13 ", fontsize=4.0, va='center',rotation=0.0)
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/1.4,ay1lim2+(ay1lim2-ay1lim1)/25, "Specific Events in Cycle 23", fontsize = 12, va='center')
ax1.text(ax1lim1+(ax1lim2-ax1lim1)/25,ay1lim2-(ay1lim2-ay1lim1)/16, "Prior to November 2001", fontsize = 10, va='center')

ax2 = host_subplot(212)
ax2.scatter(absNHSH609023AM,absNLSL104023AM,c="red",s=3)
ax2.set_xlabel('Absolute asymmetry index of high-latitude CMEs',fontsize=12)
#ax2.set_ylabel("Absolute asymmetry values of the CMEs at low latitudes in cycle 23",fontsize = 12)

ax2lim1 = -1.8
ax2lim2 = 2.8
ay2lim1 = -15.0
ay2lim2 = 9.0
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(0.75))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(6))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(3))
#ax2.text(1996.2,75.0, "Correlation Coefficient: 0.091, fitpar: A= -0.279 B= -560.02 ", fontsize=4.0, va='center',rotation=0.0)
ax2.axhline(y=0., ls=':', c='k')
#ax2.plot([2001.917,2001.917],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")
#ax2.plot([2009.0,2009.0],[-120.0,120.0],"black",lw=1.0,linestyle="-")
#ax2.plot([2014.333,2014.333],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")

AabsNHSL23AM, BabsNHSL23AM = optimize.curve_fit(f_1, absNHSH609023AM,absNLSL104023AM)[0]
preabsNLSL104023AM = []
for x1 in absNHSH609023AM:
    y1 = AabsNHSL23AM*x1 + BabsNHSL23AM
    preabsNLSL104023AM.append(y1)
ax2.plot(absNHSH609023AM, preabsNLSL104023AM,lw=1.5,c="blue")
print("AabsNHSLAM= ",AabsNHSL23AM)
print("BabsNHSLAM= ",BabsNHSL23AM)
print("abs104023cacl_corrsmooth",calc_corr1(absNHSH609023AM,absNLSL104023AM))
#ax2.text(1996.2,70.0, "cycle23 Correlation Coefficient: -0.273, fitpar: A= -1.279 B= 2558.15 ", fontsize=4.0, va='center',rotation=0.0)
ax2.text(ax2lim1-(ax2lim2-ax2lim1)/11, ay2lim2+(ay2lim2-ay2lim1)/12.5, "Absolute asymmetry index of low-latitude CMEs", fontsize=12, va='center', rotation=90)
ax2.text(ax2lim1+(ax2lim2-ax2lim1)/25, ay2lim2-(ay2lim2-ay2lim1)/16, "After November 2001", fontsize = 10, va='center', rotation=0)

plt.savefig('z-Figure2-specific-cy23.eps', format='eps',dpi=1000)
plt.savefig('z-Figure2-specific-cy23.png', format='png',dpi=1000)
plt.show()
