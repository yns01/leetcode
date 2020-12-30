from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def recurse(node, chars):
            if not node:
                return

            chars[node.val] += 1

            recurse(node.left, chars)
            recurse(node.right, chars)

            if not node.left and not node.right and self.is_pseudo_palindrome(chars):
                self.count += 1

            chars[node.val] -= 1

        self.count = 0
        chars = Counter()
        recurse(root, chars)
        return self.count

    def is_pseudo_palindrome(self, chars):
        found_odd = False

        for _, v in chars.items():
            if v % 2 == 1:
                if found_odd:
                    return False

                found_odd = True

        return True


root = TreeNode(2)
left = root.insert_left(3)
left.insert_left(3)
left.insert_right(1)

right = root.insert_right(1)
right.insert_right(1)

print(Solution().pseudoPalindromicPaths(root))
