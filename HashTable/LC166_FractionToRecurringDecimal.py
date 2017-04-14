"""
166. Fraction To Decimal Part
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
For example,
Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 or denominator == 0:
            return '0'
        res = [] if numerator * denominator > 0 else ['-']
        # Intergal Part
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator > denominator:
            res.append(str(numerator / denominator))
            numerator %= denominator
        else:
            res.append('0')
        # Decimal Part
        if numerator != 0:
            res.append('.')
            repeat = collections.defaultdict(int)
            repeat[numerator] = len(res)
            while numerator > 0:
                numerator *= 10
                res.append(str(numerator / denominator))
                numerator %= denominator
                if numerator in repeat.keys():
                    res.insert(repeat[numerator], '(')
                    res.append(')')
                    break
                else:
                    repeat[numerator] = len(res)
        return ''.join(res)
