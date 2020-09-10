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

        serial = []
        nodes = deque()
        nodes.append(root)

        while nodes:
            level_nodes = []
            at_least_one_node_in_level = False

            for _ in range(len(nodes)):
                n = nodes.popleft()
                level_nodes.append(n.val if n else None)

                if n:
                    at_least_one_node_in_level = True
                    nodes.append(n.left)
                    nodes.append(n.right)

            if at_least_one_node_in_level:
                serial.extend(level_nodes)

        serialized = ''
        for n in serial:
            serialized += str(n) + ','

        return serialized[:-1]

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        serialized_nodes = data.split(',')
        root = TreeNode(int(serialized_nodes[0]))
        que = deque()
        que.append(root)

        serial_index = 1
        while que and serial_index < len(serialized_nodes):
            n = que.popleft()

            if n:
                v = serialized_nodes[serial_index]
                serial_index += 1
                if v != 'None':
                    n.left = TreeNode(int(v))
                    que.append(n.left)

                v = serialized_nodes[serial_index]
                serial_index += 1
                if v != 'None':
                    n.right = TreeNode(int(v))
                    que.append(n.right)

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
