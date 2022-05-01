class Solution(object):
    def removeDigit(self, number, digit):
        answer= '0'
        for i in range(len(number)):
            if(number[i]==digit):
                if(answer < (number[:i]+number[i+1:])):
                    answer= number[:i]+number[i+1:]
        return answer