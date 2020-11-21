import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return None

        heap = []

        for i in range(min(len(matrix), k)):
            heap.append((matrix[i][0], i, 0))

        heapq.heapify(heap)

        # Since the input is sorted, we use a min heap. After K pop operations, we have the Kth min
        ops = 0
        while ops < k:
            val, row, col = heapq.heappop(heap)
            if col != len(matrix) - 1:
                heapq.heappush(heap, (matrix[row][col+1], row, col + 1))

            ops += 1

        return val


# TC = X=min(K,N); X+K log(X)
# For similar problems where the input is not sorted, the TC will be K log(N)
print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
