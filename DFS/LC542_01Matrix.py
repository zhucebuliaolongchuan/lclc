"""
542. 01 Matrix
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1: 
Input:
0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0

Example 2: 
Input:
0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        height, width = len(matrix), len(matrix[-1])
        dists = [[0 if matrix[i][j] == 0 else sys.maxint for j in range(width)] for i in range(height)]
        # Top To Down
        for row in range(1, height):
            for col in range(width):
                if dists[row][col] != 0:
                    dists[row][col] = min(dists[row - 1][col] + 1, dists[row][col])
        # Down To Top
        for row in reversed(range(height - 1)):
            for col in range(width):
                if dists[row][col] != 0:
                    dists[row][col] = min(dists[row + 1][col] + 1, dists[row][col])
        # Left To Right
        for row in range(height):
            for col in range(1, width):
                if dists[row][col] != 0:
                    dists[row][col] = min(dists[row][col - 1] + 1, dists[row][col])
        # Right To Left
        for row in range(height):
            for col in reversed(range(width - 1)):
                if dists[row][col] != 0:
                    dists[row][col] = min(dists[row][col + 1] + 1, dists[row][col])
        return dists
