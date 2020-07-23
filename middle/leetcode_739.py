'''
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，
都是在 [30, 100] 范围内的整数。
'''


class Solution:
    def dailyTemperatures(self, T):
        res = list()
        l = len(T)
        if l == 1:
            return [0]
        for i in range(l):
            for j in range(i + 1, l):
                if T[j] > T[i]:
                    res.append(j - i)
                    break
                if j == l - 1:
                    res.append(0)
        res.append(0)
        return res

    def dailyTemperatures1(self, T):
        l = len(T)
        res = [0] * l
        stack = []
        for i in range(l):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res


print(Solution().dailyTemperatures1([73, 74, 75, 71, 69, 72, 76, 73]))
# [1,1,4,2,1,1,0,0]
