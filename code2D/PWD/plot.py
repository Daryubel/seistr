from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rc('font', family='Times New Roman', size=14)

path = 'PWD/'
# model = 'SLOL'
# model = 'ladder'
model = 'ladderLarge'

dipFile = path+model+'_dip.dat'
pwdFile = path+model+'_PWD.dat'
orgFile = path+model+'_org.dat'

dip = (np.loadtxt(dipFile))
print(dip.shape)
pwd = (np.loadtxt(pwdFile))
print(pwd.shape)
org = (np.loadtxt(orgFile))

# # Get the jet colormap
# cmap = plt.cm.jet

# # Modify the color distribution
# newcolors = cmap(np.linspace(0, 1, 256))
# middle = int(len(newcolors)/2)
# newcolors[:middle, :] *= np.linspace(0, 1, middle)[:, np.newaxis]
# newcolors[middle:, 0] = np.linspace(1, 1, len(newcolors) - middle)
# newcolors[middle:, 1] = np.linspace(0, 1, len(newcolors) - middle)
# newcolors[middle:, 2] = np.linspace(0, 0, len(newcolors) - middle)
# newcmap = colors.LinearSegmentedColormap.from_list('new_jet', newcolors)


plt.figure(1)
plt.imshow(pwd, cmap=cm.gray, aspect='auto')
# plt.title("Trace with PWD")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
plt.colorbar().set_label(r'$E_z \quad (V/m)$')
ax = plt.gca()
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
plt.savefig(path+'r1_PWD_'+model+'_sec.png', dpi=600)

plt.figure(2)
plt.imshow(dip, cmap=cm.jet, aspect='auto')
# plt.title("Dip")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
plt.colorbar().set_label('Dip (Rad)')
ax = plt.gca()
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
plt.savefig(path+'r1_PWD_'+model+'_dip.png', dpi=600)

plt.figure(3)
plt.imshow(org, cmap=cm.gray, aspect='auto')
# plt.title("Original Trace")
plt.xlabel('Trace Number')
plt.ylabel('Time (ns)')
plt.colorbar().set_label(r'$E_z \quad (V/m)$')
ax = plt.gca()
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
# plt.savefig(path+'r1_PWD_'+model+'_org.png', dpi=600)

plt.show()
