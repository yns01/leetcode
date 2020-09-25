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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def recurse(node: TreeNode, running_sum: int):
            if not node:
                return

            running_sum += node.val
            complement = running_sum - sum
            if complement in sum_counts:
                self.count += sum_counts[complement]

            if running_sum in sum_counts:
                sum_counts[running_sum] += 1
            else:
                sum_counts[running_sum] = 1

            recurse(node.left, running_sum)
            recurse(node.right, running_sum)

            sum_counts[running_sum] -= 1
            if sum_counts[running_sum] == 0:
                del sum_counts[running_sum]

        sum_counts = {0: 1}
        self.count = 0
        recurse(root, 0)
        return self.count


tree = TreeNode(10)
left = tree.insert_left(5)
right = tree.insert_right(-3)

ll = left.insert_left(3)
lr = left.insert_right(-7)

ll.insert_left(-10)
ll.insert_right(4)
print(Solution().pathSum(tree, 8))
