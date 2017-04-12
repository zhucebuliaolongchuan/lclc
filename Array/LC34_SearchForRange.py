"""
34. Search For a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        return self.binarySearch(nums, target, 0, len(nums) - 1)
        
    def binarySearch(self, nums, target, begin, end):
        if begin > end:
            return -1, -1
        elif begin == end:
            if nums[begin] != target:
                return -1, -1
            else:
                return begin, end
        else:
            mid = begin + (end - begin) / 2
            if nums[mid] < target:
                return self.binarySearch(nums, target, mid + 1, end)
            elif nums[mid] > target:
                return self.binarySearch(nums, target, begin, mid - 1)
            else:
				# If we find the postion of the target value
                i, j = mid, mid
                while j + 1 <= end and nums[j + 1] == target:
                    j += 1
                while i - 1 >= begin and nums[i - 1] == target:
                    i -= 1
                return i, j
