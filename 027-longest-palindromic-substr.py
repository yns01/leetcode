class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        longest_palindrome = ''
        for i in range(0, len(s)):
            palindrome_without_odd_char = self.get_palindrome(s, i, i+1)
            palindrome_with_odd_char = self.get_palindrome(s, i, i)
            longest_palindrome = max(
                palindrome_with_odd_char,
                palindrome_without_odd_char,
                longest_palindrome,
                key=len)

        return longest_palindrome

    def get_palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]


print(Solution().longestPalindrome("ababb"))
