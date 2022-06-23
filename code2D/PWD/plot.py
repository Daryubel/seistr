# read PWDF.dat and imshow it


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rc('font', family='Times New Roman', size=14)

path = 'PWD/'
# model = 'SLMO'
model = 'ladder'

dipFile = path+'dip_'+model+'.dat'
orgFile = path+'org_'+model+'.dat'


dip = (np.loadtxt(dipFile))
print(dip.shape)
sec = np.transpose((np.loadtxt(orgFile)))
print(sec.shape)

plt.figure(1, figsize=(10,6))
plt.subplot(1, 3, 1)
plt.imshow(sec, cmap=cm.gray)
# plt.title("Original Trace")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
# plt.colorbar().set_label(r'$E_z \quad (V/m)$')


threshold = 1
for i in range(len(dip[0])):
    for j in range(len(dip[1])):
        if dip[i][j] < threshold:
            sec[i][j] = 0


# plot original trace and secTemp trace
plt.subplot(1, 3, 2)
plt.imshow(dip, cmap=cm.seismic)
# plt.title("Dip")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
# plt.colorbar().set_label('Dip (Rad)')
plt.subplot(1, 3, 3)
plt.imshow(sec, cmap=cm.gray)
# plt.title("Trace with PWD")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
# plt.colorbar().set_label(r'$E_z \quad (V/m)$')
plt.savefig(path+'PWD_'+model+'.png', dpi=600)

plt.figure(2)
plt.imshow(sec, cmap=cm.gray, aspect='auto')
# plt.title("Trace with PWD")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
plt.colorbar().set_label(r'$E_z \quad (V/m)$')
plt.savefig(path+'PWD_'+model+'_sec.png', dpi=600)

plt.figure(3)
plt.imshow(dip, cmap=cm.seismic, aspect='auto')
# plt.title("Dip")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
plt.colorbar().set_label('Dip (Rad)')
plt.savefig(path+'PWD_'+model+'_dip.png', dpi=600)


plt.show()
