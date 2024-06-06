#regular0specific-Figure6
from cProfile import label
import matplotlib.pyplot as plt
import pylab
from matplotlib import *
from mpl_toolkits.axes_grid1 import host_subplot#lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
#from astroML.plotting import setup_text_plots
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter
time6090Ypv = [float(l.split()[0]) for l in open("step4-2-specific-Month-2count-Latitude-NHSH6090.txt")]
time6090Mpv = [float(l.split()[1]) for l in open("step4-2-specific-Month-2count-Latitude-NHSH6090.txt")]
time6090pv = [float(l.split()[2]) for l in open("step4-2-specific-Month-2count-Latitude-NHSH6090.txt")]
NH6090pv = [float(l.split()[4]) for l in open("step4-2-specific-Month-2count-Latitude-NHSH6090.txt")]
SH6090pv = [float(l.split()[5]) for l in open("step4-2-specific-Month-2count-Latitude-NHSH6090.txt")]

time1040Ypv = [float(l.split()[0]) for l in open("step4-2-specific-Month-2count-Latitude-NLSL1040.txt")]
time1040Mpv = [float(l.split()[1]) for l in open("step4-2-specific-Month-2count-Latitude-NLSL1040.txt")]
time1040pv = [float(l.split()[2]) for l in open("step4-2-specific-Month-2count-Latitude-NLSL1040.txt")]
NL1040pv = [float(l.split()[4]) for l in open("step4-2-specific-Month-2count-Latitude-NLSL1040.txt")]
SL1040pv = [float(l.split()[5]) for l in open("step4-2-specific-Month-2count-Latitude-NLSL1040.txt")]

time6090Yexpv = [float(l.split()[0]) for l in open("step4-2-regular-Month-2count-Latitude-NHSH6090.txt")]
time6090Mexpv = [float(l.split()[1]) for l in open("step4-2-regular-Month-2count-Latitude-NHSH6090.txt")]
time6090expv = [float(l.split()[2]) for l in open("step4-2-regular-Month-2count-Latitude-NHSH6090.txt")]
NH6090expv = [float(l.split()[4]) for l in open("step4-2-regular-Month-2count-Latitude-NHSH6090.txt")]
SH6090expv = [float(l.split()[5]) for l in open("step4-2-regular-Month-2count-Latitude-NHSH6090.txt")]

time1040Yexpv = [float(l.split()[0]) for l in open("step4-2-regular-Month-2count-Latitude-NLSL1040.txt")]
time1040Mexpv = [float(l.split()[1]) for l in open("step4-2-regular-Month-2count-Latitude-NLSL1040.txt")]
time1040expv = [float(l.split()[2]) for l in open("step4-2-regular-Month-2count-Latitude-NLSL1040.txt")]
NL1040expv = [float(l.split()[4]) for l in open("step4-2-regular-Month-2count-Latitude-NLSL1040.txt")]
SL1040expv = [float(l.split()[5]) for l in open("step4-2-regular-Month-2count-Latitude-NLSL1040.txt")]
#SLS1040 = [float(l.split()[-1]) for l in open("step4-Month-2count-smooth-NLSL1040.txt")]
print("\n")
print("北半球的同比变化:")
time6090Ypvcy23 = time6090Ypv[0:151]
time6090Ypvcy24 = time6090Ypv[151::]
time6090Mpvcy23 = time6090Mpv[0:151]
time6090Mpvcy24 = time6090Mpv[151::]
NH6090pvcy23 = NH6090pv[0:151]
NH6090pvcy24 = NH6090pv[151::]
print("23高北半球起止:",time6090Ypvcy23[0],time6090Mpvcy23[0],"--",time6090Ypvcy23[-1],time6090Mpvcy23[-1])
print("24高北半球起止:",time6090Ypvcy24[0],time6090Mpvcy24[0],"--",time6090Ypvcy24[-1],time6090Mpvcy24[-1])
print("23高北半球specific数量",sum(NH6090pvcy23),"24高北半球specific数量",sum(NH6090pvcy24))
print("高北半球Specific同比变化:","(sum(NH6090pvcy24)-sum(NH6090pvcy23))/sum(NH6090pvcy23)*100=",round((sum(NH6090pvcy24)-sum(NH6090pvcy23))/sum(NH6090pvcy23)*100,4),"%")

time1040Ypvcy23 = time1040Ypv[0:151]
time1040Ypvcy24 = time1040Ypv[151::]
time1040Mpvcy23 = time1040Mpv[0:151]
time1040Mpvcy24 = time1040Mpv[151::]
NL1040pvcy23 = NL1040pv[0:151]
NL1040pvcy24 = NL1040pv[151::]
print("23高北半球起止:",time1040Ypvcy23[0],time1040Mpvcy23[0],"--",time1040Ypvcy23[-1],time1040Mpvcy23[-1])
print("24高北半球起止:",time1040Ypvcy24[0],time1040Mpvcy24[0],"--",time1040Ypvcy24[-1],time1040Mpvcy24[-1])
print("23低北半球specific数量",sum(NL1040pvcy23),"24低北半球specific数量",sum(NL1040pvcy24))
print("高北半球Specific同比变化:","(sum(NL1040pvcy24)-sum(NL1040pvcy23))/sum(NL1040pvcy23)*100=",round((sum(NL1040pvcy24)-sum(NL1040pvcy23))/sum(NL1040pvcy23)*100,4),"%")

time6090Yexpvcy23 = time6090Yexpv[0:150]
time6090Yexpvcy24 = time6090Yexpv[150::]
time6090Mexpvcy23 = time6090Mexpv[0:150]
time6090Mexpvcy24 = time6090Mexpv[10::]
NH6090expvcy23 = NH6090expv[0:150]
NH6090expvcy24 = NH6090expv[150::]
print("23高北半球起止:",time6090Yexpvcy23[0],time6090Mexpvcy23[0],"--",time6090Yexpvcy23[-1],time6090Mexpvcy23[-1])
print("24高北半球起止:",time6090Yexpvcy24[0],time6090Mexpvcy24[0],"--",time6090Yexpvcy24[-1],time6090Mexpvcy24[-1])
print("23高北半球regular数量",sum(NH6090expvcy23),"24高北半球regular数量",sum(NH6090expvcy24))
print("高北半球regular同比变化:","(sum(NH6090expvcy24)-sum(NH6090expvcy23))/sum(NH6090expvcy23)*100=",round((sum(NH6090expvcy24)-sum(NH6090expvcy23))/sum(NH6090expvcy23)*100,4),"%")

time1040Yexpvcy23 = time1040Yexpv[0:150]
time1040Yexpvcy24 = time1040Yexpv[150::]
time1040Mexpvcy23 = time1040Mexpv[0:150]
time1040Mexpvcy24 = time1040Mexpv[150::]
NL1040expvcy23 = NL1040expv[0:150]
NL1040expvcy24 = NL1040expv[150::]
print("23高北半球起止:",time1040Yexpvcy23[0],time1040Mexpvcy23[0],"--",time1040Yexpvcy23[-1],time1040Mexpvcy23[-1])
print("24高北半球起止:",time1040Yexpvcy24[0],time1040Mexpvcy24[0],"--",time1040Yexpvcy24[-1],time1040Mexpvcy24[-1])
print("23低北半球regular数量",sum(NL1040expvcy23),"24低北半球regular数量",sum(NL1040expvcy24))
print("低北半球regular同比变化:","(sum(NL1040expvcy24)-sum(NL1040expvcy23))/sum(NL1040expvcy23)*100=",round((sum(NL1040expvcy24)-sum(NL1040expvcy23))/sum(NL1040expvcy23)*100,4),"%")
print("\n")
print("南半球的同比变化:")
time6090Ypvcy23 = time6090Ypv[0:151]
time6090Ypvcy24 = time6090Ypv[151::]
time6090Mpvcy23 = time6090Mpv[0:151]
time6090Mpvcy24 = time6090Mpv[151::]
SH6090pvcy23 = SH6090pv[0:151]
SH6090pvcy24 = SH6090pv[151::]
print("23高纬度南半球起止:",time6090Ypvcy23[0],time6090Mpvcy23[0],"--",time6090Ypvcy23[-1],time6090Mpvcy23[-1])
print("24高纬度南半球起止:",time6090Ypvcy24[0],time6090Mpvcy24[0],"--",time6090Ypvcy24[-1],time6090Mpvcy24[-1])
print("23高纬度南半球specific数量",sum(SH6090pvcy23),"24高纬度南半球specific数量",sum(SH6090pvcy24))
print("高纬度南半球Specific同比变化:","(sum(SH6090pvcy24)-sum(SH6090pvcy23))/sum(SH6090pvcy23)*100=",round((sum(SH6090pvcy24)-sum(SH6090pvcy23))/sum(SH6090pvcy23)*100,4),"%")

time1040Ypvcy23 = time1040Ypv[0:151]
time1040Ypvcy24 = time1040Ypv[151::]
time1040Mpvcy23 = time1040Mpv[0:151]
time1040Mpvcy24 = time1040Mpv[151::]
SL1040pvcy23 = SL1040pv[0:151]
SL1040pvcy24 = SL1040pv[151::]
print("23高纬度南半球起止:",time1040Ypvcy23[0],time1040Mpvcy23[0],"--",time1040Ypvcy23[-1],time1040Mpvcy23[-1])
print("24高纬度南半球起止:",time1040Ypvcy24[0],time1040Mpvcy24[0],"--",time1040Ypvcy24[-1],time1040Mpvcy24[-1])
print("23低纬度南半球specific数量",sum(SL1040pvcy23),"24低纬度南半球specific数量",sum(SL1040pvcy24))
print("高纬度南半球Specific同比变化:","(sum(SL1040pvcy24)-sum(SL1040pvcy23))/sum(SL1040pvcy23)*100=",round((sum(SL1040pvcy24)-sum(SL1040pvcy23))/sum(SL1040pvcy23)*100,4),"%")

time6090Yexpvcy23 = time6090Yexpv[0:150]
time6090Yexpvcy24 = time6090Yexpv[150::]
time6090Mexpvcy23 = time6090Mexpv[0:150]
time6090Mexpvcy24 = time6090Mexpv[10::]
SH6090expvcy23 = SH6090expv[0:150]
SH6090expvcy24 = SH6090expv[150::]
print("23高纬度南半球起止:",time6090Yexpvcy23[0],time6090Mexpvcy23[0],"--",time6090Yexpvcy23[-1],time6090Mexpvcy23[-1])
print("24高纬度南半球起止:",time6090Yexpvcy24[0],time6090Mexpvcy24[0],"--",time6090Yexpvcy24[-1],time6090Mexpvcy24[-1])
print("23高纬度南半球regular数量",sum(SH6090expvcy23),"24高纬度南半球regular数量",sum(SH6090expvcy24))
print("高纬度南半球regular同比变化:","(sum(SH6090expvcy24)-sum(SH6090expvcy23))/sum(SH6090expvcy23)*100=",round((sum(SH6090expvcy24)-sum(SH6090expvcy23))/sum(SH6090expvcy23)*100,4),"%")

time1040Yexpvcy23 = time1040Yexpv[0:150]
time1040Yexpvcy24 = time1040Yexpv[150::]
time1040Mexpvcy23 = time1040Mexpv[0:150]
time1040Mexpvcy24 = time1040Mexpv[150::]
SL1040expvcy23 = SL1040expv[0:150]
SL1040expvcy24 = SL1040expv[150::]
print("23高纬度南半球起止:",time1040Yexpvcy23[0],time1040Mexpvcy23[0],"--",time1040Yexpvcy23[-1],time1040Mexpvcy23[-1])
print("24高纬度南半球起止:",time1040Yexpvcy24[0],time1040Mexpvcy24[0],"--",time1040Yexpvcy24[-1],time1040Mexpvcy24[-1])
print("23低纬度南半球regular数量",sum(SL1040expvcy23),"24低纬度南半球regular数量",sum(SL1040expvcy24))
print("低纬度南半球regular同比变化:","(sum(SL1040expvcy24)-sum(SL1040expvcy23))/sum(SL1040expvcy23)*100=",round((sum(SL1040expvcy24)-sum(SL1040expvcy23))/sum(SL1040expvcy23)*100,4),"%")
print("\n")
print("北半球+南半球的同比变化:")
print("23高北半球+南半球起止:",time6090Ypvcy23[0],time6090Mpvcy23[0],"--",time6090Ypvcy23[-1],time6090Mpvcy23[-1])
print("24高北半球+南半球起止:",time6090Ypvcy24[0],time6090Mpvcy24[0],"--",time6090Ypvcy24[-1],time6090Mpvcy24[-1])
print("23高北半球+南半球specific数量",sum(NH6090pvcy23)+sum(SH6090pvcy23),"24高北半球+南半球specific数量",sum(NH6090pvcy24)+sum(SH6090pvcy24))
print("高北半球+南半球Specific同比变化:",round((sum(NH6090pvcy24)+sum(SH6090pvcy24)-sum(NH6090pvcy23)-sum(SH6090pvcy23))/(sum(NH6090pvcy23)+sum(SH6090pvcy23))*100,4),"%")

print("23高北半球+南半球起止:",time1040Ypvcy23[0],time1040Mpvcy23[0],"--",time1040Ypvcy23[-1],time1040Mpvcy23[-1])
print("24高北半球+南半球起止:",time1040Ypvcy24[0],time1040Mpvcy24[0],"--",time1040Ypvcy24[-1],time1040Mpvcy24[-1])
print("23低北半球+南半球specific数量",sum(NL1040pvcy23)+sum(SL1040pvcy23),"24低北半球+南半球specific数量",sum(NL1040pvcy24)+sum(SL1040pvcy24))
print("高北半球+南半球Specific同比变化:",round((sum(NL1040pvcy24)+sum(SL1040pvcy24)-sum(NL1040pvcy23)-sum(SL1040pvcy23))/(sum(NL1040pvcy23)+sum(SL1040pvcy23))*100,4),"%")

print("23高北半球+南半球起止:",time6090Yexpvcy23[0],time6090Mexpvcy23[0],"--",time6090Yexpvcy23[-1],time6090Mexpvcy23[-1])
print("24高北半球+南半球起止:",time6090Yexpvcy24[0],time6090Mexpvcy24[0],"--",time6090Yexpvcy24[-1],time6090Mexpvcy24[-1])
print("23高北半球+南半球regular数量",sum(NH6090expvcy23)+sum(SH6090expvcy23),"24高北半球+南半球regular数量",sum(NH6090expvcy24)+sum(SH6090expvcy24))
print("高北半球+南半球regular同比变化:",round((sum(NH6090expvcy24)+sum(SH6090expvcy24)-sum(NH6090expvcy23)-sum(SH6090expvcy23))/(sum(NH6090expvcy23)+sum(SH6090expvcy23))*100,4),"%")

print("23高北半球+南半球起止:",time1040Yexpvcy23[0],time1040Mexpvcy23[0],"--",time1040Yexpvcy23[-1],time1040Mexpvcy23[-1])
print("24高北半球+南半球起止:",time1040Yexpvcy24[0],time1040Mexpvcy24[0],"--",time1040Yexpvcy24[-1],time1040Mexpvcy24[-1])
print("23低北半球+南半球regular数量",sum(NL1040expvcy23)+sum(SL1040expvcy23),"24低北半球+南半球regular数量",sum(NL1040expvcy24)+sum(SL1040expvcy24))
print("低北半球+南半球regular同比变化:",round((sum(NL1040expvcy24)+sum(SL1040expvcy24)-sum(NL1040expvcy23)-sum(SL1040expvcy23))/(sum(NL1040expvcy23)+sum(SL1040expvcy23))*100,4),"%")



"""

NH6090pv = savgol_filter(NH6090pv,13, 1, mode='nearest')
SH6090pv = savgol_filter(SH6090pv,13, 1, mode='nearest')
NL1040pv = savgol_filter(NL1040pv,13, 1, mode='nearest')
SL1040pv = savgol_filter(SL1040pv,13, 1, mode='nearest')

NH6090expv = savgol_filter(NH6090expv,13, 1, mode='nearest')
SH6090expv = savgol_filter(SH6090expv,13, 1, mode='nearest')
NL1040expv = savgol_filter(NL1040expv,13, 1, mode='nearest')
SL1040expv = savgol_filter(SL1040expv,13, 1, mode='nearest')

fig = plt.figure(figsize =(6.0,5.0))
plt.subplots_adjust(left=0.09, bottom=0.10, right=0.98, top=0.98, wspace=0.10, hspace=0.08)
ax1 = host_subplot(211)
#ax1.set_ylabel('Whole disk')
ax1.plot(time6090pv,NH6090pv,"r",lw=1.5, linestyle="--",label="NH6090pv")
ax1.plot(time6090pv,SH6090pv,"b",lw=1.5, linestyle="--",label="SH6090pv")
ax1.plot(time6090expv,NH6090expv,"r",lw=1.5, linestyle="-",label="NH6090expv")
ax1.plot(time6090expv,SH6090expv,"b",lw=1.5, linestyle="-",label="SH6090expv")
ax1.set_ylim([0.0,30])
ax1.set_xlim([1996.0,2021.0])
ax1.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(2))
plt.setp(ax1.get_xticklabels(), visible=False)
#ax1.plot([0.0,2022.0],[5.0,5.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#ax1.plot([0.0,2022.0],[15.0,15.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#ax1.plot([0.0,2022.0],[25.0,25.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#marker label

ax1.plot([1996.55,1997.70],[28.8,28.8],"r",lw=1.0, linestyle="-",label="NH6090")
ax1.plot([1996.55,1997.70],[28.0,28.0],"r",lw=1.0, linestyle="--",label="NH6090")
ax1.plot([1996.55,1997.70],[26.2,26.2],"b",lw=1.0, linestyle="-",label="SH6090")
ax1.plot([1996.55,1997.70],[25.5,25.5],"b",lw=1.0, linestyle="--",label="SH6090")
ax1.text(1998.00,28.3,"Northern hemisphere",color = "red",fontsize=10.0,va='center',rotation=0.0)
ax1.text(1998.00,25.8,"Southern hemisphere",color = "blue",fontsize=10.0,va='center',rotation=0.0)
ax1.plot([2009.0,2009.0],[0.0,40.0],"gray",lw=1.0,linestyle="dashed")
ax1.plot([2001.90,2001.90],[0.,8000.0],"gray",alpha=0.3,lw=1.0,linestyle="--")
ax1.plot([2014.333,2014.333],[0.0,100.0],"gray",alpha=0.3,lw=1.0,linestyle="--")
ax1.text(2014.5, 28.0, "High-latitude CMEs ", fontsize=10, va='center')
#ax1.grid(alpha=0.5,linestyle=":")

ax2 = host_subplot(212)
#ax2.set_ylabel('Northern hemisphere')
ax2.plot(time1040pv,NL1040pv,"r",lw=1.5, linestyle="--",label="NL1040pv")
ax2.plot(time1040pv,SL1040pv,"b",lw=1.5, linestyle="--",label="SL1040pv")
ax2.plot(time1040expv,NL1040expv,"r",lw=1.5, linestyle="-",label="NL1040expv")
ax2.plot(time1040expv,SL1040expv,"b",lw=1.5, linestyle="-",label="SL1040expv")
ax2.set_xlabel('Calendar Year',fontsize=12)
ax2.text(1993.8,60.0, " Monthly Distribution of CME Counts", fontsize=12.0, va='center', rotation=90)
ax2.set_ylim([0.0,60])
ax2.set_xlim([1996,2021.0])
ax2.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax2.plot([0.0,2022.0],[10.0,10.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#ax2.plot([0.0,2022.0],[30.0,30.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#ax2.plot([0.0,2022.0],[50.0,50.0],"grey",alpha=0.15,lw=1.0,linestyle=":")
#ax2.grid(alpha=0.5,linestyle=":")
#marker label

ax2.plot([1996.55,1997.70],[57.0,57.0],"r",lw=1.0, linestyle="-")
ax2.plot([1996.55,1997.70],[55.5,55.5],"r",lw=1.0, linestyle="--")
ax2.plot([1996.55,1997.70],[52.0,52.0],"b",lw=1.0, linestyle="-")
ax2.plot([1996.55,1997.70],[50.5,50.5],"b",lw=1.0, linestyle="--")
ax2.text(1998.00,56.2,"Northern hemisphere",color = "red",fontsize=10.0,va='center',rotation=0.0)
ax2.text(1998.00,51.0,"Southern hemisphere",color = "blue",fontsize=10.0,va='center',rotation=0.0)
ax2.text(2014.5, 56.3, "Low-latitude CMEs", fontsize=10, va='center')
ax2.plot([2009.0,2009.0],[0.0,80.0],"gray",lw=1.0,linestyle="dashed")
ax2.plot([2001.90,2001.90],[0.,8000.0],"gray",alpha=0.3,lw=1.0,linestyle="--")
ax2.plot([2014.333,2014.333],[0.0,100.0],"gray",alpha=0.3,lw=1.0,linestyle="--")

foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('z-Figure1-regular-specific.eps', format='eps', dpi=1000)
foo_fig.savefig('z-Figure1-regular-specific.png', format='png', dpi=1000)
plt.show()
"""