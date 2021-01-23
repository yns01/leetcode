class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution:
    def maximum_sum_subtree(self, root: TreeNode):
        def recurse(node: TreeNode):
            if not node:
                return 0

            ls = recurse(node.left)
            rs = recurse(node.right)

            cs = ls + rs + node.val
            self.max_sum = max(self.max_sum, cs)

            return cs

        if not root:
            return 0

        self.max_sum = 0
        recurse(root)

        return self.max_sum


print(Solution().maximum_sum_subtree(stringToTreeNode("[1,-2,3,4,5,-6,2]")))
