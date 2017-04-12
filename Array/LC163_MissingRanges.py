"""
163. Missing Ranges
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
# In this question, there are so many corner cases that you have to handle.
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
		# Handle the case that there is no element in the array
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
		# Just handle the inner range inside the array
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 2:
                res.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))    
            elif nums[i] - nums[i - 1] == 2:
                res.append(str(nums[i - 1] + 1))
            else:
                continue
        if lower < nums[0]:
            if lower == nums[0] - 1:
                res.insert(0, str(lower))
            else:
                res.insert(0, str(lower) + '->' + str(nums[0] - 1))
        if upper > nums[-1]:
            if upper == nums[-1] + 1:
                res.append(str(upper))
            else:
                res.append(str(nums[-1] + 1) + '->' + str(upper))
        return res
