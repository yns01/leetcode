class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        dummy = Node(0)
        nodes = {}

        current_source = head
        prev_copy = dummy
        while current_source:
            # Copy node
            nxt = nodes.get(current_source, None)
            if not nxt:
                nxt = Node(current_source.val)
                nodes[current_source] = nxt

            # Copy random pointer
            random_source = current_source.random
            random_cpy = None
            if random_source:
                random_cpy = nodes.get(random_source, None)
                if not random_cpy:
                    random_cpy = Node(random_source.val)
                    nodes[random_source] = random_cpy

            # Link nodes
            nxt.random = random_cpy
            prev_copy.next = nxt

            # Move on to next node
            current_source = current_source.next
            prev_copy = prev_copy.next

        return dummy.next

    def copyRandomList_rec(self, head: Node) -> Node:
        def recurse(head: Node):
            if not head:
                return

            if head in seen:
                return seen[head]

            copy = Node(head.val)
            seen[head] = copy

            copy.next = recurse(head.next)
            copy.random = recurse(head.random)
            return copy

        seen = {}
        return recurse(head)

# [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]


four = Node(1)
three = Node(10, four)
two = Node(11, three)
one = Node(13, two)
zero = Node(7, one)

one.random = zero
two.random = four
three.random = two
four.random = zero

Solution().copyRandomList_rec(zero)
