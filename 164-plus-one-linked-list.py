class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        current = head

        result_head = None
        while current:
            node = ListNode(current.val, result_head)
            result_head = node

            current = current.next

        current, prev = result_head, None
        carry = 1
        while current:
            current_digit = current.val + carry
            carry = current_digit // 10
            current_digit %= 10

            current.val = current_digit

            prev = current
            current = current.next

        if carry:
            prev.next = ListNode(1)

        # now we reverse the list
        current, prev = result_head, None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev


def print_list(head: ListNode):
    if not head:
        print('empty list')

    while head:
        print(head.val)
        head = head.next

# Input: (7 -> 2 -> 9 -> 9) + 1
# Output: 7 -> 3 -> 0 -> 0


print_list(Solution().plusOne(
    ListNode(7, ListNode(2, ListNode(9, ListNode(9))))))
