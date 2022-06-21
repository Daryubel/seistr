# read PWDF.dat and imshow it


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot_pwdf(pwdf_file):
    """
    plot PWDF.dat
    """
    data = np.transpose((np.transpose((np.loadtxt(pwdf_file)))))
    plt.imshow(data, cmap=cm.gray)
    plt.colorbar()
    plt.show()


plot_pwdf('PWDF.dat')