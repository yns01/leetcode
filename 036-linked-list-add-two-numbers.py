# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(n: ListNode):
    while n:
        print(n.val)
        n = n.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l1:
            return None

        result = ListNode()
        last_node = result
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            s %= 10

            last_node.next = ListNode(s)
            last_node = last_node.next

            l1 = l1.next
            l2 = l2.next

        # If we did not finish iterating over one of the two list:
        node = l1 or l2
        while node:
            s = node.val + carry
            carry = s // 10
            s %= 10

            last_node.next = ListNode(s)
            last_node = last_node.next

            node = node.next

        if carry:
            last_node.next = ListNode(carry)

        return result.next


# l5 = ListNode(5)
# l4 = ListNode(4, l5)
l3 = ListNode(3)
l1 = ListNode(4, l3)
l2 = ListNode(2, l1)


m1 = ListNode(1)
m3 = ListNode(3, m1)
m1 = ListNode(7, m3)
m6 = ListNode(6, m1)
m5 = ListNode(5, m6)

# print_list(m5)

print_list(Solution().addTwoNumbers(m5, l2))
