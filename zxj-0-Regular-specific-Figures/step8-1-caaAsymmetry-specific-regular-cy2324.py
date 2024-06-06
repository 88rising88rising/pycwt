#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numpy.core.arrayprint import DatetimeFormat 
    
def caculateASymmetry(readdata,writedata):
    line = readdata.readline()
    while line:
        time_Y=line.split()[0]
        time_M=line.split()[1]
        time_YM = line.split()[2]
        N_data=line.split()[-2]
        S_data=line.split()[-1]
        Aabs=round(float(N_data)-float(S_data),4)
        if (float(N_data)+float(S_data))==0.:
            nor=0.0
        else: 
            nor=round((float(N_data)-float(S_data))/(float(N_data)+float(S_data)),4)
        writedata.write(str(time_Y).center(6)+" "+str(time_M).center(8)+" "+str(time_YM).center(12)+' '+str(N_data).center(15)+' '+str(S_data).center(15)+" "+str(round(Aabs,4)).center(15)+str(nor).center(15)+" "+'\n')
        line = readdata.readline()


caculateASymmetry(open("./step7-1-specific-Month-2caa-NHSH6090-cy23.txt",'r'),open("./step8-1-specific-Month-1-caa-Asymmetry-NHSH-cy23.txt","w"))
caculateASymmetry(open("./step7-1-regular-Month-2caa-NHSH6090-cy23.txt",'r'),open("./step8-1-regular-Month-1-caa-Asymmetry-NHSH-cy23.txt","w"))
caculateASymmetry(open("./step7-1-specific-Month-2caa-NLSL1040-cy23.txt",'r'),open("./step8-1-specific-Month-1-caa-Asymmetry-NLSL-cy23.txt","w"))
caculateASymmetry(open("./step7-1-regular-Month-2caa-NLSL1040-cy23.txt",'r'),open("./step8-1-regular-Month-1-caa-Asymmetry-NLSL-cy23.txt","w"))

caculateASymmetry(open("./step7-2-specific-Month-2caa-NHSH6090-cy24.txt",'r'),open("./step8-2-specific-Month-1-caa-Asymmetry-NHSH-cy24.txt","w"))
caculateASymmetry(open("./step7-2-specific-Month-2caa-NLSL1040-cy24.txt",'r'),open("./step8-2-specific-Month-1-caa-Asymmetry-NLSL-cy24.txt","w"))
caculateASymmetry(open("./step7-2-regular-Month-2caa-NHSH6090-cy24.txt",'r'),open("./step8-2-regular-Month-1-caa-Asymmetry-NHSH-cy24.txt","w"))
caculateASymmetry(open("./step7-2-regular-Month-2caa-NLSL1040-cy24.txt",'r'),open("./step8-2-regular-Month-1-caa-Asymmetry-NLSL-cy24.txt","w"))

