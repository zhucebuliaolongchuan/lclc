"""
310. Minimum Height Tree
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
        min_res = sys.maxint
        for i in range(n):
            visited = [False for _ in range(n)]
            res[i] = self.bfsFindDepth(i, graph, visited, min_res)
            min_res = min(min_res, res[i])
        nodes = []
        for node in res.keys():
            if res[node] == min_height:
                nodes.append(node)
        return nodes
    def bfsFindDepth(self, node, graph, visited, min_res):
        depth = 0
        last_layer = [node]
        cur_layer = []
        while len(last_layer) > 0 and depth <= min_res:
            for node in last_layer:
                if visited[node] == False:
                    for neigh in graph[node]:
                        if visited[neigh] == False:
                            cur_layer.append(neigh)
                    visited[node] = True
                else:
                    continue
            if len(cur_layer) == 0:
                break
            else:
                depth += 1
                last_layer = cur_layer
                cur_layer = []
        return depth
# Solution 2: A very smart solution
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1] += [v2]
            graph[v2] += [v1]
        nodes = [i for i in range(n)]
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                parent = graph[node].pop()
                graph[parent].remove(node)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves
        return leaves
