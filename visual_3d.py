from fwd_kinematics import fwd_kinematics
from numpy.typing import ArrayLike, NDArray
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Visual3D:
    
    def __init__(self) -> None:
        self._fig = plt.figure()
        self._ax = plt.axes(projection='3d')
        self._ax.autoscale()
        self._ax.set_title("RRT-connect path visualisation")
        self._free_point = self._ax.scatter([], [], c='blue')
        self._nonfree_point = self._ax.scatter([], [], c='red')
        self._ax.legend(['Free', 'colliding'])
        


    def plot_free(self, joint_pose: ArrayLike):
        point3D = fwd_kinematics(joint_pose)
        self._ax.scatter(*point3D)
        plt.show()
    
    def plot_colliding(self, joint_pose: ArrayLike):
        point3D = fwd_kinematics(joint_pose)
        self._free_point.set_data(*point3D)
        plt.show()



if __name__=="__main__":
    fig = Visual3D()
    pose = [0]*6
    fig.plot_free(pose)


