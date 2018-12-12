"""
Remove Nth Node From End of List

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        dummy = ListNode(0)
        dummy.next = head

        slow, quick = dummy, dummy

        for i in range(n):
            quick = quick.next

        while quick and quick.next:
            slow = slow.next
            quick = quick.next

        slow.next = slow.next.next

        return dummy.next
