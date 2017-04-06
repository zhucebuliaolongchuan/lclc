"""
216. Combination Sum 3
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(k, n, [], res, 1)
        return res

    def backtrack(self, k, n, cur, res, index):
        if len(cur) == k and sum(cur) == n:
            res.append(cur)
            return
        if sum(cur) > n or len(cur) > k:
            return
        for i in range(index, 10):
            self.backtrack(k, n, cur + [i], res, i + 1)
        return
