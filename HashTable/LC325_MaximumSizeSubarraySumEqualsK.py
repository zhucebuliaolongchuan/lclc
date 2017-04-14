"""
325. Maximum Size Subarray Sum Equals K
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
"""
# Please note that if searching the key like d.keys() instead of d, it will use the iterable list to match the key.  
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d, total, max_len = {0:-1}, 0, 0
        for i in xrange(len(nums)):
            total += nums[i]
            if total not in d:
                d[total] = i
            if total - k in d:
                max_len = max(max_len, i - d[total - k])
        return max_len
