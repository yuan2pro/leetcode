"""
Convert Sorted Array to Binary Search Tree

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    class Solution1(object):
        def sortedArrayToBST(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            tree = [None for i in range(0, 2 * len(nums))]
            l = len(nums)
            if (l == 0):
                return nums
            tree = self.util(nums, 0, l - 1, tree, 0)
            new_len = len(tree) - 1
            while (new_len > 0 and tree[new_len] == None):
                del tree[new_len]
                new_len -= 1
            return tree

        def util(self, nums, s, e, tree, index):
            if (s > e):
                tree[index] = None
            elif (s == e):
                tree[index] = nums[s]
            else:
                mid = s + (e - s) / 2
                midel = nums[mid]
                tree[index] = midel
                self.util(nums, s, mid - 1, tree, 2 * index + 1)
                self.util(nums, mid + 1, e, tree, 2 * index + 2)
            return tree
