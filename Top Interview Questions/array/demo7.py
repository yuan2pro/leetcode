"""
Plus One

"""


class Solution:
    def plusOne(self, digits):
        """
        :type
        digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 9]
    print(digits[-2])
    print(s.plusOne(digits))
