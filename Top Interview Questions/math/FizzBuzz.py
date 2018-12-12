"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append("%s" % i)
        return ans

    def fizzBuzz1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = [str(i) for i in range(1, n + 1)]
        l[2::3] = len(l[2::3]) * ["Fizz"]
        l[4::5] = len(l[4::5]) * ["Buzz"]
        l[14::15] = len(l[14::15]) * ["FizzBuzz"]
        return l

if __name__ == '__main__':
    Solution().fizzBuzz1(15)