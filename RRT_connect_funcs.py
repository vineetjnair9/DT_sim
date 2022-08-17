from anytree import Node, RenderTree, search
from anytree.exporter import DictExporter
import numpy as np
import math
from sklearn.neighbors import NearestNeighbors
from pylib import Communication
com = Communication()

class node:
  def __init__(self, parent, joint, node_index):
    self.parent = parent
    self.joint = joint
    self.node_index = node_index

def random_config(dof):
    rng = np.random.default_rng(seed=42)
    return rng.uniform(low=-math.pi,high=math.pi,size=dof)

def build_RRT(q_init,params):
    K = params.K # no. of iterations
    eps = params.eps
    dof = params.dof

    nodes = {}

    start = Node('start', joint=q_init, num=0)

    for k in range(K):

def extend_RRT(q,RRT,num_nodes):
    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(RRT)
    q_near_index = neigh.kneighbors(q,return_distance=False)
    q_near = search.find_by_attr(RRT, num=q_near_index)

def new_config(q,q_near,eps,num_nodes,nodes_dict):
    q_new = q_near + eps * (q - q_near)
 
    if com.hasCollision(q_new):
        print('Trapped')
        return

    else:
        if q_new == q:
            print('Reached')
        else: 
            print('Advanced')
        new_node_num = num_nodes + 1
        nodes_dict[new_node_num] = Node('node' + str(new_node_num), parent=q_near, joint=q_new, num=new_node_num)



