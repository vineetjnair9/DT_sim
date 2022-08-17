from fwd_kinematics import fwd_kinematics
from numpy.typing import ArrayLike, NDArray
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Visual3D:
    
    def __init__(self) -> None:
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')

    def add_point(self, point: ArrayLike, color: str=None):
        self.ax.scatter(*point, c=color)


