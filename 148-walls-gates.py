from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i, j, 0))

        INF = 2147483647

        que = deque(gates)
        seen = set()
        while que:
            r, c, d = que.popleft()

            if rooms[r][c] == INF:
                rooms[r][c] = d

            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nr = r + dy
                nc = c + dx

                if 0 <= nr < len(rooms) and 0 <= nc < len(rooms[0]) and rooms[nr][nc] == INF and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    que.append((nr, nc, d+1))

        return None


input = [[2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]

Solution().wallsAndGates(input)
print(input)
