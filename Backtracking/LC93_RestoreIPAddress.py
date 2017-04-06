"""
93. Restore IP Address
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
	# Use three loops
        while i <= 2 and i <= len(s) - 3:
            j = i + 1
            while j - i <= 3 and j <= len(s) - 2:
                k = j + 1
                while k - j <= 3 and k <= len(s) - 1:
                    s1, s2, s3, s4 = s[:i + 1], s[i + 1:j + 1], s[j + 1:k + 1], s[k + 1:]
                    if self.isValidIP(s1) and self.isValidIP(s2) and self.isValidIP(s3) and self.isValidIP(s4):
                        res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
                    k += 1
                j += 1
            i += 1
        return res
    # Determine the IP sub-domain valid or not
    def isValidIP(self, s):
        if len(s) > 3 or len(s) == 0 or int(s) > 255 or (len(s) > 1 and s[0] == '0'):
            return False
        return True
