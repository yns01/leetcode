class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def print_list(n: ListNode):
    while n:
        print(n.val)
        n = n.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node_a, node_b = headA, headB
        count = 0
        while headA and headB:
            if headA is headB:
                return headA

            count += 0
            headA = headA.next
            headB = headB.next

        if not headA and not headB:
            return None

        if headA is None:
            headA = node_a

            diff_count = 0
            while headB:
                diff_count += 1
                headB = headB.next

            headB = node_b
            ff = 0
            while ff < diff_count:
                headB = headB.next
                ff += 1

        if headB is None:
            headB = node_b

            diff_count = 0
            while headA:
                diff_count += 1
                headA = headA.next

            headA = node_a
            ff = 0

            while ff < diff_count:
                headA = headA.next
                ff += 1

        while headA and headB:
            if headA is headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None


l5 = ListNode(5)
l4 = ListNode(4, l5)
l8 = ListNode(8, l4)
l1 = ListNode(1)
l40 = ListNode(4, l1)


m1 = ListNode(1, l8)
m6 = ListNode(6, m1)
m5 = ListNode(5, m6)

print(Solution().getIntersectionNode(m5, l1))
