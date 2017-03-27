class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 or s[0] == '0':
            return 0
        else:
            dp = [0 for _ in range(len(s))]
            if len(s) == 1:
                return 1
            else:
                # Initialize the the first and second element
                if s[1] == '0':
                    if s[0] == '1' or s[0] == '2':
                        dp[0], dp[1] = 0, 1
                    else:
                        return 0
                else:
                    if 10 < int(s[0 : 2]) <= 26:
                        dp[0], dp[1] = 1, 2
                    else:
                        dp[0], dp[1] = 1, 1
            for i in range(2, len(s)):
                if s[i] == '0':
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        dp[i] = dp[i - 2]
                    else:
                        return 0
                else:
                    if 10 < int(s[i - 1 : i + 1]) <= 26:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
            return dp[-1]
