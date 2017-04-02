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
        return res

    def backtrack(self, word, pos, cur, count, res):
        if pos == len(word):
            if count > 0:
                cur += str(count)
            res.append(cur)
        else:
            self.backtrack(word, pos + 1, cur, count + 1, res)
            if count > 0:
                self.backtrack(word, pos + 1, cur + str(count) + word[pos], 0, res)
            else:
                self.backtrack(word, pos + 1, cur + word[pos], 0, res)
