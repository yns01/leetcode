from typing import List


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if not dict or not s:
            return s

        # TC
        # n = len(s)
        # m = average len of dict word
        # O(n lg n)  + O(n+m) * len(dict). KMP allowes substring search in O(n+m)

        intervals = []

        for d in dict:
            pos = s.find(d)
            while pos != -1:
                intervals.append([pos, pos+len(d)-1])
                # we start searching from the last found pos + 1
                pos = s.find(d, pos+1)

        if not intervals:
            return s

        intervals = sorted(intervals, key=lambda interval: interval[0])

        prev = intervals[0]
        merged_intervals = []
        for i in range(1, len(intervals)):
            current_interval_start, current_interval_end = intervals[i]

            if current_interval_start <= prev[1] or (current_interval_start - prev[1]) == 1:
                prev = [prev[0], max(prev[1], current_interval_end)]
            else:
                merged_intervals.append(prev)
                prev = intervals[i]

        merged_intervals.append(prev)

        result = []
        OPENING_TAG = '<b>'
        CLOSING_TAG = '</b>'

        prev = 0
        for mi in merged_intervals:
            result.extend(s[prev:mi[0]])
            result.append(OPENING_TAG)
            result.extend(s[mi[0]:mi[1]+1])
            result.append(CLOSING_TAG)

            prev = mi[1]+1

        # Copy remaining elements
        result.extend(s[mi[1]+1:])

        return ''.join(result)

    def addBoldTagv1(self, s: str, dict: List[str]) -> str:
        if not s or not dict:
            return s

        # Keep a mapping of character index to mark as bold
        boldify = [False] * len(s)
        for word in dict:
            pos = s.find(word)
            while pos != -1:
                for i in range(pos, pos+len(word)):
                    boldify[i] = True

                pos = s.find(word, pos+1)

        OPENING_TAG = '<b>'
        CLOSING_TAG = '</b>'

        i, res = 0, []
        while i < len(s):
            if boldify[i]:
                res.append(OPENING_TAG)
                while i < len(s) and boldify[i]:
                    res.append(s[i])
                    i += 1

                res.append(CLOSING_TAG)
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)


print(Solution().addBoldTagv1("abcxyz123", ["abc", "123"]))
