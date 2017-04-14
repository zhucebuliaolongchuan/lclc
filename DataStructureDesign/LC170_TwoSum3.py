"""
170. TwoSum 3 - Data Structure Design
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.num = []

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.num.append(number)
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        d = {}
        for i in range(len(self.num)):
            target = value - self.num[i]
            if target not in d:
                d[target] = i
        for i in range(len(self.num)):
            if self.num[i] in d and d[self.num[i]] != i:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
