from typing import List
import numpy as np

def dfs(graph: List[List[int]], start: int , goal: int)->list[int]:
    n_nodes = len(graph)
    visited = np.zeros(n_nodes, dtype=bool)
    
    def transverse(graph: List[List[int]], visited,  index: int):

        for i, node in enumerate(graph[index]):

            if visited[node]:
                graph[index].remove(i)
            else:
                visited[node] = True
            

            if node == goal:
                path = []
                j=0
                while graph[j][0] != goal:
                    path.append(graph[j][0])
                    j += 1
                path.append(goal)
                return path

            elif node:
                graph[index].remove(node)
            transverse(graph[node])