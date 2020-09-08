from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(nums: List[int], paths: List[int]):
            if len(paths) == k:
                res.append(paths)
                return

            for i, n in enumerate(nums):
                backtrack(nums[i+1:], paths+[n])

        res = []
        if not n or not k:
            return res

        backtrack(list(range(1, n+1)), [])
        return res

    def combineV2(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, index, k, paths):
            if k == 0:
                res.append(paths)
                return

            for i in range(index, len(nums)):
                dfs(nums, i+1, k-1, paths+[nums[i]])

        res = []
        if not n or not k:
            return res

        dfs(list(range(1, n+1)), 0, k, [])
        return res


print(Solution().combine(4, 2))
print(Solution().combineV2(4, 2))
