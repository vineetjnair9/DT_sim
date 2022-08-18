from dataclasses import dataclass
from enum import Enum
from typing import List
import numpy as np
from numpy.typing import NDArray, ArrayLike
from pylib import Communication
from visual_3d import Visual3D
#com = Communication()

fig = Visual3D()

@dataclass
class Node:
    pose: NDArray
    parent_idx: int = None

class State(Enum):
    reached = 0
    advanced = 1
    trapped = 2

RRT = List[Node]

def random_config(dim: int):
    return (2*np.pi)*np.random.rand(dim)

def nearest_neighbour(pose: NDArray, tree: RRT) -> int:
    
    min_dist = np.inf
    for i, node in enumerate(tree):
        dist = np.linalg.norm(node.pose-pose)
        
        if dist<min_dist:
            min_dist = dist
            min_idx = i

    return min_idx
    

def new_config(q: NDArray, q_near: NDArray, eps) -> int:

    if False: #com.hasCollision(q.tolist()): #TODO switch this back after testing
        return State.trapped
    
    dist = np.linalg.norm(q-q_near)
    if dist<eps:
        return State.reached
    
    else:
        return State.advanced 

def extend(tree: RRT, q_rand: NDArray, eps=0.01) -> State:
    
    near_idx = nearest_neighbour(q_rand, tree)
    state = new_config(q_rand, tree[near_idx].pose, eps)

    if state == State.reached:
        tree.append(Node(q_rand, near_idx))
        fig.plot_free(q_rand)
        return State.reached

    elif state == State.advanced:
        diff = q_rand - tree[near_idx].pose
        unit_dir = (diff)/np.linalg.norm(diff)
        advanced_pose = tree[near_idx].pose + eps*unit_dir
        tree.append(Node(advanced_pose, near_idx))
        fig.plot_free(advanced_pose)
        return State.advanced
    
    return State.trapped

def connect(tree: RRT, q: NDArray) -> State:
    S = extend(tree, q)
    while S == State.advanced:
        S = extend(tree, q)
    return S

def get_path(T_init: RRT, T_goal: RRT):
    poses= []
    current_node = T_goal[-1]
    
    # construct the path from connecting node to goal node
    while current_node.parent_idx != None:
        poses.append(current_node.pose)
        current_node = T_goal[current_node.parent_idx]

    # add the path from connecting node to init node to front of path
    current_node = T_init[-2]  #-2 to not count the connecting node again
    while current_node.parent_idx != None:
        poses.insert(0, current_node.pose)
        current_node = T_init[current_node.parent_idx]

    return poses



def RRT_connect_planner(q_init: NDArray, q_goal: NDArray, max_iter: int=1000) -> List[float]:

    T_a = [Node(q_init)]
    T_b = [Node(q_goal)]
    ndof = 6
    
    for _ in range(max_iter):
        q_rand = random_config(ndof)
        
        if not extend(T_a, q_rand) == State.trapped:
            if connect(T_b, T_a[-1].pose) == State.reached:                  
                if not np.array_equal(T_a[0].pose, q_init):
                    if not np.array_equal(T_b[0].pose, q_init):
                        raise ValueError  # for debugging, something is wrong in this case
                    T_a, T_b = T_b, T_a  # swap trees, so we pass in the right order to get_path()
                fig.show()
                return get_path(T_a, T_b)
        
        T_a, T_b = T_b, T_a  # swap the roles of the trees
    fig.show()
    print("algorithm failed")
    return 

    


if __name__ == '__main__':
   q_init = np.zeros(6)
   q_goal = np.ones(6)*np.pi
   print(RRT_connect_planner(q_init, q_goal))
   #com._mainLoop(RRT_connect_planner)
