"""
60. Permutation Sequence
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cur = 1
        factorial = [1]
        for i in range(1, n):
            cur *= i
            factorial.append(cur)
        nums = [i + 1 for i in range(n)]
        res = ''
        k -= 1
        for i in range(1, n + 1):
            index = k / factorial[n - i]
            k -= index * factorial[n - i]
            res += str(nums[index])
            nums.remove(nums[index])
        return res
