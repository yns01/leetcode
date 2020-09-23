class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow has reached middle.
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        current = head
        while stack:
            if current is stack[-1]:
                current = stack.pop()
                break

            nxt = current.next
            end = stack.pop()
            current.next = end
            end.next = nxt
            current = nxt

        current.next = None
        return head

    def print_list(self, head: ListNode):
        if not head:
            print('empty list')

        while head:
            print(head.val)
            head = head.next


l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

Solution().print_list(Solution().reorderList(l1))
