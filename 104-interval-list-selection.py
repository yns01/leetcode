from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        a_intervals = A
        b_intervals = B

        ia, ib = 0, 0
        res = []

        while ia < len(a_intervals) and ib < len(b_intervals):
            interval_a, interval_b = a_intervals[ia], b_intervals[ib]

            overlap = []
            '''


            if interval_b[0] <= interval_a[0] <= interval_b[1]:
                overlap.append(interval_a[0])
                overlap.append(min(interval_a[1], interval_b[1]))
            elif interval_a[0] <= interval_b[0] <= interval_a[1]:
                overlap.append(interval_b[0])
                overlap.append(min(interval_a[1], interval_b[1]))
            '''

            if max(interval_a[0], interval_b[0]) <= min(interval_a[1], interval_b[1]):
                overlap.append(max(interval_a[0], interval_b[0]))
                overlap.append(min(interval_a[1], interval_b[1]))

            if interval_a[1] < interval_b[1]:
                ia += 1
            else:
                ib += 1

            if overlap:
                res.append(overlap)

        return res


print(Solution().intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
