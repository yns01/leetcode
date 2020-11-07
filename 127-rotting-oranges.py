from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        que = deque()
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    que.append((i, j))

        minutes = 0
        at_least_one_rotten = False

        while que:
            for _ in range(len(que)):
                r, c = que.popleft()

                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_row = r + dy
                    new_col = c + dx

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        que.append((new_row, new_col))
                        at_least_one_rotten = True
                        fresh_count -= 1

            if at_least_one_rotten:
                minutes += 1

            at_least_one_rotten = False

        return minutes if not fresh_count else -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
