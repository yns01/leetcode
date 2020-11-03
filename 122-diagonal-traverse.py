from typing import List
from collections import defaultdict, deque


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        diags = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_point = matrix[i][j]
                diags[i+j].append(current_point)

        output = []
        for i in range(len(diags)):
            if i % 2 == 0:
                output.extend(list(reversed(diags[i])))
            else:
                output.extend(diags[i])

        return output

    def findDiagonalOrderv1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None

        diags = []
        total_rows = len(matrix)
        total_cols = len(matrix[0])
        # Start at all possible diagonals. Subtract one to avoid starting twice
        # at the top right corner.
        for d in range(total_rows + total_cols - 1):
            row, col = 0, 0
            if d < total_cols:
                row, col = 0, d
            else:
                # if we're done if the part of diagonals, we're now going from top right to bottom right
                # In that case, we must substract the number of diagonals we aldready visited, and add one to not
                # endup on the top right (already visited)
                row = d - total_cols + 1
                col = total_cols - 1

            diag = []
            while row < len(matrix) and col >= 0:
                diag.append(matrix[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                diags.extend(list(reversed(diag)))
            else:
                diags.extend(diag)

        return diags


print(Solution().findDiagonalOrderv1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
