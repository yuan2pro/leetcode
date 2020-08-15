
#
#
# @param arr int整型一维数组
# @return int整型
#
'''
链接：https://ac.nowcoder.com/acm/contest/6914/A
来源：牛客网

给你一个含有n个元素的数组arr[i]，
请你告诉牛牛这个数组的中位数大还是平均数大，
如果中位数更大输出1，如果平均数更大输出-1，
如果中位数和平均数相等输出0

'''

class Solution:
    def Answerofjudge(self, arr):
        # write code here
        if not arr:
            return 0
        arr.sort()
        sum_arr = sum(arr)
        n = len(arr)
        ava = sum_arr / n
        if n % 2 != 0:
            mid = arr[n // 2]
        else:
            mid = (arr[n // 2-1] + arr[n // 2]) / 2
        if ava == mid:
            return 0
        elif mid > ava:
            return 1
        else:
            return -1


print(Solution().Answerofjudge([6, 6, 6, 6, 5, 8]))
