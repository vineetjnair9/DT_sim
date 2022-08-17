import numpy as np
from numpy.typing import ArrayLike, NDArray

def fwd_kinematics(pose: ArrayLike) -> NDArray:
    """From a given joint pose, calculate the cartesian end effector position as seen from the base frame

    Args:
        pose (ArrayLike): Joint pose

    Returns:
        NDArray: Cartesian end effector position as seen from base frame
    """

    # Calculates the H transformation matrix for D-H parameters
    def T(theta, a, d, alpha):
        return np.array([
            [np.cos(theta), -np.sin(theta), 0, a],
            [np.sin(theta)*np.cos(alpha), np.cos(theta)*np.cos(alpha), - np.sin(alpha), -np.sin(alpha)*d],
            [np.sin(theta)*np.sin(alpha), np.cos(theta)*np.sin(alpha), - np.cos(alpha), -np.cos(alpha)*d],
            [0, 0, 0, 1]])

    theta = np.zeros(6)
    a = np.array([0, -0.24355, -0.2132, 0, 0, 0])
    d = np.array([0.15185, 0, 0, 0.13105, 0.08535, 0.0921])
    alpha = np.array([np.pi/2, 0, 0, np.pi/2, -np.pi/2, 0])
    loc_ep_pos = np.array([0, 0, 0, 1])  # position of end effector is at the position of it cs

    # Transformation matrix from end effector frame to base frame
    T_60 = np.eye(4)
    for i in range(6):
        T_60 = T_60@T(theta[i], a[i], d[i], alpha[i])
    
    return (T_60@loc_ep_pos)[:-1]

if __name__=="__main__":
    print(fwd_kinematics([1.2]*6))
