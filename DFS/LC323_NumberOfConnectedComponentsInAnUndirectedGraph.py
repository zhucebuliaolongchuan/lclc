"""
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
"""
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {i:[] for i in range(n)}
        for v1, v2 in edges:
            graph[v1] += [v2]
            graph[v2] += [v1]
        visited = [False for _ in range(n)]
        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1
                self.dfsFind(i, graph, visited)
        return count
    def dfsFind(self, i, graph, visited):
        if visited[i] == True:
            return
        else:
            visited[i] = True
            for v in graph[i]:
                self.dfsFind(v, graph, visited)
