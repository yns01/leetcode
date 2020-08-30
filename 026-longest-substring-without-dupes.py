class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:
        if not input_string:
            return 0

        max_len,  head_cursor, tail_cursor, sub_str_chars = 0, 0, 0, set()

        while tail_cursor < len(input_string) and head_cursor < len(input_string):
            current_char = input_string[head_cursor]

            if current_char not in sub_str_chars:
                sub_str_chars.add(current_char)
                head_cursor += 1
                max_len = max(max_len, head_cursor - tail_cursor)
            else:
                sub_str_chars.remove(input_string[tail_cursor])
                tail_cursor += 1

        return max_len

    def lengthOfLongestSubstring2(self, input_string: str) -> int:
        if not input_string:
            return 0

        max_len,  window_start, sub_str_chars = 0, 0, set()

        for window_end in range(len(input_string)):
            current_char = input_string[window_end]

            while current_char in sub_str_chars:
                sub_str_chars.remove(input_string[window_start])
                window_start += 1

            sub_str_chars.add(current_char)
            max_len = max(max_len, window_end - window_start + 1)

        return max_len


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring('aab'))
print(Solution().lengthOfLongestSubstring('dvdf'))

print(Solution().lengthOfLongestSubstring2('abcabcbb'))
print(Solution().lengthOfLongestSubstring2('bbbbb'))
print(Solution().lengthOfLongestSubstring2('pwwkew'))
print(Solution().lengthOfLongestSubstring2('aab'))
print(Solution().lengthOfLongestSubstring2('dvdf'))
