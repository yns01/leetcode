from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_point = grid[i][j]
                if current_point == "1":
                    islands += 1
                    self.DFS(grid, i, j)

        return islands

    def DFS(self, grid, row, col):
        if grid[row][col] == "1":
            grid[row][col] = '0'

            if col - 1 >= 0:
                self.DFS(grid, row, col - 1)
            if col + 1 < len(grid[0]):
                self.DFS(grid, row, col + 1)
            if row - 1 >= 0:
                self.DFS(grid, row - 1, col)
            if row + 1 < len(grid):
                self.DFS(grid, row + 1, col)


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

Solution().numIslands(grid)
