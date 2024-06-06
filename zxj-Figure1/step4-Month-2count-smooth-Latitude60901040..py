from cProfile import label
import matplotlib.pyplot as plt
import pylab
from matplotlib import *
from mpl_toolkits.axes_grid1 import host_subplot#lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
#from astroML.plotting import setup_text_plots
import matplotlib.ticker as ticker
from scipy.signal import savgol_filter
def txtchange(readfile, writefile):
    timeY = [float(l.split()[0]) for l in open(readfile)]
    timeM = [float(l.split()[1]) for l in open(readfile)]
    timeYM = [float(l.split()[2]) for l in open(readfile)]
    N = [float(l.split()[4]) for l in open(readfile)]
    S = [float(l.split()[5]) for l in open(readfile)]
    Nsmooth = savgol_filter(N,13, 1, mode='nearest')
    Ssmooth = savgol_filter(S,13, 1, mode='nearest')

    for i in range(0,len(timeY)):
        writefile.write(str(timeY[i]).center(10)+str(timeM[i]).center(6)+str(timeYM[i]).center(12)+str(N[i]).center(8)+str(S[i]).center(8)+str(round(Nsmooth[i],4)).center(10)+str(round(Ssmooth[i],4)).center(10)+"\n" )

txtchange("./step4-month-2count-Latitude-NHSH6090.txt",open("./step4-Month-2count-smooth-NHSH6090.txt","w"))
txtchange("./step4-month-2count-Latitude-NLSL1040.txt",open("./step4-Month-2count-smooth-NLSL1040.txt","w"))