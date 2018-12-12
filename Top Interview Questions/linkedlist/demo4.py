"""
Merge Two Sorted Lists

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            new = l1
            l1 = l1.next
        else:
            new = l2
            l2 = l2.next

        head = new
        while True:
            if not l1 and l2:
                new.next = l2
                break
            elif not l2 and l1:
                print(l1.val)
                new.next = l1
                break
            if l1.val <= l2.val:
                new.next = l1
                new = new.next
                l1 = l1.next
            elif l1.val > l2.val:
                new.next = l2
                new = new.next
                l2 = l2.next
        return head

    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def merge(l1, l2):

            root = ListNode(0)

            nd = root

            while (l1 and l2):
                if l1.val < l2.val:
                    nd.next = l1
                    l1 = l1.next
                else:
                    nd.next = l2
                    l2 = l2.next

                nd = nd.next

            if l1:
                nd.next = l1

            else:
                nd.next = l2

            return root.next

        return merge(l1, l2)
