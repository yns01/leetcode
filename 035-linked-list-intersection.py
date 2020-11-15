class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def print_list(n: ListNode):
    while n:
        print(n.val)
        n = n.next


class Solution:
    def getIntersectionNodeV1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pa, pb = headA, headB

        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB

            if pb:
                pb = pb.next
            else:
                pb = headA

        return pa

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a_count, b_count = self.count(headA), self.count(headB)

        while a_count > b_count:
            a_count -= 1
            headA = headA.next

        while b_count > a_count:
            b_count -= 1
            headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def count(self, node):
        if not node:
            return 0

        return self.count(node.next) + 1


l5 = ListNode(5)
l4 = ListNode(4, l5)
l8 = ListNode(8, l4)
l1 = ListNode(1)
l40 = ListNode(4, l1)


m1 = ListNode(1, l8)
m6 = ListNode(6, m1)
m5 = ListNode(5, m6)

print(Solution().getIntersectionNode(m5, l1))
