class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # General idea: We sum up the digits without taking into account the carries.
        # If the digit is >= 10, during the second pass we modify the value
        # Finally, we reverse the linked list

        n1, n2 = self.get_len(l1), self.get_len(l2)

        prev = None
        while n1 > n2:
            n = ListNode(l1.val)
            n.next = prev
            prev = n

            l1 = l1.next
            n1 -= 1

        while n2 > n1:
            n = ListNode(l2.val)
            n.next = prev
            prev = n

            l2 = l2.next
            n2 -= 1

        # Both pointers are at the same level
        while l1 and l2:
            n = ListNode(l1.val + l2.val)
            n.next = prev
            prev = n

            l1 = l1.next
            l2 = l2.next

        head = prev
        carry = 0
        while prev:
            s = prev.val + carry
            carry = s // 10
            d = s % 10

            prev.val = d

            prev = prev.next

        node, prev = head, None
        while node:
            nxt = node.next

            node.next = prev
            prev = node

            node = nxt

        if carry:
            return ListNode(carry, prev)
        else:
            return prev

    def get_len(self, head):
        count = 0
        while head:
            count += 1
            head = head.next

        return count


def print_list(head: ListNode):
    if not head:
        print('empty list')

    while head:
        print(head.val)
        head = head.next

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


print_list(Solution().addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))),
                                    ListNode(5, ListNode(6, ListNode(4)))))
