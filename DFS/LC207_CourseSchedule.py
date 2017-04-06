"""
207. Course Schedule 1
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        visited = [False for _ in range(numCourses)]
        for course in prerequisites:
            if course[0] in graph:
                graph[course[0]].append(course[1])
            else:
                graph[course[0]] = [course[1]]
        for key in graph.keys():
            if self.hasCircle(graph, visited, key) == True:
                return False
        return True

    def hasCircle(self, graph, visited, cur):
        if cur not in graph.keys():
            return False
        if visited[cur] == True:
            return True
        for neighbor in graph[cur]:
            visited[cur] = True
            if visited[neighbor] == True or self.hasCircle(graph, visited, neighbor) == True:
                return True
            visited[cur] = False
        return False
