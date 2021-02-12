from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que, result = deque(), []

        for i, n in enumerate(nums):
            # Keep a monotonic decreasing queue.
            while que and nums[que[-1]] <= n:
                que.pop()

            # We append the INDEX of the value to know whenever we need to
            # eject elements
            que.append(i)

            # If the oldest element we have is not in window, remove it.
            # [0,1,2,3], k = 3, i = 3
            if que[0] == i - k:
                que.popleft()

            # if we processed more than at least k elements, we can push
            # a new max
            if i + 1 >= k:
                result.append(nums[que[0]])

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
