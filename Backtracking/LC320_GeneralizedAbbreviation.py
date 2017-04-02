"""
320. Generalized Abbreviation
Write a function to generate the generalized abbreviations of a word.
"""

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.backtrack(word, 0, '', 0, res)
        return re
s
    def backtrack(self, word, pos, cur, count, res):
	str_count = '' if count == 0 else str(count)
        if pos == len(word):
	    cur += str_count
            res.append(cur)
        else:
            self.backtrack(word, pos + 1, cur, count + 1, res)
            self.backtrack(word, pos + 1, cur + str_count + word[pos], 0, res)
