import numpy as np
from numpy.typing import ArrayLike, NDArray

def fwd_kinematics(pose: ArrayLike) -> NDArray:
    """From a given joint pose, calculate the cartesian end effector position as seen from the base frame

    Args:
        pose (ArrayLike): Joint pose

    Returns:
        NDArray: Cartesian end effector position as seen from base frame
    """

    def T(theta, a, d, alpha):
        return np.array([
            [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), np.cos(theta)*a],
            [np.sin(theta), np.cos(theta)*np.cos(alpha), - np.cos(theta)*np.sin(alpha), np.sin(theta)*a],
            [0, np.sin(alpha), np.cos(alpha), d],
            [0, 0, 0, 1]])
 
    
    a = np.array([0, -0.425, -0.3922, 0, 0, 0])
    d = np.array([0.1625, 0, 0, 0.1333, 0.0997, 0.0996])
    alpha = np.array([np.pi/2, 0, 0, np.pi/2, -np.pi/2, 0])
    loc_ep_pos = np.array([0, 0, 0, 1])  # position of end effector is at the position of it cs
    T1=T(pose[0],a[0],d[0],alpha[0])
    T2=T(pose[1],a[1],d[1],alpha[1])
    T3=T(pose[2],a[2],d[2],alpha[2])
    T4=T(pose[3],a[3],d[3],alpha[3])
    T5=T(pose[4],a[4],d[4],alpha[4])
    T6=T(pose[5],a[5],d[5],alpha[5])
    Tt=T1@T2@T3@T4@T5@T6
    return Tt[0:3,-1]

if __name__=="__main__":
    print(fwd_kinematics([0.523598776,-0.523598776,1.047197551 ,0,0,0]))