from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s:
            return

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return

    def reverse_string_punctuation(self, s: List[str]) -> None:
        stack = []

        for c in s:
            if c.isalnum():
                stack.append(c)

        for i in range(len(s)):
            if s[i].isalnum():
                s[i] = stack.pop()


s = Solution()
input = ["h", "e", "l", "l", "o"]
s.reverseString(input)
print(input)

input = ["H", "a", "n", "n", "a", "h"]
s.reverseString(input)
print(input)

input = ['a', 'b', 'c']
s.reverseString(input)
print(input)


input = ['h', 'e', 'l', 'l', 'o', ',', ' ', 'world', '!']
s.reverse_string_punctuation(input)
print(input)

input = ['!', '!', '>', '?', '=']
s.reverse_string_punctuation(input)
print(input)
