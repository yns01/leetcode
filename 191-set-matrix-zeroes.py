from typing import List


class Solution:
    # SC: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        set_first_row, set_first_col = False, False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        set_first_row = True
                    if j == 0:
                        set_first_col = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if set_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if set_first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

    # SC O(m+n)
    def setZeroesv1(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


matrix = [[1, 0, 3]]
Solution().setZeroes(matrix)
print(matrix)
matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
Solution().setZeroes(matrix)
print(matrix)
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setZeroes(matrix)
print(matrix)
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(matrix)
print(matrix)

matrix = [[1, 0, 3]]
Solution().setZeroesv1(matrix)
print(matrix)
matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
Solution().setZeroesv1(matrix)
print(matrix)
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setZeroesv1(matrix)
print(matrix)
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroesv1(matrix)
print(matrix)
