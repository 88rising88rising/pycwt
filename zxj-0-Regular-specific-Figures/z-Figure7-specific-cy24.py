#!/usr/bin/env python
# coding: utf-8
from sklearn import datasets, linear_model 
import numpy as np 
import matplotlib.pyplot as plt 
from numpy.core.arrayprint import DatetimeFormat 
from matplotlib import pyplot as plt
from astroML import *   
from mpl_toolkits.axes_grid1 import host_subplot
from sklearn.model_selection  import train_test_split
import matplotlib.ticker as ticker

from scipy.signal import savgol_filter

timeY6090 = [float(l.split()[0]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt")]
timeM6090 = [float(l.split()[1]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt")]
timeYM6090 = [float(l.split()[2]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt")]
caa_absH = [float(l.split()[-2]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt")]
caa_norH = [float(l.split()[-1]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt")]

timeY1040 = [float(l.split()[0]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt")]
timeM1040 = [float(l.split()[1]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt")]
timeYM1040 = [float(l.split()[2]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt")]
caa_absL = [float(l.split()[-2]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt")]
caa_norL = [float(l.split()[-1]) for l in open("step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt")]
print(timeY6090[-1],timeM6090[-1])
print(timeY1040[-1],timeM1040[-1])

caa_absH = savgol_filter(caa_absH,13, 1, mode='nearest')
caa_absL = savgol_filter(caa_absL,13, 1, mode='nearest')

#print(len(timeY6090),timeY6090[-1],timeM6090[-1])
#print(timeY1040[-1],timeM1040[-1])
#red and blue
N_absH = []
N_absHTYM = []
S_absH = []
S_absHTYM = []
N_absL = []
N_absLTYM = []
S_absL = []
S_absLTYM = []
for i in range (0,len(timeM1040)):
    if caa_absH[i] > 0:
        N_absH.append(caa_absH[i])
        N_absHTYM.append(timeYM6090[i])
    if caa_absH[i] <= 0:
        S_absH.append(caa_absH[i])
        S_absHTYM.append(timeYM6090[i])
    if caa_absL[i] > 0:
        N_absL.append(caa_absL[i])
        N_absLTYM.append(timeYM1040[i])
    if caa_absL[i] <= 0:
        S_absL.append(caa_absL[i])
        S_absLTYM.append(timeYM1040[i])

N_absLTYM1 =N_absLTYM[0:20]
N_absL1 =N_absL[0:20]
N_absLTYM2 =N_absLTYM[20::]
N_absL2 =N_absL[20::]

print(N_absLTYM)
print(N_absLTYM1[-1])

S_absLTYM2 =S_absLTYM[0:8]
S_absL2 =S_absL[0:8]
S_absLTYM3 =S_absLTYM[8::]
S_absL3 =S_absL[8::]
fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.11, bottom=0.06, right=0.97, top=0.96, wspace=0.10, hspace=0.08)

ax1=host_subplot(211)
ax1.plot(timeYM6090,caa_absH,color='r',linewidth=1.5,linestyle="--")
ax1.plot([2014.333,2014.333],[-200.0,1200.0],"gray",lw=1.0,linestyle="--")

ax1lim1 = 2009.0
ax1lim2 = 2021.5
ay1lim1 = 0.
ay1lim2 = 600
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(50))
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/1.4,ay1lim2+(ay1lim2-ay1lim1)/25, "Specific Events in Cycle 24", fontsize = 12, va='center')
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/4.93,ay1lim2-(ay1lim2-ay1lim1)/15.5, "High Latitudes", fontsize = 10, va='center')
ax1.plot([2009.5,2010.0],[ay1lim2-(ay1lim2-ay1lim1)/17.5,ay1lim2-(ay1lim2-ay1lim1)/17.5],"r",lw=1.5, linestyle="--",label="NH6090")
ax1.text(2010.2,ay1lim2-(ay1lim2-ay1lim1)/17.5,"Northern Hemisphere",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax1.plot([2009.5,2010.0],[ay1lim2-(ay1lim2-ay1lim1)/8.5,ay1lim2-(ay1lim2-ay1lim1)/8.5],"b",lw=1.5, linestyle="--",label="NH6090")
ax1.text(2010.2,ay1lim2-(ay1lim2-ay1lim1)/8.5,"Southern Hemisphere",color = "b",fontsize=10.0,va='center',rotation=0.0)



ax2=host_subplot(212)
ax2.plot(N_absLTYM1,N_absL1,color='r',linewidth=1.5,linestyle="--")
ax2.plot(N_absLTYM2,N_absL2,color='r',linewidth=1.5,linestyle="--")

ax2.plot(S_absLTYM2,S_absL2,color='b',linewidth=1.5,linestyle="--")
ax2.plot(S_absLTYM3,S_absL3,color='b',linewidth=1.5,linestyle="--")

#pointab
ax2.plot([N_absLTYM1[-1],S_absLTYM2[0]],[N_absL1[-1],S_absL2[0]],color='r',linewidth=1.5)
ax2.plot([S_absLTYM2[-1],N_absLTYM2[0]],[S_absL2[-1],N_absL2[0]],color='r',linewidth=1.5)
ax2.plot([N_absLTYM2[-1],S_absLTYM3[0]],[N_absL2[-1],S_absL3[0]],color='r',linewidth=1.5)


ax2.plot([2014.333,2014.333],[-600.0,4000.0],"gray",lw=1.0,linestyle="--")
ax2.set_xlabel('Calendar Year',fontsize=12)
ax2.plot([2009.0,2020.0],[0.0,0.0],color="dimgray",alpha=0.45,lw=1.0,linestyle="-")
ax2lim1 = 2009.0
ax2lim2 = 2020.0
ay2lim1 = -200
ay2lim2 = 200
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(100))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(50))
ax2.text(2007.8,ay2lim2+(ay2lim2-ay2lim1)/30, "Absolute asymmetry of cumulative sum", fontsize=12, va='center', rotation=90)
ax2.plot([2009.5,2010.0],[ay2lim2-(ay2lim2-ay2lim1)/17.5,ay2lim2-(ay2lim2-ay2lim1)/17.5],"r",lw=1.5, linestyle="--",label="NH6090")
ax2.text(2010.2,ay2lim2-(ay2lim2-ay2lim1)/17.5,"Northern Hemisphere",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax2.plot([2009.5,2010.0],[ay2lim2-(ay2lim2-ay2lim1)/8.5,ay2lim2-(ay2lim2-ay2lim1)/8.5],"b",lw=1.5, linestyle="--",label="NH6090")
ax2.text(2010.2,ay2lim2-(ay2lim2-ay2lim1)/8.5,"Southern Hemisphere",color = "b",fontsize=10.0,va='center',rotation=0.0)
ax2.text(ax2lim2-(ax2lim2-ax2lim1)/5.08,ay2lim2-(ay2lim2-ay2lim1)/15.5, "Low Latitudes", fontsize = 10, va='center')

#ax2.grid(alpha=0.35,linestyle=":")

plt.savefig('z-Figure7-specific-cy24.eps', format='eps',dpi=1000)
plt.savefig('z-Figure7-specific-cy24.png', format='png',dpi=1000)
plt.show()








