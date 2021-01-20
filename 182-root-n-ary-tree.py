from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List[Node]) -> Node:
        children = set()
        for node in tree:
            children.update(node.children)

        for node in tree:
            if node not in children:
                return node

        return None
