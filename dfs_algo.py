from typing import List
import numpy as np
import random as rand

def dfs(graph: List[List[int]], start: int , goal: int)->list[int]:
    n_nodes = len(graph)
    visited = set()
    
    def transverse(graph: List[List[int]], visited: set,  index: int, path=None):
        if not path:
            path = [index]
            visited = {index}

        for node in graph[index]:

            if node in visited:
                continue
            
            path.append(node)
            visited.add(node)
            if node == goal:
                return path
            else: 
                return transverse(graph, visited, node, path)
        
        # if all nodes are visited we go 1 step back the tree and try new branch
        path.pop()
        return transverse(graph, visited, path[-1], path)

    return transverse(graph, visited, start)

if __name__=="__main__":
    test = [
        [5, 0, 1],
        [1, 2],
        [2, 3],
        [0, 3, 4,],
        [3],
        [0]]
    print(dfs(test, 0, 4))