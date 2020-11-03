import heapq
from typing import List
import random


class Solution:
    def kClosestv1(self, points: List[List[int]], K: int) -> List[List[int]]:
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

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not K or not points:
            return []

        left, right = 0, len(points) - 1
        while True:
            kth = self.partition(points, left, right)
            if kth == K - 1:
                return points[:K]
            elif kth > K - 1:
                right = kth - 1
            else:
                left = kth + 1

        return - 1

    def get_distance_to_origin(self, p):
        x, y = p
        return x**2 + y**2

    def partition(self, points, left, right):
        rand = random.randint(left, right)
        points[right], points[rand] = points[rand], points[right]

        frontier = left
        pivot = points[right]

        while left < right:
            if self.get_distance_to_origin(points[left]) < self.get_distance_to_origin(pivot):
                points[frontier], points[left] = points[left], points[frontier]
                frontier += 1

            left += 1

        points[frontier], points[right] = points[right], points[frontier]

        return frontier


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
