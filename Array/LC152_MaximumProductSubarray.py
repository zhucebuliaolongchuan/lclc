"""
152. Maximum Product Subarray (Dynamic Programming)
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = min_value = res = nums[0]
        for i in range(1, len(nums)):
			# If the current value is a negative number, the current max product should exchange with the current min product
            if nums[i] < 0:
                max_value, min_value = min_value, max_value
            max_value = max(max_value * nums[i], nums[i])
            min_value = min(min_value * nums[i], nums[i])
            res = max(res, max_value)
        return res
