class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        d = defaultdict(int)
        currSum = 0
        ans = 0
        for end in range(len(nums)):
            d[nums[end]] += 1
            currSum += nums[end]
            if d[nums[end]] != 1:
                while d[nums[end]] != 1:
                    d[nums[start]] -=1
                    if d[nums[start]] == 0:
                        del d[nums[start]]
                    currSum -= nums[start]
                    start+=1
            ans = max(ans,currSum)
        return ans
        