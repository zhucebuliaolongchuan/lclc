"""
211. Add and Search Word
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.word_dict.keys():
            self.word_dict[len(word)].append(word)
        else:
            self.word_dict[len(word)] = [word]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.word_dict.keys():
            return False
        else:
            for w in self.word_dict[len(word)]:
                if self.match(w, word):
                    return True
            return False

    def match(self, word1, word2):
        for i in range(len(word1)):
            if word1[i] != '.' and word2[i] != '.' and word1[i] != word2[i]:
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
