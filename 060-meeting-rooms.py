from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        sorted_intervals = sorted(intervals, key=lambda i: i[0])

        prev_meeting = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            _, prev_meeting_end = prev_meeting
            curr_meeting_start, _ = sorted_intervals[i]

            if prev_meeting_end > curr_meeting_start:
                return False

            prev_meeting = sorted_intervals[i]

        return True


print(Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(Solution().canAttendMeetings([[7, 10], [2, 4]]))
