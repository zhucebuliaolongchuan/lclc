class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(len(strs) + 1)]
        for i in range(len(strs) + 1):
            ones, zeros = strs[i - 1].count('1'), strs[i - 1].count('0')
            for j in range(n + 1):
                for k in range(m + 1):
                    if i == 0:
                        dp[i][j][k] = 0
                    elif j >= ones and k >= zeros:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - ones][k - zeros] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[-1][-1][-1]
