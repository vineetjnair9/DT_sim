from visual_3d import Visual3D
import numpy as np
from numpy import genfromtxt

def Read_txt():
    my_data = genfromtxt('poses.txt', delimiter=' ')
    return my_data

if __name__=="__main__":
    fig = Visual3D()
    data=Read_txt()
    fig.DrawPath(data,)


    