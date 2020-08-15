class Solution:
    def sovle(self, a, n, m):
        b = a.copy()
        b.sort()
        b.reverse()
        an = b[n-1]
        am = b[m-1]
        ai = a.index(an)
        bi = a.index(am)
        a[ai], a[bi] = a[bi], a[ai]
        return a
