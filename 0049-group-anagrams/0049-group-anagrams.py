class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedWords = defaultdict(list)
        
        for word in strs:
            groupedWords["".join(sorted(word))].append(word)
        
        result = []
        
        for valueSet in groupedWords.values():
            result.append(valueSet)
        
        return  result  