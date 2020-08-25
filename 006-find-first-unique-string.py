class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        char_count = {}

        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        for index, c in enumerate(s):
            count = char_count.get(c)
            if count == 1:
                return index

        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("lldd"))
