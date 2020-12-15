class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: Node) -> int:
        def recurse(node):
            if not node:
                return 0

            max_1, max_2 = 0, 0
            for child in node.children:
                d = recurse(child)

                if max_1 < max_2:
                    max_1 = max(max_1, d)
                else:
                    max_2 = max(max_2, d)

            self.diameter = max(self.diameter, max_1 + max_2)

            return max(max_1, max_2) + 1

        self.diameter = 0
        recurse(root)
        return self.diameter
