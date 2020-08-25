class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        fast, slow = head.next, head

        while fast and fast.next:
            if slow is fast:
                return True

            fast = fast.next.next
            slow = slow.next

        return False


l4 = ListNode(7)
l3 = ListNode(5, l4)
l2 = ListNode(4, l3)
l1 = ListNode(1, l2)
l4.next = l4

s = Solution()
print(s.hasCycle(l1))
