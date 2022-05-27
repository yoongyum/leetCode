class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            step += 1
            if num%2==0:
                num >>= 1
            else :
                num -= 1
                
        return step