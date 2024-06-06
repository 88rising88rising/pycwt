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

timeY6090 = [float(l.split()[0]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt")]
timeM6090 = [float(l.split()[1]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt")]
timeYM6090 = [float(l.split()[2]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt")]
caa_absH = [float(l.split()[-2]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt")]
caa_norH = [float(l.split()[-1]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt")]

timeY1040 = [float(l.split()[0]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt")]
timeM1040 = [float(l.split()[1]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt")]
timeYM1040 = [float(l.split()[2]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt")]
caa_absL = [float(l.split()[-2]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt")]
caa_norL = [float(l.split()[-1]) for l in open("step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt")]

caa_absH = savgol_filter(caa_absH,13, 1, mode='nearest')
caa_absL = savgol_filter(caa_absL,13, 1, mode='nearest')
print(timeY6090[-1],timeM6090[-1])
print(timeY1040[-1],timeM1040[-1])

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
        

print(len(N_absH),N_absHTYM[0],N_absHTYM[-1],N_absH)
print(len(S_absH),S_absHTYM[0],S_absHTYM[-1],S_absH)
for num in caa_absH:
    print(round(num,4))


S_absHTYMA = S_absHTYM[0:30]
S_absHTYMB = S_absHTYM[30::]
S_absHA = S_absH[0:30]
S_absHB = S_absH[30::]


S_absLTYMA = S_absLTYM[0:21]
S_absLTYMB = S_absLTYM[21::]
S_absLA = S_absL[0:21]
S_absLB = S_absL[21::]

fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.11, bottom=0.06, right=0.98, top=0.96, wspace=0.10, hspace=0.08)
ax1=host_subplot(211)
#ax1.text(1999.5,110.0, "Regular events in cycle 23", fontsize = 12, va='center')
#S
ax1.plot(S_absHTYMA,S_absHA,color='b',linewidth=1.5)
#S-N point
ax1.plot([S_absHTYMA[-1],N_absHTYM[0]],[S_absHA[-1],N_absH[0]],color='r',linewidth=1.5)
#N
ax1.plot(N_absHTYM,N_absH,color='r',linewidth=1.5)
#N-S point
ax1.plot([N_absHTYM[-1],S_absHTYMB[0]],[N_absH[-1],S_absHB[0]],color='r',linewidth=1.5)
#S
ax1.plot(S_absHTYMB,S_absHB,color='b',linewidth=1.5)

ax1.plot([2001.90,2001.90],[-160.0,200.0],"gray",lw=1.0,linestyle="--")
ax1.plot([1996.0,2010.0],[0.0,0.0],color="dimgray",alpha=0.45,lw=1.0,linestyle="-")



ax1.text(1998.8,-12.0, "September 1998", fontsize=10, color='dimgray',va='center',rotation=0)
ax1lim1 = 1996.0
ax1lim2 = 2009.0
ay1lim1 = -100
ay1lim2 = 100
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))

ax1.text(ax1lim2-(ax1lim2-ax1lim1)/1.4,ay1lim2+(ay1lim2-ay1lim1)/25, "Regular Events in Cycle 23", fontsize = 12, va='center')
ax1.plot([1996.5,1997.],[ay1lim2-(ay1lim2-ay1lim1)/17.5,ay1lim2-(ay1lim2-ay1lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax1.text(1997.2,ay1lim2-(ay1lim2-ay1lim1)/17.5,"Northern Dominant",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax1.plot([1996.5,1997.],[ay1lim2-(ay1lim2-ay1lim1)/8.5,ay1lim2-(ay1lim2-ay1lim1)/8.5],"b",lw=1.5, linestyle="-",label="NH6090")
ax1.text(1997.2,ay1lim2-(ay1lim2-ay1lim1)/8.5,"Southern Dominant",color = "b",fontsize=10.0,va='center',rotation=0.0)
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/4.93,ay1lim2-(ay1lim2-ay1lim1)/15.5, "High Latitudes", fontsize = 10, va='center')
plt.setp(ax1.get_xticklabels(), visible=False)

ax2=host_subplot(212)
ax2.plot(S_absLTYMA,S_absLA,color='b',linewidth=1.5)
ax2.plot([S_absLTYMA[-1],N_absLTYM[0]],[S_absLA[-1],N_absL[0]],color='r',linewidth=1.5)

ax2.plot(N_absLTYM,N_absL,color='r',linewidth=1.5)
ax2.plot([S_absLTYMB[0],N_absLTYM[-1]],[S_absLB[0],N_absL[-1]],color='r',linewidth=1.5)

ax2.plot(S_absLTYMB,S_absLB,color='b',linewidth=1.5)
ax2.plot([2001.90,2001.90],[-600.0,4000.0],"gray",lw=1.0,linestyle="--")

ax2.text(1994.5,120.0, "", fontsize=12, va='center', rotation=90)
ax2.text(2004.7,10.0, " August 2004", fontsize=10, color='dimgray',va='center',rotation=0)
ax2.text(1997.8,-18.0, " September 1997", fontsize=10, color='dimgray',va='center',rotation=0)
ax2.plot([1996.0,2010.0],[0.0,0.0],color="dimgray",alpha=0.45,lw=1.0,linestyle="-")

ax2lim1 = 1996.
ax2lim2 = 2009.
ay2lim1 = -120.
ay2lim2 = 130.
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(60))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(20))

ax2.text(1994.5,ay2lim2+(ay2lim2-ay2lim1)/30, "Absolute asymmetry of cumulative sum", fontsize = 12, va='center',rotation=90.0)
ax2.plot([1996.5,1997.],[ay2lim2-(ay2lim2-ay2lim1)/17.5,ay2lim2-(ay2lim2-ay2lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax2.text(1997.2,ay2lim2-(ay2lim2-ay2lim1)/17.5,"Northern Dominant",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax2.plot([1996.5,1997.],[ay2lim2-(ay2lim2-ay2lim1)/8.5,ay2lim2-(ay2lim2-ay2lim1)/8.5],"b",lw=1.5, linestyle="-",label="NH6090")
ax2.text(1997.2,ay2lim2-(ay2lim2-ay2lim1)/8.5,"Southern Dominant",color = "b",fontsize=10.0,va='center',rotation=0.0)
ax2.text(ax2lim2-(ax2lim2-ax2lim1)/5.08,ay2lim2-(ay2lim2-ay2lim1)/15.5, "Low Latitudes", fontsize = 10, va='center')
ax2.set_xlabel('Calendar Year',fontsize=12)
#ax2.grid(alpha=0.35,linestyle=":")
plt.savefig('z-Figure5-regular-cy23.eps', format='eps',dpi=1000)
plt.savefig('z-Figure5-regular-cy23.png', format='png',dpi=1000)
plt.show()
