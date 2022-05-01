class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last = dict()
        result = 10**6 + 1
        for i in range(len(cards)):
            if cards[i] in last:
                result = min(result, i - last[cards[i]] + 1);
            last[cards[i]] = i
        return -1 if result == 10**6 + 1 else result