class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row_len, col_len = len(grid), len(grid[-1])
        row_hits, col_hits, max_kills = 0, [0 for _ in range(col_len)], 0
        for i in range(row_len):
            for j in range(col_len):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    k = j
                    while k < col_len and grid[i][k] != 'W':
                        row_hits += (grid[i][k] == 'E') 
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < row_len and grid[k][j] != 'W':
                        col_hits[j] += (grid[k][j] == 'E')
                        k += 1
                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_hits + col_hits[j])
        return max_kills
