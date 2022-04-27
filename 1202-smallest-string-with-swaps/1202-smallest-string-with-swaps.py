class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        from collections import defaultdict
        d = defaultdict(list)
        s = list(s)
        visited = [False for _ in range(len(s))]

        for source, destination in pairs:
            d[source].append(destination)
            d[destination].append(source)

        def dfs(s, i, chars, indices):
            if visited[i]:
                return
            chars.append(s[i])
            indices.append(i)
            visited[i] = True

            for neigh in d[i]:
                dfs(s, neigh, chars, indices)

        for i in range(len(s)):
            if not visited[i]:
                chars = []
                indices = []

                dfs(s, i, chars, indices)
                chars = sorted(chars)
                indices = sorted(indices)
                for c, i in zip(chars, indices):
                    s[i] = c

        return "".join(s)