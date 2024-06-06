#!/usr/bin/env python
# coding: utf-8
from cProfile import label
import matplotlib.pyplot as plt
import pylab
from matplotlib import *
from mpl_toolkits.axes_grid1 import host_subplot#lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
#from astroML.plotting import setup_text_plots
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter

def calcaa(readfile, writefile):
    timeY = [float(l.split()[0]) for l in open(readfile)]
    timeM = [float(l.split()[1]) for l in open(readfile)]
    timeYM = [float(l.split()[2]) for l in open(readfile)]
    N = [float(l.split()[-2]) for l in open(readfile)]
    S = [float(l.split()[-1]) for l in open(readfile)]
    Ncaa = []
    Scaa = []
    caaN = 0
    caaS = 0
    for i in range(0,len(timeY)):
        caaN = float(caaN)+float(N[i])
        caaS = float(caaS)+float(S[i])
        Ncaa.append(caaN)
        Scaa.append(caaS)
        writefile.write(str(timeY[i]).center(10)+str(timeM[i]).center(8)+str(timeYM[i]).center(12)+str(N[i]).center(8)+str(S[i]).center(8)+str(Ncaa[i]).center(30)+str(Scaa[i]).center(30)+"\n" )
        i=i+1

calcaa("step7-1-regular-Month-2count-Latitude-NLSL1040-cy23.txt",open("./step7-1-regular-Month-2caa-NLSL1040-cy23.txt","w"))
calcaa("step7-1-specific-Month-2count-Latitude-NLSL1040-cy23.txt",open("./step7-1-specific-Month-2caa-NLSL1040-cy23.txt","w"))
calcaa("step7-1-regular-Month-2count-Latitude-NHSH6090-cy23.txt",open("./step7-1-regular-Month-2caa-NHSH6090-cy23.txt","w"))
calcaa("step7-1-specific-Month-2count-Latitude-NHSH6090-cy23.txt",open("./step7-1-specific-Month-2caa-NHSH6090-cy23.txt","w"))

calcaa("step7-2-regular-Month-2count-Latitude-NLSL1040-cy24.txt",open("./step7-2-regular-Month-2caa-NLSL1040-cy24.txt","w"))
calcaa("step7-2-specific-Month-2count-Latitude-NLSL1040-cy24.txt",open("./step7-2-specific-Month-2caa-NLSL1040-cy24.txt","w"))
calcaa("step7-2-regular-Month-2count-Latitude-NHSH6090-cy24.txt",open("./step7-2-regular-Month-2caa-NHSH6090-cy24.txt","w"))
calcaa("step7-2-specific-Month-2count-Latitude-NHSH6090-cy24.txt",open("./step7-2-specific-Month-2caa-NHSH6090-cy24.txt","w"))