class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k*(k+1)/2: return []
        answer = []
        
        def DFS(start, arr):
            if len(arr) == k and sum(arr) == n:
                answer.append(deepcopy(arr))
                return
            for i in range(start ,10):
                arr.append(i)
                DFS(i+1,arr)
                arr.pop()
        DFS(1,[])
        return answer
        