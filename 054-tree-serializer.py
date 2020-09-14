from collections import deque


class TreeNode(object):
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


def level_order_traversal(node: TreeNode):
    if not node:
        return None

    nodes = deque()
    nodes.append(node)

    while nodes:
        for _ in range(len(nodes)):
            n = nodes.popleft()
            print(str(n.val) + '->', end='')

            nodes.append(n.left) if n.left else None
            nodes.append(n.right) if n.right else None

        print('')

    return None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        serialization = []
        nodes = deque()
        nodes.append(root)

        while nodes:
            level_nodes = []
            at_least_one_node_in_level = False

            for _ in range(len(nodes)):
                n = nodes.popleft()

                if n:
                    at_least_one_node_in_level = True
                    level_nodes.append(n.val)
                    nodes.append(n.left)
                    nodes.append(n.right)
                else:
                    level_nodes.append(str(None))

            if at_least_one_node_in_level:
                serialization.extend(level_nodes)

        serialized = ','.join(map(str, serialization))
        return serialized

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return

        deserialized, deserialized_index = data.split(','), 0
        root = TreeNode(int(deserialized[deserialized_index]))
        deserialized_index += 1
        nodes = deque()
        nodes.append(root)

        while nodes and deserialized_index < len(deserialized):
            n = nodes.popleft()

            left = deserialized[deserialized_index]
            deserialized_index += 1
            if left != str(None):
                n.left = TreeNode(int(left))
                nodes.append(n.left)

            right = deserialized[deserialized_index]
            deserialized_index += 1
            if right != str(None):
                n.right = TreeNode(int(right))
                nodes.append(n.right)

        return root


tree = TreeNode(1)
left = tree.insert_left(2)
right = tree.insert_right(3)
left.insert_left(1)
left_right = left.insert_right(3)
left_right.insert_right(3).insert_left(2)
right.insert_left(4)
right.insert_right(5)

level_order_traversal(tree)

codec = Codec()
level_order_traversal(codec.deserialize(codec.serialize(tree)))

codec.deserialize(codec.serialize(None))
