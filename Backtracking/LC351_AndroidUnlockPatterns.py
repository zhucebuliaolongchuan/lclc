"""
LC351. Android Unlock Patterns

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
"""
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [[0 for _ in range(10)] for _ in range(10)]
        visited = [False for _ in range(10)]
	# Find the overlap number
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        res = 0
        for i in range(m, n + 1):
            # for j in range(1, 10):
            #     res += self.dfs(j, visited, skip, i - 1)
            res +=(self.dfs(1, visited, skip, i - 1) * 4  # 1, 3, 7, 9 are symmetric
            res += self.dfs(2, visited, skip, i - 1) * 4  # 2, 4, 6, 8 are symmetric
            res += self.dfs(5, visited, skip, i - 1)
        return res
        
    def dfs(self, cur, visited, skip, step):
        if step < 0:
            return 0
        if step == 0:
            return 1
        res = 0
        visited[cur] = True
        for i in range(1, 10):
            if visited[i] == False and (skip[cur][i] == 0 or visited[skip[cur][i]] == True):
                res += self.dfs(i, visited, skip, step - 1)
        visited[cur] = False
        return res
