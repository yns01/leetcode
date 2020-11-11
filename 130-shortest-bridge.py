from typing import List
from collections import deque
import math


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        island_one, colored = 5, False
        starting_points = []

        for i in range(len(A)):
            for j in range(len(A[0])):
                if not colored and A[i][j] == 1:
                    self.color_island(A, (i, j), island_one)
                    colored = True

                if colored and A[i][j] == 1:
                    starting_points.append([i, j])

        return self.shortest_path(A, starting_points, island_one)

    def color_island(self, grid, point, color):
        row, col = point
        grid[row][col] = color

        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr = row + dy
            nc = col + dx

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                self.color_island(grid, (nr, nc), color)

    def shortest_path(self, grid, points, to):
        visited = set()
        que = deque()

        for cr, cc in points:
            que.append((cr, cc, 0))

        while que:
            cr, cc, cd = que.popleft()

            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr = cr + dy
                nc = cc + dx

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == to:
                        return cd

                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        que.append((nr, nc, cd+1))

        return math.inf


print(Solution().shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
    1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
