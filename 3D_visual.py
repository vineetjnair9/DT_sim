from fwd_kinematics import fwd_kinematics
from numpy.typing import ArrayLike, NDArray
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Visual3D:
    
    def __init__(self) -> None:
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.ax.autoscale()
        self.ax.set_title("RRT-connect path visualisation")
        self.free_point = self.ax.scatter([], [], c='blue')
        self.nonfree_point = self.ax.scatter([], [], c='red')
        self.ax.legend(['Free', 'colliding'])
        


    def plot_free(self, joint_pose: ArrayLike):
        point3D = fwd_kinematics(joint_pose)
        self.ax.scatter(*point3D)
        plt.show()
    
    def plot_colliding(self, joint_pose: ArrayLike):
        point3D = fwd_kinematics(joint_pose)
        self.free_point.set_data(*point3D)
        plt.show()



if __name__=="__main__":
    fig = Visual3D()
    pose = [0]*6
    fig.plot_free(pose)


