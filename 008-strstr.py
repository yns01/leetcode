class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break

                if j == len(needle) - 1:
                    return i

        return -1


s = Solution()
print(s.strStr("hello", 'll'))
print(s.strStr("helllok", 'lok'))
print(s.strStr("helllokl", 'lok'))
print(s.strStr("lolok", 'lok'))
print(s.strStr("lolo", 'lok'))
print(s.strStr("lo", 'lok'))
print(s.strStr("mississippi", 'issip'))
