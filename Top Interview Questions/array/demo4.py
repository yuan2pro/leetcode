"""
Contains Duplicate

"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4]
    s = Solution()
    print(s.containsDuplicate(nums))
