from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], paths: List[int]):
            if not nums and tuple(paths) not in seen:
                seen.add(tuple(paths))
                res.append(paths)
                return

            for i, n in enumerate(nums):
                backtrack(nums[:i]+nums[i+1:], paths+[n])

        seen, res = set(), []
        if not nums:
            return res

        backtrack(nums, [])
        return res


print(Solution().permuteUnique([1, 1, 3]))
