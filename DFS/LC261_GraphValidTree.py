"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
Hint:
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {i:[] for i in range(n)}
        for v1, v2 in edges:
            graph[v1] += [v2]
            graph[v2] += [v1]
        visited = [False for i in range(n)]
        if self.hasCircle(0, None, visited, graph) == True:
            return False
        return False not in visited

    def hasCircle(self, v, parent, visited, graph):
        if visited[v] == True:
            return True
        else:
            visited[v] = True
            for neigh in graph[v]:
                if neigh != parent and self.hasCircle(neigh, v, visited, graph) == True:
                    return True
            return False
