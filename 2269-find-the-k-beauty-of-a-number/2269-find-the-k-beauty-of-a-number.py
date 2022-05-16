class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strN = str(num)
        
        answer = 0
        for i in range(len(strN)-k+1):
            N = int(strN[i:i+k])
            if  N != 0 and num%N==0:
                answer += 1
            
            
        
        return answer