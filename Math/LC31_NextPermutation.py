"""
31.Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, k = len(nums) - 2, -1
        while i >= 0:
            if nums[i] < nums[i + 1]:
                k = i
                break
            else:
                i -= 1
        if k == -1:
            nums.reverse()
            return
        else:
            l = len(nums) - 1
            while l >= 0:
                if nums[l] > nums[k]:
                    break
                else:
                    l -= 1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k + 1:] = reversed(nums[k + 1:])
            return
