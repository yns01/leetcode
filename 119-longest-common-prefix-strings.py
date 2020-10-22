from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        current_index = 0
        for c in strs[0]:
            for i in range(1, len(strs)):
                s = strs[i]
                if current_index >= len(s) or s[current_index] != c:
                    return s[:current_index]

            current_index += 1

        # If we reach this point, it means that all the strings are equals
        # We just return one of them.
        return strs[0]


print(Solution().longestCommonPrefix(['apple', 'app', 'ape']))
