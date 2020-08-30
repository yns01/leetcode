class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0

        max_len, tail_cursor, head_cursor, char_counts = 0, 0, 0, {}
        while tail_cursor < len(s) and head_cursor < len(s):
            current_head_char = s[head_cursor]

            if current_head_char in char_counts or len(char_counts) < k:
                if current_head_char in char_counts:
                    char_counts[current_head_char] += 1
                else:
                    char_counts[current_head_char] = 1

                head_cursor += 1
                max_len = max(max_len, head_cursor - tail_cursor)
            else:
                current_tail_char = s[tail_cursor]
                char_counts[current_tail_char] -= 1

                if char_counts[current_tail_char] == 0:
                    del char_counts[current_tail_char]

                tail_cursor += 1

        return max_len


print(Solution().lengthOfLongestSubstringKDistinct('aa', 1))
print(Solution().lengthOfLongestSubstringKDistinct('eceba', 2))
print(Solution().lengthOfLongestSubstringKDistinct('eceba', 0))
