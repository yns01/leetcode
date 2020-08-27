from typing import List
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        self.initial = nums
        self.shuffled = list(self.initial)

    def reset(self) -> List[int]:
        self.shuffled = list(self.initial)
        return self.initial

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled)):
            random_index = randrange(i, len(self.shuffled))
            self.shuffled[i], self.shuffled[random_index] = self.shuffled[random_index], self.shuffled[i]
        return self.shuffled


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 5, 6]
obj = Solution(nums)
obj.reset()
param_2 = obj.shuffle()
print(param_2)
print(obj.initial)
param_2 = obj.shuffle()
print(param_2)
print(obj.initial)
