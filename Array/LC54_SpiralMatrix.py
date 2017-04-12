"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0:
            return res
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[-1]) - 1
        while row_begin <= row_end and col_begin <= col_end:
            # top-left to top-right
            for i in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            # top-right to bottom-right
            for j in range(row_begin, row_end + 1):
                res.append(matrix[j][col_end])
            col_end -= 1
            # bottom-right to bottom-left
            if row_begin <= row_end:
                for k in reversed(range(col_begin, col_end + 1)):
                    res.append(matrix[row_end][k])
                row_end -= 1
            # bottom-left to top-left
            if col_begin <= col_end:
                for l in reversed(range(row_begin, row_end + 1)):
                    res.append(matrix[l][col_begin])
                col_begin += 1
        return res
