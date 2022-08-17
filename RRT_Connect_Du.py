#!/usr/bin/env python3

from cmath import pi
from math import dist
import random
from turtle import pos
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fw_kinematic import fwd_kinematics

JointValues = List[float]
JointValuesList = List[JointValues]

from pylib import Communication
com = Communication()


class RRT_connect:

    class Node:
        """
        创建节点
        """

        def __init__(self, p):
            self.point=p
            # self.path = [] # 路径，作为画图的数据，也可以理解成保存的边集
            self.parent = None #父节点

    def __init__(self,start,stop,rand_area=None,expand_dis=pi/100, goal_sample_rate=5,max_iter=1000):
        self.start=start
        self.stop=stop
        self.area=rand_area
        self.step=expand_dis
        self.max_iter=max_iter
        self.tree_list_1 = []
        self.tree_list_2 = []
        self.tree_list_1.append(self.Node(start))
        self.tree_list_2.append(self.Node(stop))
    

    def generate_random_point(self):
        # x:-0.664 0.336
        # y:-0.736 0.264
        # z:0.102 0.881
        
        
        seed_1=random.random()
        seed_2=random.random()
        seed_3=random.random()
        seed_4=random.random()
        seed_5=random.random()
        seed_6=random.random()

        rand_1=2*pi*seed_1+(-pi)
        rand_2=2*pi*seed_2+(-pi)
        rand_3=2*pi*seed_3+(-pi)
        rand_4=2*pi*seed_4+(-pi)
        rand_5=2*pi*seed_5+(-pi)
        rand_6=2*pi*seed_6+(-pi)

        rand_point=self.Node([rand_1,rand_2,rand_3,rand_4,rand_5,rand_6])
        
        return rand_point

    def Extend_Tree(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        p1=fwd_kinematics([self.start[0], self.start[1],self.start[2],self.start[3], self.start[4],self.start[5]])
        ax.scatter(p1[0],p1[1],p1[2])
        p2=fwd_kinematics([self.stop[0], self.stop[1],self.stop[2],self.stop[3], self.stop[4],self.stop[5]])
        ax.scatter(p2[0],p2[1],p2[2])
        # plt.show()

        for i in range(self.max_iter):
            rand_point=self.generate_random_point()
            step=self.step
            nearest_point=self.Find_nearest(rand_point.point,self.tree_list_1)
            distance=self.Cal_distance(rand_point.point,nearest_point.point)
            if distance>step:
                
                p_new=self.Generate_point_new(distance,rand_point,nearest_point)

            else:
                p_new=rand_point
            print(p_new)
            print(rand_point.point)
            print(nearest_point.point)

            p_new=self.Node(p_new)
            p_new.parent=nearest_point
            # p_new.path=[p_new.parent.path,p_new.point]
            #check collision
            # mid_p_new=[p_new.point[0]/2,p_new.point[1]/2,p_new.point[2]/2]

            if not self.Check_collision(p_new.point):
                self.tree_list_1.append(p_new)
                nearest_point2=self.Find_nearest(p_new.point,self.tree_list_2)
                distance2=self.Cal_distance(p_new.point,nearest_point2.point)
                if distance2>step:
                    p_new2=self.Generate_point_new2(distance2,p_new,nearest_point2)
                else:
                    p_new2=rand_point
                
                # print()

                p_new2=self.Node(p_new2)
                p_new2.parent=nearest_point2
                # mid_p_new2=[p_new2.point[0]/2,p_new2.point[1]/2,p_new2.point[2]/2]

                if not self.Check_collision(p_new2.point):
                    self.tree_list_2.append(p_new2)

            if self.Check_end():
                break
            
            p3=fwd_kinematics([p_new.point[0], p_new.point[1],p_new.point[2],p_new.point[3], p_new.point[4],p_new.point[5]])
            ax.scatter(p3[0],p3[1],p3[2])
            p4=fwd_kinematics([p_new2.point[0], p_new2.point[1],p_new2.point[2],p_new2.point[3], p_new2.point[4],p_new2.point[5]])
            ax.scatter(p4[0],p4[1],p4[2])
            plt.show()
    
    def Cal_distance(self,p,q):
        # dis=sqrt((p[0]-q[0])**2+(p[1]-q[1])**2+(p[2]-q[2])**2)
        dis=dist(p,q)
        return dis

    def Check_collision(self,p):
        hsCol = com.hasCollision(p)
        clr = com.clearance(p)
        if hsCol==True:
            return True
        else:
            return False

    def Find_nearest(self, p, tree):
        dis_s=[]
        for i in range(len(tree)):
            point_temp=tree[i]
            dis=self.Cal_distance(point_temp.point,p)
            dis_s.append(dis)
        inx=np.argmin(dis_s)

        return tree[inx]

    def Generate_point_new(self,distance,rand_point,nearest_point):
        # print(rand_point.point[0])
        # p_new_1=(self.step/distance)*(rand_point.point[0]-nearest_point.point[0])+nearest_point.point[0]
        # p_new_2=(self.step/distance)*(rand_point.point[1]-nearest_point.point[1])+nearest_point.point[1]
        # p_new_3=(self.step/distance)*(rand_point.point[2]-nearest_point.point[2])+nearest_point.point[2]
        # p_new_4=(self.step/distance)*(rand_point.point[3]-nearest_point.point[3])+nearest_point.point[3]
        # p_new_5=(self.step/distance)*(rand_point.point[4]-nearest_point.point[4])+nearest_point.point[4]
        # p_new_6=(self.step/distance)*(rand_point.point[5]-nearest_point.point[5])+nearest_point.point[5]

        new_point=[]
        for i in range(6):
            value=nearest_point.point[i]+(self.step/distance)*(rand_point.point[i]-nearest_point.point[i])
            new_point.append(value)

        return new_point

        # return [p_new_1,p_new_2,p_new_3,p_new_4,p_new_5,p_new_6]

    def Generate_point_new2(self,distance,rand_point,nearest_point):
        # p_new_1=((distance-self.step)/distance)*(nearest_point.point[0]-rand_point.point[0])+rand_point.point[0]
        # p_new_2=((distance-self.step)/distance)*(nearest_point.point[1]-rand_point.point[1])+rand_point.point[1]
        # p_new_3=((distance-self.step)/distance)*(nearest_point.point[2]-rand_point.point[2])+rand_point.point[2]
        # p_new_4=((distance-self.step)/distance)*(nearest_point.point[3]-rand_point.point[3])+rand_point.point[3]
        # p_new_5=((distance-self.step)/distance)*(nearest_point.point[4]-rand_point.point[4])+rand_point.point[4]
        # p_new_6=((distance-self.step)/distance)*(nearest_point.point[5]-rand_point.point[5])+rand_point.point[5]

        new_point=[]
        for i in range(6):
            value=nearest_point.point[i]+(self.step/distance)*(rand_point.point[i]-nearest_point.point[i])
            new_point.append(value)

        return new_point

    def Check_end(self):
        for i in range(len(self.tree_list_1)):
            for j in range(len(self.tree_list_2)):
                if self.Cal_distance(self.tree_list_1[i].point,self.tree_list_2[j].point)>self.step:
                    continue
                else:
                    return True


def compilePath(start: JointValues, stop: JointValues) -> JointValuesList:

   print('start = ', start)
   print('stop = ', stop)
   if len(start) != 6 or len(stop) != 6:
      print('Array length mismatch')
      return None

   poseList = list()
   poseList.append(start)
   hsCol = com.hasCollision(start)
   clr = com.clearance(start)
   print("start:", "iscollision",hsCol, "clearance", clr)

   poseList.append(stop)
   hsCol = com.hasCollision(stop)
   clr = com.clearance(stop)
   print("stop:", "iscollision", hsCol, "clearance", clr)
   # fill in the poses

   return poseList

   
def DergeeToRadius(degree):
    return degree/180*pi

if __name__ == '__main__':
#    com._mainLoop(compilePath)
    rrt=RRT_connect(start=[-2.194994195566857, -2.204066153002122, -1.782691206638569, -2.296184584257166, -0.2502436962787926, 1.653367853706748],stop=[-2.194994195566857, -1.866362961559723, -1.422051457171162, -2.994527525166973, -0.2502436962787904, 1.653367853706747])
    rrt.Extend_Tree()
