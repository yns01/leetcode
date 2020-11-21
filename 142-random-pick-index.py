import random
from typing import List
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.index = defaultdict(list)
        for i, n in enumerate(nums):
            self.index[n].append(i)

    def pick(self, target: int) -> int:
        indexes = self.index.get(target)
        return indexes[random.randint(0, len(indexes)-1)]

    def pickv1(self, target: int) -> int:
        # Reservoir sampling. Note that elements at the end of array have a lower probability of being chosen
        count, index = 0, 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1

                # Why count-1 ? it's because randint(a,b) includes b. Say we found the first occurrence, we want to the probability to be 1/1.
                # If we don't count-1, we would have a 50% chance as the possible values for the rand are 0 and 1.
                if random.randint(0, count-1) == 0:
                    index = i

        return index


obj = Solution([1, 2, 3, 3, 3])
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))
print("v1")
print(obj.pickv1(3))
print(obj.pickv1(3))
print(obj.pickv1(3))
