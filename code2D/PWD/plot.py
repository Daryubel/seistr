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

dip = (np.loadtxt(dipFile))
print(dip.shape)
pwd = (np.loadtxt(pwdFile))
print(pwd.shape)

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


plt.show()
