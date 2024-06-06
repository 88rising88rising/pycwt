import numpy as np

#转维度

date = [str(l.split()[0]) for l in open("119.txt")]
cpa = [str(l.split()[2]) for l in open("119.txt")]
width = [str(l.split()[3]) for l in open("119.txt")]
remarks = [str(l.split()[12::]) for l in open("119.txt")]
date_d = np.array(date)
cap_d = np.array(cpa)
width_d = np.array(width)
remarks_d = np.array(remarks)

#1change to float
float_cpa_all = []
for num in cpa:
    float_cpa_all.append(float(num))
#2change to latitude    
latitude_all =[]
for num in float_cpa_all :
    if  0 < num < 90 or 90 < num < 180:
        latitude = 90. - num
        latitude_all.append(latitude)
    if 180 < num < 270 or 270 < num <360:
        latitude = num- 270.
        latitude_all.append(latitude)
    if num == 0.:
        latitude = 90.
        latitude_all.append(latitude)
    if num == 90.:
        latitude = 0.
        latitude_all.append(latitude)
    if num == 180.:
        latitude= -90.
        latitude_all.append(latitude)
    if num == 270.:
        latitude = 0.
        latitude_all.append(latitude)

write_fil= open("119_latitude.txt",'w')
write_fil_high = open("119_latitude_high.txt",'w')
write_fil_low= open("119_latitude_low.txt",'w')
for i in range(0,len(date_d)):
    write_fil.write(str(date_d[i]).center(8)+" "+str(cap_d[i]).center(8)+" "+str(width_d[i]).center(8)+" "+str(latitude_all[i]).center(8)+" "+str(remarks_d[i]).center(20)+" "+'\n')
    if latitude_all[i] >= -40 and latitude_all[i] <= 40:
        write_fil_low.write(str(date_d[i]).center(8)+" "+str(cap_d[i]).center(8)+" "+str(width_d[i]).center(8)+" "+str(latitude_all[i]).center(8)+" "+str(remarks_d[i]).center(20)+" "+'\n')
    if 60 <= latitude_all[i] <= 90 or -90 <= latitude_all[i] <= -60:
        write_fil_high.write(str(date_d[i]).center(8)+" "+str(cap_d[i]).center(8)+" "+str(width_d[i]).center(8)+" "+str(latitude_all[i]).center(8)+" "+str(remarks_d[i]).center(20)+" "+'\n')
