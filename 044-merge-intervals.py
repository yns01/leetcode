from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Merge meeting ranges based on their starting times
        intervals = sorted(intervals, key=lambda interval: interval[0])

        merged_intervals = []
        prev_interval = intervals[0]

        for i in range(1, len(intervals)):
            current_interval_start, current_interval_end = intervals[i]
            prev_interval_start, prev_interval_end = prev_interval

            if prev_interval_end >= current_interval_start:
                prev_interval = [prev_interval_start,
                                 max(prev_interval_end, current_interval_end)]

            else:
                merged_intervals.append(prev_interval)
                prev_interval = intervals[i]

        merged_intervals.append(prev_interval)

        return merged_intervals


print(Solution().merge([[1, 4], [0, 0]]))
