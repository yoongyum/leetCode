class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = []
        keyword = ""
        for i in range(1,len(searchWord)+1):
            save = []
            for p in products:
                if p.startswith(searchWord[:i]):
                    save.append(p)
                    
            save.sort() #사전순으로 정렬
            answer.append(save[:3])
            
        return answer