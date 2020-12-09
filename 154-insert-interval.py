from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval[:]]

        intervals_to_merge, index = [], 0
        while index < len(intervals) and newInterval[0] > intervals[index][0]:
            intervals_to_merge.append(intervals[index])
            index += 1
        else:
            intervals_to_merge.append(newInterval)

        if index < len(intervals):
            intervals_to_merge.extend(intervals[index:])

        prev = intervals_to_merge[0]
        result = []
        for i in range(1, len(intervals_to_merge)):
            current_interval = intervals_to_merge[i]

            if current_interval[0] <= prev[1]:
                prev = [prev[0], max(prev[1], current_interval[1])]
            else:
                result.append(prev)
                prev = current_interval

        result.append(prev)

        return result


print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
