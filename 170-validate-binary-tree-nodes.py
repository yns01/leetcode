from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        seen = set()

        # There are several types of cycles:

        # Simple cycles are present in a tree when the graph is presented as an edge list
        # and thus in an undirected graph. To validate a tree, we have to of course check cycles,
        # but ignore simple cycles.
        # To do so, we skip the cycle if its points to the parent node. If we already saw the node
        # we have a cycle.

        # Cycles in directed graphs.
        # When performing a topological sort, we need to take care of cycles.
        #     A <- D    There is no cycle, but it's not a valid tree. So we just have to make sure we see
        #   /  \        each node only once.
        # B<    >C

        #     A <-   D    We cannot sort this graph as there's a cycle.
        #   /  \    /
        # B<    >C >

        # In this problem, the root might not be zero. In fact, since this is an undirected graph,
        # not all nodes might be reachable from 0.
        # There are two ways to proceed.

        # A. We find the root (as it's the only node from which we can reach all nodes)
        # The root is the only node which should not be in the children arrays. From there, we DFS the graph
        # and make sure we don't see the same node twice.

        # B. We transform the directed graph in an undirected graph. In an undirected graph,
        # we can reach every node from every node. From there, we DFS the graph and make sure we don't see the same
        # node twice unless it's a parent (simple cycles).

        def dfs(node):
            if node == -1:
                return False

            seen.add(node)

            left = leftChild[node]
            right = rightChild[node]

            for nei in [left, right]:
                if nei in seen:
                    return True

                cycle = dfs(nei)
                if cycle:
                    return True

            return False

        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i in children:
                continue

            root = i
            break

        has_cycle = dfs(root)
        if has_cycle:
            return False

        if len(seen) != n:
            return False

        return True


print(Solution().validateBinaryTreeNodes(4,
                                         [1, -1, 3, -1],
                                         [-1, -1, -1, 2]))
print(Solution().validateBinaryTreeNodes(4,
                                         [1, -1, 3, -1],
                                         [2, -1, -1, -1]))
