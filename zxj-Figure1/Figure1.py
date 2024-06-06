from cProfile import label
import matplotlib.pyplot as plt
import pylab
from matplotlib import *
from mpl_toolkits.axes_grid1 import host_subplot#lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
#from astroML.plotting import setup_text_plots
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter
timeY6090 = [float(l.split()[0]) for l in open("step4-month-2count-Latitude-NHSH6090.txt")]
timeM6090 = [float(l.split()[1]) for l in open("step4-month-2count-Latitude-NHSH6090.txt")]
time6090 = [float(l.split()[2]) for l in open("step4-month-2count-Latitude-NHSH6090.txt")]
NH6090 = [float(l.split()[4]) for l in open("step4-month-2count-Latitude-NHSH6090.txt")]
SH6090 = [float(l.split()[5]) for l in open("step4-month-2count-Latitude-NHSH6090.txt")]

timeY1040 = [float(l.split()[0]) for l in open("step4-Month-2count-Latitude-NLSL1040.txt")]
timeM1040 = [float(l.split()[1]) for l in open("step4-Month-2count-Latitude-NLSL1040.txt")]
time1040 = [float(l.split()[2]) for l in open("step4-Month-2count-Latitude-NLSL1040.txt")]
NL1040 = [float(l.split()[4]) for l in open("step4-Month-2count-Latitude-NLSL1040.txt")]
SL1040 = [float(l.split()[5]) for l in open("step4-Month-2count-Latitude-NLSL1040.txt")]

print(timeY6090[-1],timeM6090[-1])
print(timeY1040[-1],timeM1040[-1])
#SLS1040 = [float(l.split()[-1]) for l in open("step4-Month-2count-smooth-NLSL1040.txt")]

NH6090_smo = savgol_filter(NH6090,13, 1, mode='nearest')
SH6090_smo = savgol_filter(SH6090,13, 1, mode='nearest')
NL1040_smo = savgol_filter(NL1040,13, 1, mode='nearest')
SL1040_sm0 = savgol_filter(SL1040,13, 1, mode='nearest')

fig = plt.figure(figsize =(6.9,7.5))
plt.subplots_adjust(left=0.09, bottom=0.06, right=0.98, top=0.98, wspace=0.10, hspace=0.08)
ax1 = host_subplot(211)
ax1.plot(time6090,NH6090_smo,"r",lw=1.5, linestyle="-",label="NH6090")
ax1.plot(time6090,SH6090_smo,"r",lw=1.5, linestyle=":",label="SH6090")
ax1lim1 = 1996.0
ax1lim2 = 2021.1
ay1lim1 = 0.0
ay1lim2 = 30.0
ax1.set_xlim(ax1lim1,ax1lim2)
ax1.set_ylim(ay1lim1,ay1lim2)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.setp(ax1.get_xticklabels(), visible=False)
#ax1.set_xlabel('Calendar Year',fontsize=12)

ax1.plot([2009.0,2009.0],[0.0,40.0],"gray",lw=1.0,linestyle="dashed")
ax1.plot([0.0,2022.0],[5.0,5.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax1.plot([0.0,2022.0],[15.0,15.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax1.plot([0.0,2022.0],[25.0,25.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax1.grid(alpha=0.5,linestyle=":")
#marker label
ax1.plot([1996.55,1997.60],[ay1lim2-(ay1lim2-ay1lim1)/17.5,ay1lim2-(ay1lim2-ay1lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax1.text(1998.00,ay1lim2-(ay1lim2-ay1lim1)/17.5,"Northern hemisphere",color = "red",fontsize=14.0,va='center',rotation=0.0)
ax1.plot([1996.55,1997.60],[ay1lim2-(ay1lim2-ay1lim1)/7.7,ay1lim2-(ay1lim2-ay1lim1)/7.7],"r",lw=1.5, linestyle=":",label="SH6090")
ax1.text(1998.00,ay1lim2-(ay1lim2-ay1lim1)/7.7,"Southern hemisphere",color = "r",fontsize=14.0,va='center',rotation=0.0)
#ax1.text(2015.0, 27.8, "High-latitude CMEs ", fontsize=10, va='center')
ax1.text(ax1lim2-(ax1lim2-ax1lim1)/3.2,ay1lim2-(ay1lim2-ay1lim1)/15.5, "High-latitude CMEs", fontsize = 14, va='center')


ax2 = host_subplot(212)
ax2.plot(time6090,NL1040_smo,"r",lw=1.5, linestyle="-",label="NL1040")
ax2.plot(time6090,SL1040_sm0,"r",lw=1.5, linestyle=":",label="SL1040")
ax2lim1 = 1996.0
ax2lim2 = 2021.1
ay2lim1 = 0.0
ay2lim2 = 60.0
ax2.set_xlim(ax2lim1,ax2lim2)
ax2.set_ylim(ay2lim1,ay2lim2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.set_xlabel('Calendar Year',fontsize=14)
#ax2.text(1993.8,60.0, " Monthly Distribution of CME Counts ", fontsize=12.0, va='center', rotation=90)
ax2.text(1993.7,ay2lim2+(ay2lim2-ay2lim1)/30, "Monthly Distribution of CME Counts", fontsize = 14, va='center',rotation=90.0)

ax2.plot([0.0,2022.0],[10.0,10.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax2.plot([0.0,2022.0],[30.0,30.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax2.plot([0.0,2022.0],[50.0,50.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
ax2.plot([2009.0,2009.0],[0.0,80.0],"gray",lw=1.0,linestyle="dashed")
ax2.grid(alpha=0.5,linestyle=":")
#marker label
ax2.plot([1996.55,1997.60],[ay2lim2-(ay2lim2-ay2lim1)/17.5,ay2lim2-(ay2lim2-ay2lim1)/17.5],"r",lw=1.5, linestyle="-",label="NH6090")
ax2.text(1998.00,ay2lim2-(ay2lim2-ay2lim1)/17.5,"Northern hemisphere",color = "red",fontsize=14.0,va='center',rotation=0.0)
ax2.plot([1996.55,1997.60],[ay2lim2-(ay2lim2-ay2lim1)/7.7,ay2lim2-(ay2lim2-ay2lim1)/7.7],"r",lw=1.5, linestyle=":",label="SH6090")
ax2.text(1998.00,ay2lim2-(ay2lim2-ay2lim1)/7.7,"Southern hemisphere",color = "r",fontsize=14.0,va='center',rotation=0.0)
#ax2.text(2015.0, 55.5, "Low-latitude CMEs", fontsize=10, va='center')
ax2.text(ax2lim2-(ax2lim2-ax2lim1)/3.3,ay2lim2-(ay2lim2-ay2lim1)/15.5, "Low-latitude CMEs", fontsize = 14, va='center')


plt.savefig('Figure1.eps', format='eps', dpi=1000)
plt.savefig('Figure1.png', format='png', dpi=1000)

plt.show()

