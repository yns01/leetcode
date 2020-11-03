from typing import List

# https://leetcode.com/discuss/interview-question/124616/


def merge(intervals1: List[List[int]], intervals2: List[List[int]]):
    if not intervals1 or not intervals2:
        return intervals1 or intervals2

    merged = []
    i1, i2 = 0, 0

    if intervals1[0][0] < intervals2[0][0]:
        prev = intervals1[0]
        i1 += 1
    else:
        prev = intervals2[0]
        i2 += 1

    while i1 < len(intervals1) or i2 < len(intervals2):
        if i2 == len(intervals2) or intervals1[i1][0] <= intervals2[i2][0]:
            current = intervals1[i1]
            i1 += 1
        else:
            current = intervals2[i2]
            i2 += 1

        if prev[1] >= current[0]:
            prev = [prev[0], max(prev[1], current[1])]
        else:
            merged.append(prev)
            prev = current

    merged.append(prev)

    return merged


res = merge(
    [(1, 5), (10, 14),  (16, 18), (20, 24), (30, 38)
     ],
    [(2, 6), (8, 10), (11, 20)])

print(res)
