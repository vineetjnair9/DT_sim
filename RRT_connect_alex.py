from dataclasses import dataclass
from enum import Enum
from typing import List, TextIO
import numpy as np
from numpy.typing import NDArray, ArrayLike
from fwd_kinematics import fwd_kinematics
from pylib import Communication
from visual_3d import Visual3D
com = Communication()

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
    return (2*np.pi)*np.random.rand(dim)-np.pi

def nearest_neighbour(pose: NDArray, tree: RRT) -> int:
    
    min_dist = np.inf
    for i, node in enumerate(tree):
        dist = np.linalg.norm(node.pose-pose)
        
        if dist<min_dist:
            min_dist = dist
            min_idx = i

    return min_idx
    

def new_config(q: NDArray, q_near: NDArray, eps) -> int:

    dist = np.linalg.norm(q-q_near)
    if dist<eps:
        if com.hasCollision(q.tolist()): #TODO switch this back after testing
            return State.trapped
        else: 
            return State.reached
    
    # calculating advancing direction and pose
    diff = q - q_near
    unit_dir = (diff)/np.linalg.norm(diff)
    advanced_pose = q_near + eps*unit_dir
    
    if com.hasCollision(advanced_pose.tolist()):
        return State.trapped

    return State.advanced 

def extend(tree: RRT, q_rand: NDArray, eps=0.1, savetofile: TextIO=None) -> State:
    
    near_idx = nearest_neighbour(q_rand, tree)
    state = new_config(q_rand, tree[near_idx].pose, eps)

    if state == State.reached:
        tree.append(Node(q_rand, near_idx))
        
        #save to file
        if savetofile:
            clearence = com.clearance(q_rand.tolist())
            data_str = " ".join([str(x) for x in q_rand]) + " " + str(clearence) + "\n"
            savetofile.write(data_str)
        return State.reached

    elif state == State.advanced:
        diff = q_rand - tree[near_idx].pose
        unit_dir = (diff)/np.linalg.norm(diff)
        advanced_pose = tree[near_idx].pose + eps*unit_dir
        tree.append(Node(advanced_pose, near_idx))
        
        #save to file
        if savetofile:
            clearence = com.clearance(advanced_pose.tolist())
            data_str = " ".join([str(x) for x in advanced_pose]) + " " + str(clearence) + "\n"
            savetofile.write(data_str)
        return State.advanced
    
    return State.trapped

def connect(tree: RRT, q: NDArray, savetofile=None) -> State:
    S = extend(tree, q, savetofile=savetofile)
    while S == State.advanced:
        S = extend(tree, q, savetofile=savetofile)
    return S

def get_path(T_init: RRT, T_goal: RRT):
    poses= []
    current_node = T_goal[-1]
    
    # construct the path from connecting node to goal node
    while current_node.parent_idx != None:
        poses.append(current_node.pose.tolist())
        current_node = T_goal[current_node.parent_idx]

    # add the path from connecting node to init node to front of path
    current_node = T_init[-2]  #-2 to not count the connecting node again
    while current_node.parent_idx != None:
        poses.insert(0, current_node.pose.tolist())
        current_node = T_init[current_node.parent_idx]

    return poses



def RRT_connect_planner(q_init: NDArray, q_goal: NDArray, max_iter: int=10000) -> List[float]:

    T_a = [Node(q_init)]
    T_b = [Node(q_goal)]

    ndof = 6
    with open("poses.txt", 'w') as f:
        for _ in range(max_iter):
            q_rand = random_config(ndof)
            
            if not extend(T_a, q_rand, savetofile=f) == State.trapped:
                if connect(T_b, T_a[-1].pose, savetofile=f) == State.reached:                  
                    if not np.array_equal(T_a[0].pose, q_init):
                        if not np.array_equal(T_b[0].pose, q_init):
                            raise ValueError  # for debugging, something is wrong in this case
                        T_a, T_b = T_b, T_a  # swap trees, so we pass in the right order to get_path()
                    path = get_path(T_a, T_b)
                    return path
            
            T_a, T_b = T_b, T_a  # swap the roles of the trees
    print("algorithm failed")
    return 

    


if __name__ == '__main__':
    com._mainLoop(RRT_connect_planner)
   #q_init = np.zeros(6)
   #q_goal = np.ones(6)*np.pi
   #print(RRT_connect_planner(q_init, q_goal))
   
