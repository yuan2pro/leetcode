"""
Remove Duplicates from Sorted Array

"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

    def main(self):
        nums = [0, 0, 1, 1, 2 ]
        print(self.removeDuplicates(nums))


if __name__ == '__main__':
    s = Solution()
    s.main()
