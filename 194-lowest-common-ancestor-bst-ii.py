class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


# Returns the LCA in a bst or None if one or both of the nodes are not in the bst
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(node):
            if not node:
                return

            if node is p or node is q:
                self.count += 1
                if find(node, p if node is q else q):
                    self.count += 1

                return node

            if min(p.val, q.val) < node.val < max(p.val, q.val):
                if find(node, q):
                    self.count += 1

                if find(node, p):
                    self.count += 1

                return node
            elif p.val < node.val:
                return recurse(node.left)
            else:
                return recurse(node.right)

        def find(node, target):
            if not node:
                return False

            if node is target:
                return True

            if node.val > target.val:
                return find(node.left, target)
            else:
                return find(node.right, target)

        if not p or not q:
            return None

        self.count = 0
        lca = recurse(root)
        return lca if self.count == 2 else None


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
ll = left.insert_left(10)
lr = left.insert_right(40)
# right.insert_left(60)
# right.insert_right(80)

print(Solution().lowestCommonAncestor(tree, ll, lr).val)  # 30
print(Solution().lowestCommonAncestor(tree, None, lr))  # None
print(Solution().lowestCommonAncestor(tree, right, TreeNode(10000)))  # None
print(Solution().lowestCommonAncestor(tree, TreeNode(10000), left))  # None
print(Solution().lowestCommonAncestor(tree, TreeNode(0), lr))  # None
