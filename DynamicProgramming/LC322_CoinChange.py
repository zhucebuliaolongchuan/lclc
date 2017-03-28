"""
322.Coin Change
	You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
		# Initialize the dp array
        dp = [sys.maxint for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
			# Calculate the min number of coins that to change the current number
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == sys.maxint else dp[amount]
