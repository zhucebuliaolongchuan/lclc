"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.backtrack(s, '', res, [], 0, 0)
        return res

    def backtrack(self, s, cur_s, res, partition, index, count):
        if index >= len(s):
            if count == len(s):
                res.append(partition)
            return
        else:
            new_s = cur_s + s[index]
            if new_s == new_s[::-1]:
                self.backtrack(s, '', res, partition + [new_s], index + 1, count + len(new_s))
            self.backtrack(s, new_s, res, partition, index + 1, count)
