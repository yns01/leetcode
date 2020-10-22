from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        de = set(deadends)

        if start in de:
            return -1

        que = deque([(start, 0)])
        visited = set([start])
        while que:
            c, d = que.popleft()
            if c == target:
                return d

            for n in self.neighbors(c):
                if n not in visited and n not in de:
                    que.append((n, d + 1))
                    visited.add(n)

        return -1

    def neighbors(self, node):
        neighbors = []
        for i, c in enumerate(node):
            for next in (-1, +1):
                neighbors.append(
                    node[:i] + str((int(c) + next) % 10) + node[i+1:])

        return neighbors


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], '0202'))
