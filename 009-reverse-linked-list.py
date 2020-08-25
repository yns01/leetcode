class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev

    def print_list(self, head: ListNode):
        if not head:
            print('empty list')

        while head:
            print(head.val)
            head = head.next


l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2)
l1 = ListNode(1, l2)

s = Solution()
s.print_list(l1)
s.print_list(s.reverseList(l1))
