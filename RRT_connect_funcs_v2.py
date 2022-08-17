from ntpath import join
from anytree import Node, RenderTree, search
from anytree.exporter import DictExporter
import numpy as np
import math
from sklearn.neighbors import NearestNeighbors
from pylib import Communication
com = Communication()

def random_config(dof):
    rng = np.random.default_rng(seed=42)
    return rng.uniform(low=-math.pi,high=math.pi,size=dof)

def build_RRT(q_init,params):
    K = params.K # no. of iterations
    eps = params.eps
    dof = params.dof

    # Create list to show parent nodes of each node/vertex
    RRT = []
    joints = []

    # Starting point
    num_nodes = 1
    joints[0] = q_init
    RRT[0] = [0]

    for k in range(K):
        q_rand = random_config(dof)
        status, RRT, joints, num_nodes = extend_RRT(q_rand,RRT,joints,num_nodes,eps)

def extend_RRT(q,RRT,joints,num_nodes,eps):
    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(joints)
    q_near_index = neigh.kneighbors(q,return_distance=False)
    q_near = joints[q_near_index]
    q_new = q_near + eps * (q - q_near)
 
    # Status codes: Reached = 0, Advanced = 1, Trapped = 2
    if com.hasCollision(q_new):
        print('Trapped')
        status = 2

    else: # Add new node to tree
        joints[num_nodes] = q_new

        # Record parent node of newly added vertex
        RRT.append(q_near_index)

        num_nodes = num_nodes + 1

        if q_new == q:
            print('Reached')
            status = 0
        else: 
            print('Advanced')
            status = 1

    return status, RRT, joints, num_nodes

        



