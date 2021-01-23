from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0

        window_start, max_len, char_counts = 0, 0, Counter()
        for window_end in range(len(s)):
            current_char = s[window_end]

            char_counts[current_char] += 1

            while len(char_counts) > k:
                window_start_char = s[window_start]
                char_counts[window_start_char] -= 1

                if char_counts[window_start_char] == 0:
                    del char_counts[window_start_char]

                window_start += 1

            max_len = max(max_len, (window_end - window_start + 1))

        return max_len


print(Solution().lengthOfLongestSubstringKDistinct('aa', 1))
print(Solution().lengthOfLongestSubstringKDistinct('eceba', 2))
