class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        count = 1
        i = 2
		# Minimize the time complexity
        while i <= math.sqrt(num):
            if num % i == 0:
                count += i
				# Add the divisor that we could not check in the current loop
                if num / i != i:
                    count += num / i
            i += 1
        return count == num
