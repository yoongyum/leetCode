class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n, prodDict = len(arr), {num: [] for num in arr}
        sol, mod = [1] * n, 10 ** 9 + 7

        for i in range(n):
            for j in range(i, n):
                prod = arr[i] * arr[j]
                if prod > arr[-1]: break
                if prod in prodDict:
                    prodDict[prod].append((i, j))

        for i in range(n):
            for i1, i2 in prodDict.get(arr[i], []):
                sol[i] += sol[i1] * sol[i2] * (1 if i1 == i2 else 2) % mod

        return sum(sol) % mod
        