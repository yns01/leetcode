from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return

        seen = {node: Node(node.val)}
        que = deque()
        que.append(node)

        while que:
            n = que.popleft()
            # When dequeuing an element, we're sure we already cloned it
            # as it's a BFS and we start by creating the root
            for u in n.neighbors:
                if u not in seen:
                    que.append(u)
                    seen[u] = Node(u.val)

                seen[n].neighbors.append(seen[u])

        return seen[node]

    def cloneGraph_rec(self, node: Node) -> Node:
        def recurse(node: Node) -> Node:
            if not node:
                return None

            if node in seen:
                return seen[node]

            copy = Node(node.val)
            seen[node] = copy

            for u in node.neighbors:
                n = recurse(u)
                copy.neighbors.append(n)

            return copy

        seen = {}
        return recurse(node)

# [[2,4],[1,3],[2,4],[1,3]]


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.neighbors = [two, four]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [one, three]

Solution().cloneGraph_rec(one)
