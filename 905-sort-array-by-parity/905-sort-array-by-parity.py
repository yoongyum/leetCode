class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        odd = []
        while nums:
            n = nums.pop()
            if n % 2==0:
                arr.append(n)
            else:
                odd.append(n)

        return arr+odd
                