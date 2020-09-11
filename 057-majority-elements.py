import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for n in nums:
            c = counts.get(n, 0) + 1
            if c >= len(nums)/2:
                return n

            counts[n] = c

        return -1

    def majorityElementVotingAlgorithm(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            n = nums[i]
            if n == candidate:
                count += 1
            else:
                count -= 1

            if count == 0:
                count = 1
                candidate = n

        # In this case, the problem states that there's always a majority element.
        # However, if it's not the case, we have to count the occurrences of the candidate
        # and ensure its >= len(nums) /2
        return candidate


print(Solution().majorityElementVotingAlgorithm([1, 6, 3, 1, 1, 1, 4, 1]))
