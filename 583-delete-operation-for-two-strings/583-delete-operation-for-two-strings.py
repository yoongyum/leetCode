class Solution(object):
    def minDistance(self, word1, word2):
        m=len(word1)
        n=len(word2)
        ans_val=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    ans_val[i][j]=ans_val[i-1][j-1]+1
                else:
                    ans_val[i][j]=max(ans_val[i-1][j],ans_val[i][j-1])
        val=m+n-(2*ans_val[m][n])
        return val
        