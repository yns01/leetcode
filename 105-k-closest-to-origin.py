import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not K or not points:
            return []

        def get_distance(x, y):
            return x**2 + y**2

        heap = []

        for p in points:
            x, y = p
            if len(heap) < K:
                heapq.heappush(heap, (-1 * get_distance(x, y), x, y))
            else:
                heapq.heappushpop(heap, (-1 * get_distance(x, y), x, y))

        k_closest = []
        for _, x, y in heap:
            k_closest.append([x, y])

        return k_closest


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
