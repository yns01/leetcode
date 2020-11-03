from typing import List
import heapq
import random


class Solution:
    def findKthLargestv1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)

        return h[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        left, right, kth = 0, len(nums) - 1, None

        while True:
            kth = self.partition(nums, left, right)
            if kth == (len(nums) - k):
                return nums[kth]
            elif kth > (len(nums) - k):
                right = kth - 1
            else:
                left = kth + 1

        return -1

    def partition(self, nums: List[int], left: int, right: int) -> int:
        rand = random.randint(left, right)
        nums[rand], nums[right] = nums[right], nums[rand]

        pivot = nums[right]

        frontier = left
        while left < right:
            if nums[left] < pivot:
                nums[frontier], nums[left] = nums[left], nums[frontier]
                frontier += 1

            left += 1

        nums[right], nums[frontier] = nums[frontier], nums[right]

        return frontier


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 1))
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
