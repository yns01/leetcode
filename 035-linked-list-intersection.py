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

        node_a, node_b = headA, headB

        while headA and headB:
            if headA is headB:
                return headA

            headA = headA.next
            headB = headB.next

        if not headA and not headB:
            return None

        if headA is None:
            # Rewind headA
            headA = node_a

            # Finish iterating over headb and count how much more nodes there are
            diff_count = 0
            while headB:
                diff_count += 1
                headB = headB.next

            # Now reset node b and fast forward it by diff_count nodes.
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

        # At this stage, we will iterate over both lists until we find the intersection
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
