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


s = Solution()
print(s.strStr("hello", 'll'))
print(s.strStr("helllok", 'lok'))
print(s.strStr("helllokl", 'lok'))
print(s.strStr("lolok", 'lok'))
print(s.strStr("lolo", 'lok'))
print(s.strStr("lo", 'lok'))
print(s.strStr("mississippi", 'issip'))
