"""
267. Palindrome Permutation
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Show Hint 
Show Tags
Show Similar Problems

"""
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        odd_even = {}
        for i in range(len(s)):
            if s[i] in odd_even:
                odd_even[s[i]] += 1
            else:
                odd_even[s[i]] = 1
        new_s, odd, odd_char = [], 0, ''
        for key in odd_even.keys():
            if odd_even[key] % 2 == 1:
                odd += 1
                odd_char = key
                new_s += [key] * ((odd_even[key] - 1) / 2)
            else:
                new_s += [key] * (odd_even[key] / 2)
        if odd > 1:
            return []
        else:
            res = []
            used = [False for _ in range(len(new_s))]
            self.backtrack(new_s, '', res, used, odd_char)
            return res

    def backtrack(self, s, cur_s, res, used, odd_char):
        if len(s) == len(cur_s):
            res.append(cur_s + odd_char +cur_s[::-1])
            return
        else:
            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1] and used[i - 1] == False:
                    continue
                if used[i] == False:
                    used[i] = True
                    self.backtrack(s, s[i] + cur_s, res, used, odd_char)
                    used[i] = False
