from cProfile import label
import matplotlib.pyplot as plt
import pylab
from matplotlib import *
from mpl_toolkits.axes_grid1 import host_subplot#lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
#from astroML.plotting import setup_text_plots
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter

def regulartxtchange(readfile, writefile23,writefile24):
    timeY = [float(l.split()[0]) for l in open(readfile)]
    timeM = [float(l.split()[1]) for l in open(readfile)]
    timeYM = [float(l.split()[2]) for l in open(readfile)]
    N = [float(l.split()[4]) for l in open(readfile)]
    S = [float(l.split()[5]) for l in open(readfile)]
    timeY23 = timeY[0:150]
    timeY24 = timeY[150::]
    timeM23 = timeM[0:150]
    timeM24 = timeM[150::]
    timeYM23 = timeYM[0:150]
    timeYM24 = timeYM[150::]
    N23 = N[0:150]
    N24 = N[150::]
    S23 = S[0:150]
    S24 = S[150::]
#    Nsmooth = savgol_filter(N,13, 1, mode='nearest')
#    Ssmooth = savgol_filter(S,13, 1, mode='nearest')

    for i in range(0,len(timeY23)):
        writefile23.write(str(timeY23[i]).center(10)+str(timeM23[i]).center(8)+str(timeYM23[i]).center(12)+str(N23[i]).center(30)+str(S23[i]).center(30)+"\n" )
    for i in range(0,len(timeY24)):
        writefile24.write(str(timeY24[i]).center(10)+str(timeM24[i]).center(8)+str(timeYM24[i]).center(12)+str(N24[i]).center(30)+str(S24[i]).center(30)+"\n" )

regulartxtchange("./step4-2-regular-Month-2count-Latitude-NHSH6090.txt",open("./step7-1-regular-Month-2count-Latitude-NHSH6090-cy23.txt","w"),open("./step7-2-regular-Month-2count-Latitude-NHSH6090-cy24.txt","w"))
regulartxtchange("./step4-2-regular-Month-2count-Latitude-NLSL1040.txt",open("./step7-1-regular-Month-2count-Latitude-NLSL1040-cy23.txt","w"),open("./step7-2-regular-Month-2count-Latitude-NLSL1040-cy24.txt","w"))

def specifictxtchange(readfile, writefile23,writefile24):
    timeY = [float(l.split()[0]) for l in open(readfile)]
    timeM = [float(l.split()[1]) for l in open(readfile)]
    timeYM = [float(l.split()[2]) for l in open(readfile)]
    N = [float(l.split()[4]) for l in open(readfile)]
    S = [float(l.split()[5]) for l in open(readfile)]
    timeY23 = timeY[0:151]
    timeY24 = timeY[151::]
    timeM23 = timeM[0:151]
    timeM24 = timeM[151::]
    timeYM23 = timeYM[0:151]
    timeYM24 = timeYM[151::]
    N23 = N[0:151]
    N24 = N[151::]
    S23 = S[0:151]
    S24 = S[151::]
#    Nsmooth = savgol_filter(N,13, 1, mode='nearest')
#    Ssmooth = savgol_filter(S,13, 1, mode='nearest')

    for i in range(0,len(timeY23)):
        writefile23.write(str(timeY23[i]).center(10)+str(timeM23[i]).center(8)+str(timeYM23[i]).center(12)+str(N23[i]).center(30)+str(S23[i]).center(30)+"\n" )
    for i in range(0,len(timeY24)):
        writefile24.write(str(timeY24[i]).center(10)+str(timeM24[i]).center(8)+str(timeYM24[i]).center(12)+str(N24[i]).center(30)+str(S24[i]).center(30)+"\n" )

specifictxtchange("./step4-2-specific-Month-2count-Latitude-NHSH6090.txt",open("./step7-1-specific-Month-2count-Latitude-NHSH6090-cy23.txt","w"),open("./step7-2-specific-Month-2count-Latitude-NHSH6090-cy24.txt","w"))
specifictxtchange("./step4-2-specific-Month-2count-Latitude-NLSL1040.txt",open("./step7-1-specific-Month-2count-Latitude-NLSL1040-cy23.txt","w"),open("./step7-2-specific-Month-2count-Latitude-NLSL1040-cy24.txt","w"))