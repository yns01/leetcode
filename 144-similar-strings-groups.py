from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not strs:
            return 0

        # We need to have a look at all the possible pairs and try to connect them
        # Then we apply a DFS to find the number of connected components
        # Similar to Accounts merge problem
        graph = {v: [] for v in strs}
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                w1, w2 = strs[i], strs[j]

                if self.are_similar(w1, w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)

        visited = set()
        result = 0
        for vertex in graph:
            if vertex not in visited:
                result += 1
                self.dfs(graph, vertex, visited)

        return result

    def dfs(self, graph, vertex, visited):
        visited.add(vertex)

        for nei in graph[vertex]:
            if nei not in visited:
                self.dfs(graph, nei, visited)

    def are_similar(self, word1, word2):
        if word1 == word2:
            return True

        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1

            if diff_count > 2:
                return False

        return True


print(Solution().numSimilarGroups(["blw", "bwl", "wlb"]))
print(Solution().numSimilarGroups(["tars", "rats", "arts", "star"]))
