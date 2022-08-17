from dataclasses import dataclass
from enum import Enum
from typing import List
import numpy as np
from numpy.typing import NDArray, ArrayLike
from pylib import Communication
com = Communication()

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
            min_dist = node
            min_idx = i

    return min_idx
    

def new_config(q: NDArray, q_near: NDArray, eps) -> int:

    if com.hasCollision(q.tolist()):
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
        return State.reached

    elif state == State.advanced:
        diff = q_rand - tree[near_idx].pose
        unit_dir = (diff)/np.linalg.norm(diff)
        advanced_pose = tree[near_idx].pose + eps*unit_dir
        tree.append(Node(advanced_pose, near_idx))
        return State.advanced
    
    return State.trapped

def connect(tree: RRT, q: NDArray) -> State:
    S = None
    while S != State.advanced:
        S = extend(tree, q)
    return S

def get_path(T_a: RRT, T_b: RRT):
    poses= []
    current_node = T_a[-1]
    
    while current_node.parent_idx != None:
        poses.append(current_node.pose)
        current_node = T_a[current_node.parent_idx]

    current_node = T_b[-2]  #-2 to not count the connecting node again
    while current_node.parent_idx != None:
        poses.insert(0, current_node.pose)
        current_node = T_a[current_node.parent_idx]
    
    return poses



def RRT_connect_planner(q_init: NDArray, q_goal: NDArray, max_iter):
    T_a = [Node(q_init)]
    T_b = [Node(q_goal)]
    ndof = 6
    for _ in range(max_iter):
        q_rand = random_config(ndof)
        if not extend(T_a, q_rand) == State.trapped:
            if connect(T_b, T_a[-1].pose) == State.reached:
                return get_path(T_a, T_b)
        T_a, T_b = T_b, T_a  # swap the roles of the trees
    print("algorithm failed")
    return 

    


if __name__ == '__main__':
   com._mainLoop(RRT_connect_planner)