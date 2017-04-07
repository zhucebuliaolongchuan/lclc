"""
533. Lonely Pixel 2
Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
"""
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        rule_2 = {}
        for i in range(len(picture)):
            for j in range(len(picture)):
                if j != i and picture[i] == picture[j]:
                    if i in rule_2:
                        rule_2[i].append(j)
                    else:
                        rule_2[i] = [j]
        rows = []
        for i in range(len(picture)):
            rows.append(picture[i].count('B'))
        cols = {}
        for j in range(len(picture[-1])):
            cols[j] = []
            for i in range(len(picture)):
                if picture[i][j] == 'B':
                    cols[j].append(i)
        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[-1])):
                if picture[i][j] == 'B' and rows[i] == len(cols[j]) == N:
                    if (i in rule_2.keys() and sorted(rule_2[i] + [i]) == sorted(cols[j])) or len(cols[j]) == N == 1:
                        count += 1
        return count
