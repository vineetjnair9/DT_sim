# from time import time
# from fwd_kinematics import fwd_kinematics
# from numpy.typing import ArrayLike, NDArray
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
# from mpl_toolkits.mplot3d import Axes3D

# class Visual3D:
    
#     def __init__(self) -> None:
#         # self._fig = plt.figure()
#         # self._ax = plt.axes(projection='3d')
#         # self._ax.autoscale()
#         # self._ax.set_title("RRT-connect path visualisation")
#         # self._free_point = self._ax.scatter([], [], c='blue')
#         # self._nonfree_point = self._ax.scatter([], [], c='red')
#         # self._ax.legend(['Free', 'colliding'])
#         self.fig = plt.figure()
#         self.ax = Axes3D(self.fig)
        


#     def plot_free(self,point):
#         self.ax.scatter(point[0],point[1],point[2],marker='o',s=20,c='b')
        
#         # point3D = fwd_kinematics(joint_pose)
#         # self._ax.scatter(*point3D)
#         # self._ax.clf()
#         # self._ax.show()
#         # time.sleep(0.5)
        
        
#     def show(self):
#         plt.show()
    
#     def plot_colliding(self,point):
#         self.ax.scatter(point[0],point[1],point[2],marker='o',s=20,c='r')

#     def DrawPath(self,path):
#         for i in range(len(path)):
#             if path[i][0]==0:
#                 self.plot_free(path[i][1])
#             else:
#                 self.plot_colliding(path[i][1])

#         plt.show()



# # if __name__=="__main__":
# #     fig = Visual3D()
# #     pose = [0]*6
# #     fig.plot_free(pose)
import imp
from time import time
from fwd_kinematics import fwd_kinematics
from numpy.typing import ArrayLike, NDArray
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D



class Visual3D:
    
    def __init__(self) -> None:
        # self._fig = plt.figure()
        # self._ax = plt.axes(projection='3d')
        # self._ax.autoscale()
        # self._ax.set_title("RRT-connect path visualisation")
        # self._free_point = self._ax.scatter([], [], c='blue')
        # self._nonfree_point = self._ax.scatter([], [], c='red')
        # self._ax.legend(['Free', 'colliding'])
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
        


    def plot_free(self,point):
        
        self.ax.scatter(point[0],point[1],point[2],marker='o',s=20,c='b')
        
        # point3D = fwd_kinematics(joint_pose)
        # self._ax.scatter(*point3D)
        # self._ax.clf()
        # self._ax.show()
        # time.sleep(0.5)
        
    def draw_point(self,row,diff):
        if row[6]==0:
            iscollision=1
        else:
            iscollision=0
        
        # red = [255 0 0]
        #blue= [0 0 255]
        
        color=[255*row[6]/diff,0,255*(diff-row[6])/diff]
        cart_point=fwd_kinematics(row[0],row[1],row[2],row[3],row[4],row[5])
        self.ax.scatter(cart_point[0],cart_point[1],cart_point[2],marker='o',c=color)



    def show(self):
        plt.show()
    
    def plot_colliding(self,point):
        self.ax.scatter(point[0],point[1],point[2],marker='o',s=20,c='r')

    def DrawPath(self,path):
        max=np.argmax(path[:,6])
        min=np.argmin(path[:,6])
        diff=max-min

        for i in range(len(path)):
            self.draw_point(path[i,:],diff)
        plt.show()



# if __name__=="__main__":
#     fig = Visual3D()
#     pose = [0]*6
#     fig.plot_free(pose)

