# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:16:59 2024

@author: Lycoris
"""


from collections import deque

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : [],
  '8' : []
}

def bfs(graph, start):
    visited = set()  # 用來記錄已經訪問過的節點
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
                
def main():
    bfs(graph, '5')
    
main()