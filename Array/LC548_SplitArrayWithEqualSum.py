"""
548. Split Array With Equal Sum
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
	0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.

where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
"""
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        total = [nums[0]]
        for i in range(1, len(nums)):
            total.append(nums[i] + total[i - 1])
        for mid in range(3, len(nums) - 3):
            quarters = set()
            for left in range(1, mid - 1):
                if total[left - 1] == total[mid - 1] - total[left]:
                    quarters.add(total[left - 1])
            for right in range(mid + 2, len(nums) - 1):
                if total[right - 1] - total[mid] == total[-1] - total[right] and total[right - 1] - total[mid] in quarters:
                    return True
        return False
