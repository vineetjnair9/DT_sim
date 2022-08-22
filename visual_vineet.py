import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

eps = [0.1, 0.05, 0.01]
times = [, 2.9117011507352193, 0.4922470927238464, 15.267076067129771]
times_s = [t * 60.0 for t in times]

plt.plot(eps,times_s.)
plt.xlabel('Epsilon')
plt.ylabel('Time [s]')
plt.show()