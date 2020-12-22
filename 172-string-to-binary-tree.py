class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None

        def recurse(s, start, end, bracket_indexes):
            if end < start:
                return None

            i = start
            while i <= end and (s[i].isdigit() or s[i] == '-'):
                i += 1

            root = TreeNode(int(s[start:i]))

            if i < end:
                left_start, left_end = i+1, bracket_indexes[i]
                root.left = recurse(s, left_start, left_end, bracket_indexes)
                i = left_end + 1

            if i < end:
                right_start, right_end = i+1, bracket_indexes[i]
                root.right = recurse(
                    s, right_start, right_end, bracket_indexes)

            return root

        return recurse(s, 0, len(s) - 1, self.build_bracket_index(s))

    def build_bracket_index(self, s):
        bracket_indexes = {}
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                bracket_indexes[stack.pop()] = i

        return bracket_indexes


print(Solution().str2tree("4(2(3)(1))(6(5))").val)
print(Solution().str2tree("-51(232)(434)").val)
