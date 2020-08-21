from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        values = {}

        for n in nums1:
            if n not in values:
                values[n] = 1
            else:
                values[n] += 1

        join = []
        for n in nums2:
            if n in values and values.get(n) > 0:
                join.append(n)
                values[n] -= 1
        return join


nums1 = [1, 2, 2, 2]
nums2 = [2, 2]
s = Solution()
print(s.intersect(nums1, nums2))
