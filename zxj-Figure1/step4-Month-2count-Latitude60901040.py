#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:42:27 2021

"""
import numpy as np

file_new1=open('./step4-Month-2count-Latitude-NHSH6090.txt','w')
file_new2=open('./step4-Month-2count-Latitude-NLSL1040.txt','w')

file=open('./step4-Month-1devide-Latitude.txt','r')
line=file.readline()
print(len(line))

while line:
    NH6090=0
    SH6090=0
    NHSH6090 = 0

    NL1040=0
    SL1040=0
    NLSL1040 = 0

    value=[]
    
    timeY=line.split()[0]
    timeM=line.split()[1]
    timeYM=line.split()[2]
    
    for i in range(4, len(line.split())):
        value.append(float(line.split()[i]))
    sum_n=len(value)
    print(timeYM, sum_n)
    for j in range(len(value)):
        if 60.0 <= value[j]<= 90.0:
            NH6090=NH6090+1
            NHSH6090=NHSH6090+1
        if -90.0 <= value[j]<= -60.0:
            SH6090=SH6090+1
            NHSH6090=NHSH6090+1
        if 10.0 <= value[j] <=40.0:
            NL1040 = NL1040+1
            NLSL1040 =  NLSL1040+1
        if -40.0 <= value[j] <= -10.0 :
            SL1040 =  SL1040+1
            NLSL1040 =  NLSL1040+1

    file_new1.write(str(timeY).center(6)+str(timeM).center(4)+str(timeYM).center(10)+str(len(value)).center(6)+str(NH6090).center(6)+str(SH6090).center(6)+str(NHSH6090).center(6)+"\n")
    file_new2.write(str(timeY).center(6)+str(timeM).center(4)+str(timeYM).center(10)+str(len(value)).center(6)+str(NL1040).center(6)+str(SL1040).center(6)+str(NLSL1040).center(6)+"\n")
    line=file.readline()


