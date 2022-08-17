import numpy as np
import math
from sklearn.neighbors import NearestNeighbors
from pylib import Communication
com = Communication()

def random_config(dof):
    rng = np.random.default_rng(seed=42)
    return rng.uniform(low=-math.pi,high=math.pi,size=dof)

def build_RRT(q_init):
    # Returns 2 outputs
    # RRT = list showing parent node of each node/vertex in tree
    # joints = joint angles/configurations of each node in tree
    
    # Hyperparameters
    K = 100 # no. of iterations
    eps = 0.01
    dof = 6

    # Create list to show parent nodes of each node/vertex
    RRT = []
    joints = []

    # Starting point (root node)
    num_nodes = 1
    joints[0] = q_init
    RRT[0] = 0 # parent of root is itself

    for k in range(K):
        q_rand = random_config(dof)
        status, RRT, joints = extend_RRT(q_rand,RRT,joints,num_nodes,eps)
    
    return RRT, joints

def extend_RRT(q,RRT,joints,eps):
    # Returns 3 outputs
    # status = 0 (Reached), 1 (Advanced) or 2 (Trapped)
    # RRT = list showing parent node of each node/vertex in tree
    # joints = joint angles/configurations of each node in tree

    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(joints)
    q_near_index = neigh.kneighbors(q,return_distance=False)
    q_near = joints[q_near_index]
    q_new = q_near + eps * (q - q_near)
 
    # Status codes: 
    if com.hasCollision(q_new):
        print('Trapped')
        status = 2

    else: # Add new node to tree
        joints.append = q_new

        # Record parent node of newly added vertex
        RRT.append(q_near_index)

        if q_new == q:
            print('Reached')
            status = 0
        else: 
            print('Advanced')
            status = 1

    return status, RRT, joints

