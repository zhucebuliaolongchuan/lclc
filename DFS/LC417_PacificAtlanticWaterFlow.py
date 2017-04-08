"""
417. Pacific Atlantic Water Flow
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
# First Solution: Naive, Time-Consuming
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[-1])):
                visited_1 = [[False for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
                visited_2 = [[False for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
                if self.canFlowToPacific(matrix, i, j, matrix[i][j], visited_1) and self.canFlowToAtlantic(matrix, i, j, matrix[i][j], visited_2):
                    res.append([i, j])
        return res
    
    def canFlowToPacific(self, matrix, x, y, last, visited):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[-1]):
            if visited[x][y] == True:
                return False
            if matrix[x][y] > last:
                return False
            else:
                visited[x][y] = True
                return self.canFlowToPacific(matrix, x, y - 1, matrix[x][y], visited) \
                        or self.canFlowToPacific(matrix, x - 1, y, matrix[x][y], visited) \
                        or self.canFlowToPacific(matrix, x, y + 1, matrix[x][y], visited) \
                        or self.canFlowToPacific(matrix, x + 1, y, matrix[x][y], visited)
        else:
            if x < 0 or y < 0:
                return True
            else:
                return False

    def canFlowToAtlantic(self, matrix, x, y, last, visited):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[-1]):
            if visited[x][y] == True:
                return False
            if matrix[x][y] > last:
                return False
            else:
                visited[x][y] = True
                return self.canFlowToAtlantic(matrix, x + 1, y, matrix[x][y], visited) \
                        or self.canFlowToAtlantic(matrix, x, y + 1, matrix[x][y], visited) \
                        or self.canFlowToAtlantic(matrix, x - 1, y, matrix[x][y], visited) \
                        or self.canFlowToAtlantic(matrix, x, y - 1, matrix[x][y], visited) 
        else:
            if x >= len(matrix) or y >= len(matrix[-1]):
                return True
            else:
                return False
# Second Solution: More Concise than the first solution, but still time consuming
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cells = []
        for i in range(len(matrix)):
            for j in range(len(matrix[-1])):
                res = [False, False]
                visited = [[False for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
                self.dfs(matrix, i, j, matrix[i][j], visited, res)
                if res == [True, True]:
                    cells.append([i, j])
        return cells
    
    def dfs(self, matrix, x, y, last, visited, res):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[-1]):
            if visited[x][y] == True or matrix[x][y] > last:
                return
            else:
                visited[x][y] = True
                directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
                for dic in directions:
                    self.dfs(matrix, x + dic[0], y + dic[1], matrix[x][y], visited, res)
        else:
            if x < 0 or y < 0:
                res[0] = True
            if x >= len(matrix) or y >= len(matrix[-1]):
                res[1] = True
            return
# Third Solution: Smart and Trick Solution. Flow the water from the sides util it stops, if the cell is visited by the water from two sides, return it
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) <= 0:
            return []
        cells = []
        p_visited = [[False for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
        a_visited = [[False for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            self.dfs(matrix, i, 0, 0, a_visited)
            self.dfs(matrix, i, len(matrix[-1]) - 1, 0, p_visited)
        for j in range(len(matrix[-1])):
            self.dfs(matrix, 0, j, 0, a_visited)
            self.dfs(matrix, len(matrix) - 1, j, 0, p_visited)
        for i in range(len(matrix)):
            for j in range(len(matrix[-1])):
                if a_visited[i][j] == p_visited[i][j] == True:
                    cells.append([i, j])
        return cells
    
    def dfs(self, matrix, x, y, last, visited):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[-1]):
            if visited[x][y] == True:
                return
            if last <= matrix[x][y]:
                visited[x][y] = True
                directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
                for dic in directions:
                    self.dfs(matrix, x + dic[0], y + dic[1], matrix[x][y], visited)
