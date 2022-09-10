class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        reverse = 0
        if num[0] == '-': 
            reverse = -int(num[:0:-1])
        else:
            reverse = int(num[::-1])
        print(reverse)
        if -math.pow(2,31) <= reverse and reverse <= math.pow(2,31):
            return reverse
        else:
            return 0