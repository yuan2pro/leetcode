# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 21:28
# @Author  : ProYuan

"""
 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        ans = []
        for x in l:
            x = x[::-1]
            ans.append(x)
        return " ".join(ans)

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        for a in range(len(l)):
            l[a] = l[a][::-1]
        return ' '.join(l)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
