class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        haystack_cursor, needle_cursor, matching_position_start = 0, 0, -1

        while haystack_cursor < len(haystack):
            if needle_cursor == len(needle):
                return matching_position_start

            current_haystack_char = haystack[haystack_cursor]
            current_needle_char = needle[needle_cursor]

            if current_haystack_char == current_needle_char:
                if matching_position_start == -1:
                    matching_position_start = haystack_cursor

                needle_cursor += 1
                haystack_cursor += 1
            else:
                needle_cursor = 0

                if matching_position_start != -1:
                    haystack_cursor = matching_position_start + 1
                else:
                    haystack_cursor += 1

                matching_position_start = -1

        if needle_cursor == len(needle):
            return matching_position_start

        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(0, len(haystack)-len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


s = Solution()
print(s.strStr2("hello", 'll'))
print(s.strStr2("helllok", 'lok'))
print(s.strStr2("helllokl", 'lok'))
print(s.strStr2("lolok", 'lok'))
print(s.strStr2("lolo", 'lok'))
print(s.strStr2("lo", 'lok'))
print(s.strStr2("mississippi", 'issip'))
