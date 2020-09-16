class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            left_char = s[l]
            right_char = s[r]

            if not left_char.isalnum():
                l += 1
            elif not right_char.isalnum():
                r -= 1
            elif left_char.lower() != right_char.lower():
                return False
            else:
                l += 1
                r -= 1

        return True


print(Solution().isPalindrome(' '))
print(Solution().isPalindrome('1p'))
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
