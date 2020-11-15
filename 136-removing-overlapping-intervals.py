from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        if not toBeRemoved:
            return intervals

        i, result = 0, []
        while i < len(intervals):
            ci_start, ci_end = intervals[i]
            rm_start, rm_end = toBeRemoved

            # No overlap cases
            if ci_end <= rm_start or rm_end <= ci_start:
                result.append([ci_start, ci_end])

            # Interval to remove is bigger than the current interval
            elif rm_start <= ci_start and ci_end <= rm_end:
                pass

            # At this point, there must be an overlap between to compared intervals
            # Current interval includes the interval to remove
            elif ci_start < rm_start and ci_end > rm_end:
                result.append([ci_start, rm_start])
                result.append([rm_end, ci_end])

            # Interval to remove overlaps with current interval and starts after the current one
            elif ci_start < rm_start:
                result.append([ci_start, rm_start])

            # Interval to remove overlaps with current interval and starts before the current one
            elif ci_start < rm_end:
                result.append([rm_end, ci_end])

            i += 1

        return result


print(Solution().removeInterval([[0, 2], [3, 4], [5, 7]], [1, 6]))
print(Solution().removeInterval([[0, 5]], [2, 3]))
print(Solution().removeInterval(
    [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]))
