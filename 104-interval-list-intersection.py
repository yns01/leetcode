from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        intersection = []

        ia, ib = 0, 0
        while ia < len(A) and ib < len(B):
            a_start, a_end = A[ia]
            b_start, b_end = B[ib]

            if max(a_start, b_start) <= min(a_end, b_end):
                intersection.append([max(a_start, b_start), min(a_end, b_end)])

                # if b_start <= a_start <= b_end:
                #    intersection.append(a_start, min(a_end, b_end)])
                # elif a_start <= b_start <= a_end:
                #    intersection.append([b_start, min(a_end, b_end)])

            if a_end < b_end:
                ia += 1
            else:
                ib += 1

        return intersection


print(Solution().intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
