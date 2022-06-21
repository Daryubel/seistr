# read PWDF.dat and imshow it


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

path = 'PWD/'
# model = 'SLMO'
model = 'ladder'

dipFile = path+'dip_'+model+'.dat'
orgFile = path+'org_'+model+'.dat'


dip = (np.loadtxt(dipFile))
print(dip.shape)
sec = ((np.loadtxt(orgFile)))
print(sec.shape)

plt.subplot(1, 3, 1)
plt.imshow(sec, cmap=cm.gray)
plt.title("Original Trace")


threshold = 1
for i in range(len(dip[0])):
    for j in range(len(dip[1])):
        if dip[i][j] < threshold:
            sec[i][j] = 0


# plot original trace and secTemp trace
plt.subplot(1, 3, 2)
plt.imshow(dip, cmap=cm.gray)
plt.title("Dip")
plt.subplot(1, 3, 3)
plt.imshow(sec, cmap=cm.gray)
plt.title("Trace with PWD")
plt.show()
