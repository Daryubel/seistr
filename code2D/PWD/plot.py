# read PWDF.dat and imshow it


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

model = 'SLMO'
# model = 'ladder'

dipFile = 'dip_'+model+'.dat'
orgFile = 'legacy_originalTrace_'+model+'.dat'


dip = np.transpose(np.transpose(np.loadtxt(dipFile)))
sec = np.transpose(np.transpose(np.loadtxt(orgFile)))
secTemp = sec


for i in range(np.size(dip, 0)):
    for j in range(np.size(dip, 1)):
        if dip[i, j] < 1:
            secTemp[i, j] = 0

# plot original trace and secTemp trace
plt.subplot(1, 2, 1)
plt.imshow(sec, cmap=cm.gray)
plt.title("Original Trace")
plt.subplot(1, 2, 2)
plt.imshow(secTemp, cmap=cm.gray)
plt.title("Trace with PWD")
