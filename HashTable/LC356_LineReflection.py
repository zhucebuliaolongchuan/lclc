"""
356. Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
Example 1:
Given points = [[1,1],[-1,1]], return true.
Example 2:
Given points = [[1,1],[-1,-1]], return false.
"""
# If there are odd number different points, it will be right if there are odd number on the parallel line 
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 0:    return True
        X = max(points)[0] + min(points)[0]
        return {(x, y) for x, y in points} == {(X - x, y) for x, y in points}
