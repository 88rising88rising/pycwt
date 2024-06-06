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

time6090Y = [float(l.split()[0]) for l in open("step5-1-regular-Month-4Asymmetry-NHSH6090.txt")]
time6090M = [float(l.split()[1]) for l in open("step5-1-regular-Month-4Asymmetry-NHSH6090.txt")]
time6090 = [float(l.split()[2]) for l in open("step5-1-regular-Month-4Asymmetry-NHSH6090.txt")]
absNHSH6090 = [float(l.split()[-2]) for l in open("step5-1-regular-Month-4Asymmetry-NHSH6090.txt")]
norNHSH6090 = [float(l.split()[-1]) for l in open("step5-1-regular-Month-4Asymmetry-NHSH6090.txt")]

time1040Y = [float(l.split()[0]) for l in open("step5-1-regular-Month-4Asymmetry-NLSL1040.txt")]
time1040M = [float(l.split()[1]) for l in open("step5-1-regular-Month-4Asymmetry-NLSL1040.txt")]
time1040 = [float(l.split()[2]) for l in open("step5-1-regular-Month-4Asymmetry-NLSL1040.txt")]
absNLSL1040 = [float(l.split()[-2]) for l in open("step5-1-regular-Month-4Asymmetry-NLSL1040.txt")]
norNLSL1040 = [float(l.split()[-1]) for l in open("step5-1-regular-Month-4Asymmetry-NLSL1040.txt")]
#absNHSH6090 = savgol_filter(absNHSH6090,13, 1, mode='nearest')
#absNLSL1040 = savgol_filter(absNLSL1040,13, 1, mode='nearest')

time609023BM = time6090[0:65]
time609023AM = time6090[65:150]
time609024BM = time6090[150:214]
time609024AM = time6090[214::]
absNHSH609023BM = absNHSH6090[0:65]
absNHSH609023AM = absNHSH6090[65:150]
absNHSH609024BM = absNHSH6090[150:214]
absNHSH609024AM = absNHSH6090[214::]

time104023BM = time1040[0:65]
time104023AM = time1040[65:150]
time104024BM = time1040[150:214]
time104024AM = time1040[214::]
absNLSL104023BM = absNLSL1040[0:65]
absNLSL104023AM = absNLSL1040[65:150]
absNLSL104024BM = absNLSL1040[150:214]
absNLSL104024AM = absNLSL1040[214::]

time6090Y23BM = time6090Y[0:65]
time6090Y23AM = time6090Y[65:150]
time6090Y24BM = time6090Y[150:214]
time6090Y24AM = time6090Y[214::]

time6090M23BM = time6090M[0:65]
time6090M23AM = time6090M[65:150]
time6090M24BM = time6090M[150:214]
time6090M24AM = time6090M[214::]

print("time6090Y23BM",time6090Y23BM[0],time6090M23BM[0],time6090Y23BM[-1],time6090M23BM[-1])
print("time6090Y23AM",time6090Y23AM[0],time6090M23AM[0],time6090Y23AM[-1],time6090M23AM[-1])
print("time6090Y24BM",time6090Y24BM[0],time6090M24BM[0],time6090Y24BM[-1],time6090M24BM[-1])
print("time6090Y24AM",time6090Y24AM[0],time6090M24AM[0],time6090Y24AM[-1],time6090M24AM[-1])

time1040Y23BM = time1040Y[0:65]
time1040Y23AM = time1040Y[65:150]
time1040Y24BM = time1040Y[150:214]
time1040Y24AM = time1040Y[214::]

time1040M23BM = time1040M[0:65]
time1040M23AM = time1040M[65:150]
time1040M24BM = time1040M[150:214]
time1040M24AM = time1040M[214::]

print("time1040Y23BM",time1040Y23BM[0],time1040M23BM[0],time1040Y23BM[-1],time1040M23BM[-1])
print("time1040Y23AM",time1040Y23AM[0],time1040M23AM[0],time1040Y23AM[-1],time1040M23AM[-1])
print("time1040Y24BM",time1040Y24BM[0],time1040M24BM[0],time1040Y24BM[-1],time1040M24BM[-1])
print("time1040Y24AM",time1040Y24AM[0],time1040M24AM[0],time1040Y24AM[-1],time1040M24AM[-1])

absNHSH609024BM = savgol_filter(absNHSH609024BM,13, 1, mode='nearest')
absNLSL104024BM = savgol_filter(absNLSL104024BM,13, 1, mode='nearest')
absNHSH609024AM = savgol_filter(absNHSH609024AM,13, 1, mode='nearest')
absNLSL104024AM = savgol_filter(absNLSL104024AM,13, 1, mode='nearest')


fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.09, bottom=0.06, right=0.98, top=0.96, wspace=0.10, hspace=0.08)

ax1 = host_subplot(211)
ax1.scatter(absNHSH609024BM,absNLSL104024BM,c="red",s=3)

#ax1.set_xlabel("Calendar Year",fontsize = 12)
#ax1.invert_yaxis()
ax1lim1 = -6.0
ax1lim2 = 6.5
ay1lim1 = -6
ay1lim2 = 8.0
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(2))
ax1.axhline(y=0., ls=':', c='k')
#ax1.plot([-40.0,22.0],[0.0,0.0],"gray",lw=1.0,linestyle="--")
#ax1.plot([2001.917,2001.917],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")
#ax1.plot([2009.0,2009.0],[-120.0,120.0],"black",lw=1.0,linestyle="-")
#ax1.plot([2014.333,2014.333],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")

Aabs609024BM, Babs609024BM = optimize.curve_fit(f_1, absNHSH609024BM,absNLSL104024BM)[0]
preabsNLSL104024BM = []
for x1 in absNHSH609024BM:
    y1 = Aabs609024BM*x1 + Babs609024BM
    preabsNLSL104024BM.append(y1)
ax1.plot(absNHSH609024BM, preabsNLSL104024BM,lw=1.5,c="blue")
print("Aabs609024BM= ",Aabs609024BM)
print("Babs609024BM= ",Babs609024BM)
print("abs609024cacl_corrsmooth",calc_corr1(absNHSH609024BM,absNLSL104024BM))
#ax1.text(1996.2,35.0, "cycle24 Correlation Coefficient: -0.273, fitpar: A= -1.279 B= 2558.15 ", fontsize=4.0, va='center',rotation=0.0)
#ax1.text(1996.2,32.5, "cycle24 Correlation Coefficient: -0.132, fitpar: A= -1.109 B= 2242.13 ", fontsize=4.0, va='center',rotation=0.0)
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/1.4,ay1lim2+(ay1lim2-ay1lim1)/25, "Regular Events in Cycle 24", fontsize = 12, va='center')
ax1.text(ax1lim1+(ax1lim2-ax1lim1)/25,ay1lim2-(ay1lim2-ay1lim1)/16, "Prior to April 2014", fontsize=10, va='center')



ax2 = host_subplot(212)
ax2.scatter(absNHSH609024AM,absNLSL104024AM,c="red",s=3)
ax2.set_xlabel('Absolute asymmetry index of high-latitude CMEs',fontsize=12)
#ax2.set_ylabel("Absolute asymmetry values of the CMEs at low latitudes in cycle 24",fontsize = 12)

ax2lim1 = -0.2
ax2lim2 = 4.2
ay2lim1 = -4.0
ay2lim2 = 8.0
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)

ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(2))
#ax2.text(1996.2,75.0, "Correlation Coefficient: 0.091, fitpar: A= -0.279 B= -560.02 ", fontsize=4.0, va='center',rotation=0.0)
ax2.axhline(y=0., ls=':', c='k')
#ax2.plot([2001.917,2001.917],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")
#ax2.plot([2009.0,2009.0],[-120.0,120.0],"black",lw=1.0,linestyle="-")
#ax2.plot([2014.333,2014.333],[-120.0,120.0],"darkgray",lw=1.0,linestyle="--")

AabsNHSL24AM, BabsNHSL24AM = optimize.curve_fit(f_1, absNHSH609024AM,absNLSL104024AM)[0]
preabsNLSL104024AM = []
for x1 in absNHSH609024AM:
    y1 = AabsNHSL24AM*x1 + BabsNHSL24AM
    preabsNLSL104024AM.append(y1)
ax2.plot(absNHSH609024AM, preabsNLSL104024AM,lw=1.5,c="blue")
print("AabsNHSL24AM= ",AabsNHSL24AM)
print("BabsNHSL24AM= ",BabsNHSL24AM)
print("abs104024cacl_corrsmooth",calc_corr1(absNHSH609024AM,absNLSL104024AM))
#ax2.text(1996.2,70.0, "cycle24 Correlation Coefficient: -0.273, fitpar: A= -1.279 B= 2558.15 ", fontsize=4.0, va='center',rotation=0.0)
ax2.text(ax2lim1-(ax2lim2-ax2lim1)/11, ay2lim2+(ay2lim2-ay2lim1)/12.5, "Absolute asymmetry index of low-latitude CMEs", fontsize=12, va='center', rotation=90)
ax2.text(ax2lim1+(ax2lim2-ax2lim1)/25, ay2lim2-(ay2lim2-ay2lim1)/16, "After April 2014", fontsize=10, va='center', rotation=0)

plt.savefig('z-Figure3-regular-cy24.eps', format='eps',dpi=1000)
plt.savefig('z-Figure3-regular-cy24.png', format='png',dpi=1000)
plt.show()

