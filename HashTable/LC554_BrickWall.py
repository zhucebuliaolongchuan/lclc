"""
554. Brick Wall
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) <= 0:
            return 0
        height = sum(wall[0])
        s = collections.defaultdict(int)
        max_len = 0
        for i in range(len(wall)):
            total = 0
            for j in range(len(wall[i])):
                total += wall[i][j]
                if j < len(wall[i]) - 1:
                    s[total] += 1
                    max_len = max(max_len, s[total])
        return len(wall) - max_len
