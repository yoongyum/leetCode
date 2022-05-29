class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxVal = 0
        
        for comb in combinations(words,2):
            for char in comb[0]:
                if char in comb[1]:
                    break
            else:
                maxVal = max(len(comb[0])*len(comb[1]),maxVal)
        return maxVal
        