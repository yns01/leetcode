from typing import List
from collections import Counter
import heapq


class Solution:
    def minMeetingRoomsv1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starting_times = sorted([i[0] for i in intervals])
        ending_times = sorted([i[1] for i in intervals])

        required_rooms, eti = 0, 0
        for st in starting_times:
            if st < ending_times[eti]:
                required_rooms += 1
            else:
                eti += 1

        return required_rooms

    def minMeetingRoomsv2(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        minheap = []
        heapq.heappush(minheap, sorted_intervals[0][1])

        for i in range(1, len(sorted_intervals)):
            current_meeting_start, current_meeting_end = sorted_intervals[i]

            if current_meeting_start < minheap[0]:
                heapq.heappush(minheap, current_meeting_end)
            else:
                heapq.heappop(minheap)
                heapq.heappush(minheap, current_meeting_end)

        return len(minheap)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starting_times, ending_times, min_starting_time, max_starting_time = Counter(), Counter(), 0, 0

        for interval in intervals:
            min_starting_time = min(min_starting_time, interval[0])
            # After the last starting time, meetings will start to end
            # and the number of required rooms to decline.
            max_starting_time = max(max_starting_time, interval[0])
            starting_times[interval[0]] += 1
            ending_times[interval[1]] += 1

        meeting_rooms_count,  needed_rooms = 0, 0
        for t in range(min_starting_time, max_starting_time+1):
            meeting_rooms_count += starting_times[t] - ending_times[t]
            needed_rooms = max(meeting_rooms_count, needed_rooms)

        return needed_rooms


print(Solution().minMeetingRoomsv2(
    [[1, 5], [8, 9], [8, 9]]))
