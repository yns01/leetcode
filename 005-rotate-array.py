from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return None

        n = len(nums)
        rotated = [0] * n
        for i in range(n):
            rotated[(i+k) % n] = nums[i]

        nums[:] = rotated


input = [11, 13, 1, 9, 5, 0, 2]
[11, 13, 1, 9, 5, 0, 2]

k = 3
s = Solution()
s.rotate(input, k)
print(input)

input = [-1, -100, 3, 99]
k = 2
s.rotate(input, k)
print(input)
