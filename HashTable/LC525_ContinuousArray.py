"""
525. Continuous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        index_sum = {0 : -1}
        total, max_len = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            if total in index_sum:
                max_len = max(max_len, i - index_sum[total])
            else:
                index_sum[total] = i
        return max_len
