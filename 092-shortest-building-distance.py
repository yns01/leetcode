from typing import List
from collections import deque, Counter
import math


class Solution:
    def shortestDistance(self, grid):
        if not grid:
            return -1

        grid_rows = len(grid)
        grid_cols = len(grid[0])

        # For each point, we will compute the distance to each building.
        distances = Counter()
        # From each point, how many buildings are we able to reach?
        reachable_buildings = Counter()
        total_buildings = 0

        # General idea:
        # We will compute the distance from each building to each of the empty spots.
        # To do so, we start a BFS at each building.
        # The BFS will expand to all reachable empty lands. For each new land we have not visited, we
        # keep track of the total distance from that building and add it to the cumulative sum.
        # In other words, starting a BFS from point A to empty spot B, will add n distance. From
        # a second building, we will add m to it.
        # Once the traversal is done, each point will hold the total distance to reach all the buildings.
        # We also keep track of how many buildings are reachable from an empty spot.
        # Indeed, some building may not be reachable from that spot and are not eligible to a shortest distance

        # After each DFS, each point will hold its distance from the building which started the DFS
        # Reach will be incremented by one for each empty spot we could reach from that building.

        for gr in range(grid_rows):
            for gc in range(grid_cols):
                if grid[gr][gc] == 1:
                    total_buildings += 1
                    self.BFS(grid, distances, reachable_buildings, gr, gc)

        min_distance = math.inf
        for gr in range(grid_rows):
            for gc in range(grid_cols):
                if grid[gr][gc] == 0 and reachable_buildings[(gr, gc)] == total_buildings:
                    min_distance = min(min_distance, distances[(gr, gc)])

        return min_distance if min_distance != math.inf else -1

    def BFS(self, grid, distances, reachable_buildings, row_start, col_start):
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        visited = set()
        que = deque([(row_start, col_start, 0)])

        while que:
            current_row, current_col, current_distance = que.popleft()

            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                next_row = current_row + dy
                next_col = current_col + dx

                next_point = (next_row, next_col)

                if (0 <= next_row < grid_rows and 0 <= next_col < grid_cols and
                        grid[next_row][next_col] == 0 and
                        next_point not in visited):

                    visited.add(next_point)
                    distances[next_point] += current_distance + 1
                    reachable_buildings[next_point] += 1

                    que.append((next_row, next_col, current_distance+1))


print(Solution().shortestDistance(
    [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
