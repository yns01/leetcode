class Solution:
    def letterCombinations(self, digits):
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(digits, combinations):
            if not digits:
                res.append(combinations)
                return

            for l in digit_to_letters[digits[0]]:
                backtrack(digits[1:], combinations+l)

            return None

        res = []
        if not digits:
            return res

        backtrack(digits, '')
        return res


print(Solution().letterCombinations('29'))
