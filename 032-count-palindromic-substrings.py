class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        for i in range(len(s)):
            c1 = self.get_palindromes(s, i, i)
            c2 = self.get_palindromes(s, i, i+1)

            count += c1
            count += c2

        return count

    def get_palindromes(self, s: str, left: int, right: int):
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        return count


print(Solution().countSubstrings('abc'))
