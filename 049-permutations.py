from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], path: List[int]):
            if not nums:
                res.append(path)

            for i, n in enumerate(nums):
                backtrack(nums[:i] + nums[i+1:], path+[n])

        res = []
        if not nums:
            return res

        backtrack(nums, [])
        return res

    def permute_string(self, string: str) -> [str]:

        def backtrack(suffix: str, prefix: str):
            if not suffix:
                res.append(prefix)

            for i, s in enumerate(suffix):
                backtrack(suffix[:i]+suffix[i+1:], prefix+s)

        res = []
        if not string:
            return res

        backtrack(string, '')
        return res


print(Solution().permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(Solution().permute_string('abc'))
