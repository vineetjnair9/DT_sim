# from visual_3d import Visual3D
# import numpy as np
# from numpy import genfromtxt

# def Read_txt():
#     my_data = genfromtxt('poses.txt', delimiter=' ')
#     return my_data

# if __name__=="__main__":
#     fig = Visual3D()
#     data=Read_txt()
#     fig.DrawPath(data)
#     print("done")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
from fwd_kinematics import fwd_kinematics

def Read_txt():
    my_data = genfromtxt('poses.txt', delimiter=' ')
    return my_data

def Get_cart(data):
    carts=[]
    for i in range(len(data)):
        row=data[i,:]
        cart=fwd_kinematics([row[0],row[1],row[2],row[3],row[4],row[5]])
        carts.append(cart)

    return np.array(carts)

if __name__=="__main__":

    data=Read_txt()
    
    carts=Get_cart(data)
    start=carts[0,:]
    stop=carts[-1,:]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = carts[:,0]
    y = carts[:,1]
    z = carts[:,2]
    c = data[:,6]

    img = ax.scatter(x, y, z, c=c, cmap=plt.viridis())
    ax.scatter(start[0],start[1],start[2],marker='x',s=80,c="red")
    ax.scatter(stop[0],stop[1],stop[2],marker='*',s=80,c="red")

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    cbar=fig.colorbar(img)
    cbar.set_label('Clearance [m]')

    plt.show()
    print("done")
    