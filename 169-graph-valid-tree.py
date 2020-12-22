from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        nodes = {i: [] for i in range(n)}

        for e1, e2 in edges:
            nodes[e1].append(e2)
            nodes[e2].append(e1)

        seen = set()

        def dfs(node, parent):
            seen.add(node)

            for nei in nodes[node]:
                if nei == parent:
                    continue

                if nei in seen:
                    return True

                has_cycle = dfs(nei, node)
                if has_cycle:
                    return True

            return False

        # If there's a cycle, it's not a valid tree
        if dfs(0, None):
            return False

        # If it's a connected graph, we should have seen all the nodes
        if len(seen) != n:
            return False

        return True


print(Solution().validTree(5,       [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution().validTree(5,       [[0, 1], [0, 2], [0, 3], [1, 4]]))
