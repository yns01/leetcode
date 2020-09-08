from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for m in matrix:
            if not m:
                return False

        # find first row for which: row_start <= target <= row_end
        first_row = self.find_row_index(matrix, target, True)

        # find last row for which: row_start <= target <= row_end
        last_row = self.find_row_index(matrix, target, False)
        print(first_row, last_row)

        # apply BS on each row
        for i in range(first_row, last_row + 1):
            found = self.binary_search(matrix[i], target)
            if found:
                return True

        return False

    def find_row_index(self, matrix: List[List[int]], target: int, first: bool):
        row_len, row_index = len(matrix[0]), -1
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if matrix[mid][0] <= target <= matrix[mid][row_len-1]:
                row_index = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        return row_index

    def binary_search(self, nums: List[int], target: int):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrixV2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for m in matrix:
            if not m:
                return False

        row, col = 0, len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False


matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(Solution().searchMatrixV2(matrix, 18))
print(Solution().searchMatrix([[], [1]], 99))
