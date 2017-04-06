"""
89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

Show Company Tags
Show Tags

"""
# Solution 1
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res

# Backtrack Solution 2, more general, but the online judge just accept one particular pattern
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = [i for i in range(1 << n)]
        res = []
        self.backtrack(res, nums, [0])
        return res[-1]

    def backtrack(self, res, nums, temp_nums):
        if len(temp_nums) == len(nums):
            res.append(temp_nums)
            return
        else:
            for i in range(1, len(nums)):
                if nums[i] not in temp_nums:
                    if len(temp_nums) > 0 and bin(temp_nums[-1] ^ nums[i]).count('1') == 1 or len(temp_nums) == 0:
                        self.backtrack(res, nums, temp_nums + [nums[i]])
