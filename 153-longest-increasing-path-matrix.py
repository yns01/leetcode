from typing import List
import math


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        # We don't a seen set as the path must be strictly increasing.
        # If we made progress towards a path, we will not be able to come back
        # to an already seen element as it will necessarily be smaller
        cache = {}
        longest_path = -math.inf
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(
                    longest_path, self.dfs(matrix, (i, j), cache))

        return longest_path

    def dfs(self, matrix, starting_point, cache):
        if starting_point in cache:
            return cache[starting_point]

        path_len = 0

        r, c = starting_point
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr = r + dy
            nc = c + dx

            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[r][c]:
                path_len = max(path_len, self.dfs(matrix, (nr, nc), cache))

        cache[starting_point] = path_len + 1

        return path_len + 1


print(Solution().longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))
