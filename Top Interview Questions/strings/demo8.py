"""
Count and Say

"""
import re
import itertools


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = '1'
        for _ in range(1, n):
            c = 0
            l = None
            r2 = ''
            for i, x in enumerate(r):
                if l is None:
                    c = 1
                    l = x
                elif x == l:
                    c += 1
                else:
                    r2 += '%s%s' % (c, l)
                    c = 1
                    l = x
            if l is not None:
                r2 += '%s%s' % (c, l)
            r = r2
        return r

    def countAndSay1(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

    def countAndSay3(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s


if __name__ == '__main__':
    print(Solution().countAndSay(10))
