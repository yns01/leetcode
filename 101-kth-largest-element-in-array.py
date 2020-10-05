from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            elif n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, n)

        return h[0]


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
