class Solution:
    def minDeletions(self, s: str) -> int:
        word_counts=[]
        count=0
        for freq in Counter(s).values():
            if freq not in word_counts:
                word_counts.append(freq)
            else:
                while(freq in word_counts):
                    freq-=1
                    count+=1
                if(freq!=0):
                    word_counts.append(freq)      
        return count