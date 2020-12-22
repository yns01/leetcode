# https://leetcode.com/discuss/interview-question/980711/facebook-phone-counts-of-connected-islands/795656
# Given matrix with 0 as water and 1 as island, find the number of island in each distinct group of connected of island.
# If any island has another island in its proximity (all 8 adjacent vertex), then they are connected.

# [[0, 1, 0],
# [0, 0, 0],
# [0, 1, 0]]
# Ans: [1, 1], there are 2 chain of island with 1 island each

# [[0, 1, 0],
# [1, 0, 0],
# [0, 1, 0]]
# Ans [3] 1 chain of island with 3 island on it

# [[0, 1, 1],
# [0, 0, 0],
# [0, 1, 0]]
# Ans [2, 1] 2 chain of island and 2 island on first and 1 island on another.

class Solution:
    def connected_islands(self, grid):
        if not grid:
            return 0

        island_sizes, island_id = [], 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sz = self.dfs(grid, (i, j), island_id)
                    island_sizes.append(sz)
                    island_id += 1

        return island_sizes

    def dfs(self, grid, starting_point, island_id):
        r, c = starting_point
        grid[r][c] = island_id

        sz = 0

        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1):
            nr = r + dy
            nc = c + dx

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                sz += self.dfs(grid, (nr, nc), island_id)

        return sz + 1


count = Solution().connected_islands([[0, 1, 0], [0, 0, 0], [0, 1, 0]])
print(count)

count = Solution().connected_islands([[0, 1, 0], [1, 0, 0], [0, 1, 0]])
print(count)

count = Solution().connected_islands([[0, 1, 1], [0, 0, 0], [0, 1, 0]])
print(count)
