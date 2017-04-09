"""
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:
Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]
"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = {}
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1] += [v2]
            graph[v2] += [v1]
        visited = [False for i in range(n)]
        for i in range(n):
            res[i] = self.findDepth(i, graph, visited)
        min_height = min(res.values())
        nodes = []
        for node in res.keys():
            if res[node] == min_height:
                nodes.append(node)
        return nodes
        
    def findDepth(self, node, graph, visited):
        if visited[node] == True:
            return -1
        else:
            res = 0
            visited[node] = True
            for neigh in graph[node]:
                res = max(res, self.findDepth(neigh, graph, visited) + 1)
            visited[node] = False
            return res
