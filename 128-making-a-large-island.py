from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        island_sizes = {}

        max_island_sz, island_id = 0, 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_point = (i, j)

                if grid[i][j] == 1:
                    island_sz = self.dfs(grid, current_point, island_id)
                    island_sizes[island_id] = island_sz
                    max_island_sz = max(max_island_sz, island_sz)
                    island_id += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 0:
                    # Start at one to count the water we're transforming in land.
                    connected_island_sz = 1
                    # Keep track of seen islands around the water we're exploring so we only count them once
                    seen_islands = set()
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        next_row = r + dx
                        next_col = c + dy

                        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                            island_id = grid[next_row][next_col]

                            # If the current point is not an island or we already counted it, we skip it.
                            if island_id == 0 or island_id in seen_islands:
                                continue

                            island_sz = island_sizes.get(island_id)
                            connected_island_sz += island_sz
                            seen_islands.add(island_id)

                    max_island_sz = max(max_island_sz, connected_island_sz)

        return max_island_sz

    def dfs(self, grid, point, island_id):

        def visit(point, island_id, island_sz):
            r, c = point

            island_sz += 1
            grid[r][c] = island_id

            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                next_row = r + dx
                next_col = c + dy
                np = (next_row, next_col)

                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == 1:
                    island_sz = visit(np, island_id, island_sz)

            return island_sz

        return visit(point, island_id, 0)


print(Solution().largestIsland([[1, 1], [1, 0]]))
