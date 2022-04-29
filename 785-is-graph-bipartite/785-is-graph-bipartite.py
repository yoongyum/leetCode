class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for n in range(len(graph)):
            if n not in colors and not self.dfs(graph, n, colors, 1):
                return False

        return True

    def dfs(self, graph, node, colors, color):

        colors[node] = color

        for node_to in graph[node]:
            if node_to in colors:
                if colors[node_to] == colors[node]:
                    return False
            elif not self.dfs(graph, node_to, colors, color * -1):
                    return False

        return True