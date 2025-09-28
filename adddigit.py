class Solution(object):
    def addDigits(self, num):
        num = sum(int(digit) for digit in str(num))
        num = sum(int(digit) for digit in str(num))
        if num > 9 :
            return sum(int(digit) for digit in str(num))
        return num