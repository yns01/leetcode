class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list_head = ListNode(0)
        sorted_list_curr = sorted_list_head

        while l1 and l2:
            sorted_list_node = ListNode()

            if l1.val <= l2.val:
                sorted_list_node.val = l1.val
                l1 = l1.next
            else:
                sorted_list_node.val = l2.val
                l2 = l2.next

            sorted_list_curr.next = sorted_list_node
            sorted_list_curr = sorted_list_curr.next

        while l1:
            n = ListNode(l1.val)
            sorted_list_curr.next = n
            sorted_list_curr = sorted_list_curr.next

            l1 = l1.next

        while l2:
            n = ListNode(l2.val)
            sorted_list_curr.next = n
            sorted_list_curr = sorted_list_curr.next

            l2 = l2.next

        # Return the second node as the first one is a dummy. It helps when inserting a node as we don't have to check
        # whether we're inserting the head or not.
        return sorted_list_head.next

    def print_list(self, head: ListNode):
        if not head:
            print('empty list')

        while head:
            print(head.val)
            head = head.next


l4 = ListNode(7)
l3 = ListNode(5, l4)
l2 = ListNode(4, l3)
l1 = ListNode(1, l2)

m6 = ListNode(15)
m5 = ListNode(13, m6)
m4 = ListNode(12, m5)
m3 = ListNode(5, m4)
m2 = ListNode(2, m3)
m1 = ListNode(0, m2)
s = Solution()
# s.print_list(l1)
# s.print_list(m1)
print("merge")
s.print_list(s.mergeTwoLists(None, m1))
