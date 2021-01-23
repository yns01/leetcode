from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []

        window_chars, dict_p = Counter(), Counter(p)
        formed, required = 0, len(dict_p)

        window_start = 0
        res = []

        for window_end in range(len(s)):
            current_char = s[window_end]

            window_chars[current_char] += 1
            if current_char in dict_p and window_chars.get(current_char) == dict_p.get(current_char):
                formed += 1

            while formed == required:
                if (window_end - window_start + 1 == len(p)):
                    res.append(window_start)

                start_char = s[window_start]
                window_chars[start_char] -= 1
                if window_chars[start_char] == 0:
                    del window_chars[start_char]

                if start_char in dict_p and window_chars.get(start_char, 0) < dict_p.get(start_char):
                    formed -= 1

                window_start += 1

        return res


print(Solution().findAnagrams('eabcd', 'aab'))
print(Solution().findAnagrams("cbaebabacd", "abc"))
