"""
Palindrome Linked List

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        pre = ListNode(0)
        pre.next = slow = head
        fast = slow.next

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp

        if not fast:
            point1 = slow.next
            point2 = pre
        else:
            point1 = slow.next
            point2 = slow
            slow.next = pre

        while point1 and point2:
            if point1.val != point2.val:
                return False
            point1 = point1.next
            point2 = point2.next

        return True

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        reverse = lst[::-1]
        for i in range(len(lst)):
            if lst[i] != reverse[i]:
                return False
        return True
