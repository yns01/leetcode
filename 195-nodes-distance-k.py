from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def build_parents_map(node, parent):
            if not node:
                return

            self.parents[node] = parent
            build_parents_map(node.left, node)
            build_parents_map(node.right, node)

        def bfs():
            que, seen, distance = deque(), set(), 0

            que.append(target)
            seen.add(target)

            while que:
                level_nodes = []

                for _ in range(len(que)):
                    n = que.popleft()

                    level_nodes.append(n.val)

                    for nei in [n.left, n.right, self.parents[n]]:
                        if nei and nei not in seen:
                            que.append(nei)
                            seen.add(nei)

                if distance == K:
                    return level_nodes

                distance += 1

            return []

        if not root:
            return []

        self.parents = {}
        build_parents_map(root, None)
        return bfs()


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


root = (stringToTreeNode('[3,5,1,6,2,0,8,null,null,7,4]'))

print(Solution().distanceK(root, root.left, 2))
