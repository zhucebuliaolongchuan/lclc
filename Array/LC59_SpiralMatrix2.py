"""
59. Spiral Matrix 2
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row_begin, row_end = 0, n - 1
        col_begin, col_end = 0, n - 1
        count = 1
        while row_begin <= row_end and col_begin <= col_end:
            for i in range(col_begin, col_end + 1):
                matrix[row_begin][i] = count
                count += 1
            row_begin += 1
            for j in range(row_begin, row_end + 1):
                matrix[j][col_end] = count
                count += 1
            col_end -= 1
            if row_begin <= row_end:
                for k in reversed(range(col_begin, col_end + 1)):
                    matrix[row_end][k] = count
                    count += 1
                row_end -= 1
            if col_begin <= col_end:
                for l in reversed(range(row_begin, row_end + 1)):
                    matrix[l][col_begin] = count
                    count += 1
                col_begin += 1
        return matrix
