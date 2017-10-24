class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = s.strip().split()
		s = s[::-1]
		for i in range(len(s)):
			s[i] = self.reverse(s[i])
		return " ".join(s)

	def reverse(self, s):
		s = list(s)
		return "".join(reversed(s))


test = Solution()
s = "  s  b dahi djaiosajd ajs da   djiaosjd   djaoi "
print test.reverseWords(s)
