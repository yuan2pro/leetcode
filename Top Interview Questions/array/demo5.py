"""
Single Number

"""
from functools import reduce
import operator
from collections import Counter


class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber3(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber5(self, nums):
        return reduce(operator.xor, nums)

    def singleNumber6(self, nums):
        c = Counter(nums)
        for key, value in c.items():
            if value == 1:
                return key


if __name__ == '__main__':
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    print(s.singleNumber2(nums))
