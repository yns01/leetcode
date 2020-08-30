from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0

        tail_cursor, front_cursor, longest_substr, distinct_chars = 0, 0, 0, {}

        while tail_cursor < len(s) and front_cursor < len(s):
            current_char = s[front_cursor]
            if current_char in distinct_chars or len(distinct_chars) < 2:
                if not current_char in distinct_chars:
                    distinct_chars[current_char] = 1
                else:
                    distinct_chars[current_char] += 1

                front_cursor += 1

                longest_substr = max(
                    longest_substr,
                    front_cursor - tail_cursor)

            else:
                count = distinct_chars[s[tail_cursor]]
                if count == 1:
                    del distinct_chars[s[tail_cursor]]
                else:
                    distinct_chars[s[tail_cursor]] -= 1

                tail_cursor += 1

        return longest_substr


print(Solution().lengthOfLongestSubstringTwoDistinct('ccaabbb'))
print(Solution().lengthOfLongestSubstringTwoDistinct('abaccc'))
print(Solution().lengthOfLongestSubstringTwoDistinct('ccaabbb'))
