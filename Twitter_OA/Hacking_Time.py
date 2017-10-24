class Solution(object):
	def hacking(self, en_s):
		key = [4, 0, 7, 1, 3, 2, 1]
		key_pointer = 0
		de_s = ""
		for i in range(len(en_s)):
			if en_s[i].isalpha():
				print ord(en_s[i])
				key_digit = key[key_pointer % len(key)]
				key_pointer += 1
				if 65 <= ord(en_s[i]) <= 90:
					if ord(en_s[i]) - key_digit < 65:
						de_s += chr(ord(en_s[i]) + 26 - key_digit)
					else:
						de_s += chr(ord(en_s[i]) - key_digit)
				elif 97 <= ord(en_s[i]) <= 122:
					if ord(en_s[i]) - key_digit < 97:
						de_s += chr(ord(en_s[i]) + 26 - key_digit)
					else:
						de_s += chr(ord(en_s[i]) - key_digit)
			else:
				de_s += en_s[i]
		return de_s

test = Solution()
message = "Li, ailu jw au facntll"
print test.hacking(message)
