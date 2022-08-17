from typing import List
import numpy as np
import random as rand

def dfs(graph: List[List[int]], start: int , goal: int)->list[int]:
    n_nodes = len(graph)
    visited = np.zeros(n_nodes, dtype=bool)
    
    def transverse(graph: List[List[int]], visited,  index: int):
    
        list_copy = graph[index].copy()
        for node in list_copy:

            if visited[node]:
                graph[index].remove(node)
                continue
            
            elif node == goal:
                path = []
                j=0
                while graph[j][0] != goal:
                    path.append(graph[j][0])
                    j += 1
                path.append(goal)
                return path

            visited[node] = True
            transverse(graph, visited, node)
        return  #if the list is empty

if __name__=="__main__":
    