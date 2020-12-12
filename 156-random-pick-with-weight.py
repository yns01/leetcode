from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        # To pick randomly an index we can build an array where each element is repeated
        # as many times as their weight.
        # For example w = [1,4,3]
        # [0,1,1,1,1,2,2,2]. Then we just pick one number.
        # While this works the SC would be very bad if one weight would be 2e9
        # Instead, we use prefix sums:
        # w = [1,3,2,5,1]
        # sums = [1,4,6,12]. From there we generate a random number
        # and we find the first bigger element.
        self.sums = []

        running_sum = 0
        for weight in w:
            running_sum += weight
            self.sums.append(running_sum)

    def pickIndex(self) -> int:
        upper_random_boundary = self.sums[-1]
        random_val = random.randrange(1, upper_random_boundary + 1)

        left, right = 0, len(self.sums) - 1
        index = -1
        while left <= right:
            mid = (right - left) // 2 + left

            if self.sums[mid] == random_val:
                return mid

            if self.sums[mid] >= random_val:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index


s = Solution([1, 3, 2, 5, 1])
print(s.pickIndex())
