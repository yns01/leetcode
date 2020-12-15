from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        tree = {n: [] for n in range(len(edges) + 1)}

        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)

        def recurse(node, parent):
            max_1, max_2 = 0, 0
            for nei in tree.get(node):
                if nei == parent:
                    continue

                d = recurse(nei, node)
                if max_1 < max_2:
                    max_1 = max(max_1, d)
                else:
                    max_2 = max(max_2, d)

            self.diameter = max(self.diameter, max_1 + max_2)

            return max(max_1, max_2) + 1

        self.diameter = 0

        recurse(0, None)
        return self.diameter


print(Solution().treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
