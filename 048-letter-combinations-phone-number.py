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

        def backtrack(digits, digit_index, combinations):
            if digit_index == len(digits):
                res.append(combinations)
                return

            for l in digit_to_letters[digits[digit_index]]:
                backtrack(digits, digit_index+1, combinations+l)

            return None

        res = []
        if not digits:
            return res

        backtrack(digits, 0, '')
        return res


print(Solution().letterCombinations('29'))
