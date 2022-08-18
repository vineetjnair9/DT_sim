import numpy as np
import math
from sklearn.neighbors import NearestNeighbors
from pylib import Communication
from typing import List
JointValues = List[float]
JointValuesList = List[JointValues]
import pickle
com = Communication()

# Hyperparameters
K = 10 # no. of iterations
eps = 0.01
dof = 6

def random_config(dof):
    rng = np.random.default_rng(seed=42)
    return rng.uniform(low=-math.pi,high=math.pi,size=dof)

def build_RRT(q):
    # Returns 2 outputs
    # RRT = list showing parent node of each node/vertex in tree
    # joints = joint angles/configurations of each node in tree

    # Create list to show parent nodes of each node/vertex
    RRT = []
    joints = []

    # Starting point (root node)
    joints.append(q)
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
    joints_fit = np.array(joints)
    if len(joints) == 1:
        neigh.fit(joints_fit.reshape(1,-1))
    else:
        neigh.fit(joints_fit)
    q_near_index = neigh.kneighbors(np.array(q).reshape(1,-1),return_distance=False)
    q_near_index = int(q_near_index[0][0])
    q_near = joints[q_near_index]

    if np.linalg.norm(q - q_near) < eps:
        q_new = q

         # Status codes: 
        if com.hasCollision(q_new.tolist()):
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
        if com.hasCollision(q_new.tolist()):
            print('Trapped')
            status = 2

        else: # Add new node to tree
            joints.append(q_new)

            # Record parent node of newly added vertex
            RRT.append(q_near_index)

            print('Advanced')
            status = 1

    return status, RRT, joints, q_new

def connect(RRT,joints,q):
    status = 0
    while status != 1:
        status, RRT, joints, q_new = extend_RRT(RRT,joints,q)
    return status, RRT, joints

def traverse(RRT, joints, visited, node, path, poses):
    while node != 0: # start point
        if node not in visited:
            visited.add(node)
            path.append(node)
            poses.append(joints[node])
            visited, node, path, poses = traverse(RRT, joints, visited, RRT[node], path, poses)
    return visited, node, path, poses

def get_path(RRT, joints):
    visited = set()
    node = RRT[-1] # end goal vertex
    path = []
    poses = []
    visited, node, path, poses = traverse(RRT, joints, visited, node, path, poses)
    return path, poses
        
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

                # Check which is tree A or B
                if joints1[0] == q_init:
                    RRT_a = RRT1
                    RRT_b = RRT2
                    joints_a = joints1
                    joints_b = joints2
                else:
                    RRT_a = RRT2
                    RRT_b = RRT1
                    joints_a = joints2
                    joints_b = joints1

                RRT_b = RRT_a.reverse() + len(RRT_a)
                RRT = RRT_a + RRT_b
                joints = joints_a + joints_b.reverse
                return RRT, joints
        RRT2 = RRT1
        joints2 = joints1
    print('Failure')
    return

q_init = [-2.088896595860315, -2.017484530838456, -1.611079074071187, -0.07048029509520992, 0.5640853634948029, -1.093268836863869]
q_goal = [-1.1862522062110772, -1.6803693959628347, -2.2637243080183618, -0.7820281405620721, 1.6033439459250105, 0.38341871361603497]
RRT_connect_planner(q_init,q_goal)

def compilePath(start: JointValues, stop: JointValues, savetofile=False) -> JointValuesList:

    print('start = ', start)
    print('stop = ', stop)
    if len(start) != 6 or len(stop) != 6:
        print('Array length mismatch')
        return None

    poseList = list()
    poseList.append(start)

    diff = [0] * 6
    for index in range(6):
        diff[index] = stop[index] - start[index]
    m = max(diff)
    steps = int(m / 0.1)

    for step in range(steps):
        jointValues = [0] * 6
        percentage = step / steps
        for index in range(6):
            addValue = percentage * diff[index]
            jointValues[index] = start[index] + addValue
        hsCol = com.hasCollision(jointValues)
        clr = com.clearance(jointValues)
        print(hsCol, clr)
        poseList.append(jointValues)

    poseList.append(stop)
    
    # save the pose to file
    if savetofile:
        with open("Path", 'wb') as f:
            pickle.dump(poseList, f)
    
    return poseList
   
if __name__ == '__main__':
   com._mainLoop(compilePath)
