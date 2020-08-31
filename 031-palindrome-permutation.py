class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return True

        char_count = set()
        for c in s:
            if not c in char_count:
                char_count.add(c)
            else:
                char_count.remove(c)

        return len(char_count) <= 1


print(Solution().canPermutePalindrome('careeracd'))
