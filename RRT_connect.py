import numpy as np
import math
from sklearn.neighbors import NearestNeighbors
from pylib import Communication
com = Communication()

# Hyperparameters
K = 5 # no. of iterations
eps = 0.01
dof = 6

def random_config(dof):
    rng = np.random.default_rng(seed=42)
    return rng.uniform(low=-math.pi,high=math.pi,size=dof)

def build_RRT(q_init):
    # Returns 2 outputs
    # RRT = list showing parent node of each node/vertex in tree
    # joints = joint angles/configurations of each node in tree

    # Create list to show parent nodes of each node/vertex
    RRT = []
    joints = []

    # Starting point (root node)
    joints.append(q_init)
    RRT.append(0) # parent of root is itself

    for k in range(K):
        q_rand = random_config(dof)
        status, RRT, joints, q_new = extend_RRT(RRT,joints,q_rand)
    
    return RRT, joints

def extend_RRT(RRT,joints,q):
    # Returns 3 outputs
    # status = 0 (Reached), 1 (Advanced) or 2 (Trapped)
    # RRT = list showing parent node of each node/vertex in tree
    # joints = joint angles/configurations of each node in tree

    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(joints)
    q_near_index = neigh.kneighbors(q,return_distance=False)
    q_near = joints[q_near_index]

    if np.norm(q - q_near) < eps:
        q_new = q

         # Status codes: 
        if com.hasCollision(q_new):
            print('Trapped')
            status = 2
        else:
            print('Reached')
            status = 0

            # Add new node to tree
            joints.append(q_new)

            # Record parent node of newly added vertex
            RRT.append(q_near_index)

    else: 
        q_new = q_near + eps * (q - q_near)

         # Status codes: 
        if com.hasCollision(q_new):
            print('Trapped')
            status = 2

        else: # Add new node to tree
            joints.append(q_new)

            # Record parent node of newly added vertex
            RRT.append(q_near_index)

            print('Advanced')
            status = 1

    return status, RRT, joints, q_new

def connect(RRT,q,joints):
    status = 0
    while status != 1:
        status, RRT, joints, q_new = extend_RRT(RRT,joints,q)
    return status, RRT, joints

def RRT_connect_planner(q_init,q_goal):
    RRT_a, joints_a = build_RRT(q_init)
    RRT_b, joints_b = build_RRT(q_goal)

    RRT1 = RRT_a
    RRT2 = RRT_b
    joints1 = joints_a
    joints2 = joints_b

    for k in range(K):
        q_rand = random_config(dof)

        status1, RRT1, joints1, q_new = extend_RRT(RRT1,joints1,q_rand)
        if status1 != 2:
            status2, RRT2, joints2 = connect(RRT2,joints2,q_new)
            if status2 == 0:
                RRT2 = RRT2 + len(RRT1)
                RRT = RRT1 + RRT2
                joints = joints1 + joints2
                return RRT, joints
        RRT2 = RRT1
        joints2 = joints1
    print('Failure')
    return

q_init = [-2.088896595860315, -2.017484530838456, -1.611079074071187, -0.07048029509520992, 0.5640853634948029, -1.093268836863869]
q_goal = [-1.1862522062110772, -1.6803693959628347, -2.2637243080183618, -0.7820281405620721, 1.6033439459250105, 0.38341871361603497]
RRT_connect_planner(q_init,q_goal)