from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, nums_index, path):
            res.append(path)

            for i in range(nums_index, len(nums)):
                dfs(nums, i+1, path+[nums[i]])

            return None

        res = []
        if not nums:
            return res

        dfs(nums, 0, [])
        return res


print(Solution().subsets([1, 2, 3, ]))
