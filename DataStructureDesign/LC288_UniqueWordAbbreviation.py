"""
288. Unique Word Abbreviation

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)
b) d|o|g                   --> d1g
c) i|nternationalizatio|n  --> i18n
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr_d = {}
        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            if abbr in self.abbr_d:
                if word not in self.abbr_d[abbr]:
                    self.abbr_d[abbr].append(word)
            else:
                self.abbr_d[abbr] = [word]
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        if abbr not in self.abbr_d:
            return True
        else:
            return self.abbr_d[abbr] == [word]
# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
