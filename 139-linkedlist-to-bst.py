class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def build_tree(start, end):
            if not start or start == end:
                return None

            mid = find_middle(start, end)
            root = TreeNode(mid.val)

            root.left = build_tree(start, mid)
            root.right = build_tree(mid.next, end)

            return root

        def find_middle(start, end):
            slow, fast = start, start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next

            return slow

        return build_tree(head, None)
