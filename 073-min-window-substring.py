from collections import Counter
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        # Tracks the characters in the window
        window_chars = Counter()
        # Used to provide O(1) lookups of a character in t
        t_map = Counter(t)

        # Required keep track of how many characters we need to be present in the window
        required = len(t_map)
        # Formed tracks if the current window is matching t. It matches t when the frequency of chars in the window
        # equals the frequency in s.
        formed = 0

        window_start = 0
        # Window size, window start, window end (inclusive)
        window_result = (math.inf, None, None)

        for window_end in range(len(s)):
            window_end_char = s[window_end]

            window_chars[window_end_char] += 1
            # If the current char is needed to form t, and we have already seen it as many times as required,
            # we can say we formed one more character
            if window_end_char in t_map and t_map.get(window_end_char) == window_chars.get(window_end_char):
                formed += 1

            while formed == required:
                window_size = window_end - window_start + 1
                if window_size < window_result[0]:
                    window_result = (window_size, window_start, window_end+1)

                window_start_char = s[window_start]
                window_chars[window_start_char] -= 1
                if window_chars[window_start_char] == 0:
                    del window_chars[window_start_char]

                # If window_start_char is needed to form t, we must check our current window to ensure we have window_start_char
                # at least as many times as t as it.
                # In other words, the frequency of window_start_char in our window must be equal or higher than it is in t.
                if window_start_char in t_map and t_map.get(window_start_char) > window_chars.get(window_start_char, 0):
                    formed -= 1

                window_start += 1

        return '' if window_result[0] == math.inf else s[window_result[1]:window_result[2]]


print(Solution().minWindow('aa', 'aa'))
