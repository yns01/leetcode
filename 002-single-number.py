from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None

        values = set()

        for n in nums:
            if n not in values:
                values.add(n)
            else:
                values.remove(n)

        for e in values:
            return e

        return None


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
