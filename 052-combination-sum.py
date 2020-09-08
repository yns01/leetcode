from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates: List[int], candidate_index: int, selected_candidates: List[int], target: int):
            if target < 0:
                return

            if target == 0:
                res.append(selected_candidates)
                return

            for i in range(candidate_index, len(candidates)):
                t = target - candidates[i]

                backtrack(candidates, i, selected_candidates +
                          [candidates[i]], t)

        res = []
        if not candidates:
            return res

        backtrack(candidates, 0, [], target)
        return res

    def combinationSumv1(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates: List[int], candidate_index: int, selected_candidates: List[int], target: int):
            if target < 0:
                return

            if target == 0:
                res.append(selected_candidates)
                return

            if candidate_index >= len(candidates):
                return

            multiplier = target // candidates[candidate_index]
            for i in range(0, multiplier+1):
                t = target - i * candidates[candidate_index]

                backtrack(candidates, candidate_index + 1,
                          selected_candidates + ([candidates[candidate_index]] * i), t)

        res = []
        if not candidates:
            return res

        backtrack(candidates, 0, [], target)
        return res


print(Solution().combinationSum([2, 3, 4], 9))
