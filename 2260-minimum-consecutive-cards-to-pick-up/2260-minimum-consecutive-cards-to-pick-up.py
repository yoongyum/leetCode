class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = 100001
        arr = defaultdict(list)
        for i,card in enumerate(cards):
            arr[card].append(i)
            if len(arr[card]) > 1:
                ans = min( ans, abs(arr[card].pop(0)-i)+1)
            
        return -1 if ans == 100001 else ans