#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash
        a = {}
        ans = []
        for num in nums1:
            if num not in a.keys():
                a[num] = 1
            else:
                a[num] = a[num] + 1
        for num in nums2:
            if num in a.keys() and a[num] > 0:
                a[num] -= 1
                ans.append(num)
        return ans

        # 集合
        import collections
        a = collections.Counter(nums1)
        b = collections.Counter(nums2)
        c = a & b
        return c.elements()
        
        # 双指针
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        ans = []
        nums1.sort()
        nums2.sort()
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return ans


# @lc code=end
