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

timeYM6090 = [float(l.split()[2]) for l in open("step7-1-regular-Month-2caa-NHSH6090-cy23.txt")]
caaNH6090 = [float(l.split()[-2]) for l in open("step7-1-regular-Month-2caa-NHSH6090-cy23.txt")]
caaSH6090 = [float(l.split()[-1]) for l in open("step7-1-regular-Month-2caa-NHSH6090-cy23.txt")]

timeYM1040 = [float(l.split()[2]) for l in open("step7-1-regular-Month-2caa-NLSL1040-cy23.txt")]
caaNL1040 = [float(l.split()[-2]) for l in open("step7-1-regular-Month-2caa-NLSL1040-cy23.txt")]
caaSL1040 = [float(l.split()[-1]) for l in open("step7-1-regular-Month-2caa-NLSL1040-cy23.txt")]

caaNH6090 = savgol_filter(caaNH6090,13, 1, mode='nearest')
caaSH6090 = savgol_filter(caaSH6090,13, 1, mode='nearest')
caaNL1040 = savgol_filter(caaNL1040,13, 1, mode='nearest')
caaSL1040 = savgol_filter(caaSL1040,13, 1, mode='nearest')
fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.11, bottom=0.06, right=0.98, top=0.96, wspace=0.10, hspace=0.08)

ax1=host_subplot(211)
ax1.plot(timeYM6090,caaNH6090,color='red',linewidth=1.5)
ax1.plot(timeYM6090,caaSH6090,color='blue',linewidth=1.5)
ax1lim1 = 1996.0
ax1lim2 = 2009.0
ay1lim1 = 0.
ay1lim2 = 800
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(50))

ax1.plot([2001.90,2001.90],[0.,1200.0],"gray",lw=1.0,linestyle="--")
ax1.text(2002.2,300.0, "January 2002", fontsize=10, color='dimgray',va='center',rotation=0)
#自定义label的位置
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/1.4,ay1lim2+(ay1lim2-ay1lim1)/25, "Regular Events in Cycle 23", fontsize = 12, va='center')
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/4.93,ay1lim2-(ay1lim2-ay1lim1)/15.5, "High Latitudes", fontsize = 10, va='center')
ax1.plot([1996.5,1997.0],[ay1lim2-(ay1lim2-ay1lim1)/17.5,ay1lim2-(ay1lim2-ay1lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax1.text(1997.2,ay1lim2-(ay1lim2-ay1lim1)/17.5,"Northern Hemisphere",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax1.plot([1996.5,1997.0],[ay1lim2-(ay1lim2-ay1lim1)/8.5,ay1lim2-(ay1lim2-ay1lim1)/8.5],"b",lw=1.5, linestyle="-",label="NH6090")
ax1.text(1997.2,ay1lim2-(ay1lim2-ay1lim1)/8.5,"Southern Hemisphere",color = "b",fontsize=10.0,va='center',rotation=0.0)

plt.setp(ax1.get_xticklabels(), visible=False)

ax2=host_subplot(212)
ax2.plot(timeYM1040,caaNL1040,color='red',linewidth=1.5)
ax2.plot(timeYM1040,caaSL1040,color='blue',linewidth=1.5)
ax2.plot([2001.90,2001.90],[0.,4000.0],"gray",lw=1.0,linestyle="--")

ax2.text(2004.6,1400.0, " July 2004", fontsize=10, color='dimgray',va='center',rotation=0)
#自定义label的位置


ax2lim1 = 1996.0
ax2lim2 = 2009.0
ay2lim1 = 0.0
ay2lim2 = 2400
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(600))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(150))
ax2.text(1994.5,ay2lim2+(ay2lim2-ay2lim1)/30, "Cumulative sum of hemispheric CMEs", fontsize=12, va='center', rotation=90)
ax2.plot([1996.5,1997.0],[ay2lim2-(ay2lim2-ay2lim1)/17.5,ay2lim2-(ay2lim2-ay2lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax2.text(1997.2,ay2lim2-(ay2lim2-ay2lim1)/17.5,"Northern Hemisphere",color = "r",fontsize=10.0,va='center',rotation=0.0)
ax2.plot([1996.5,1997.0],[ay2lim2-(ay2lim2-ay2lim1)/8.5,ay2lim2-(ay2lim2-ay2lim1)/8.5],"b",lw=1.5, linestyle="-",label="NH6090")
ax2.text(1997.2,ay2lim2-(ay2lim2-ay2lim1)/8.5,"Southern Hemisphere",color = "b",fontsize=10.0,va='center',rotation=0.0)
ax2.text(ax2lim2-(ax2lim2-ax2lim1)/5.08,ay2lim2-(ay2lim2-ay2lim1)/15.5, "Low Latitudes", fontsize = 10, va='center')

ax2.set_xlabel('Calendar Year',fontsize=12)


plt.savefig('./z-Figure4-regular-cy23.eps', format='eps',dpi=1000)
plt.savefig('./z-Figure4-regular-cy23.png', format='png',dpi=1000)
plt.show()






