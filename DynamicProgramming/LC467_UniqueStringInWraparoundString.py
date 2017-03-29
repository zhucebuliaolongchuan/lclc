"""
467. Unique Substring in Wraparound String
Consider the strings to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.
"""
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = dict()
        max_length = 0
        for i in range(len(p)):
            if i > 0 and ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25:
                max_length += 1
            else:
                max_length = 1
            if p[i] not in count:
                count[p[i]] = max_length
            else:
                count[p[i]] = max(count[p[i]], max_length)
        return sum(count.values())
