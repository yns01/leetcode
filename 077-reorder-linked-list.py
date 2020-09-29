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

    def reorderListv2(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current

            current = nxt

        # merge two list
        current_reversed = prev
        current = head

        while current_reversed:
            if not current:
                break

            nxt = current.next
            nxt2 = current_reversed.next
            current.next = current_reversed
            current_reversed.next = nxt

            current_reversed = nxt2
            current = nxt

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

# Solution().print_list(Solution().reorderList(l1))
print("next")
Solution().print_list(Solution().reorderListv2(l1))
