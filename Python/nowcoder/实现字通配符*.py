if __name__ == "__main__":
    s = input()
    p = input()
    len1, len2 = len(s), len(p)
    dp = [[False] * (len2) for _ in range(len1)]
    for i in range(len1):
        t = i
        for j in range(t, len2):
            if s[i] == p[j]:
                dp[i][j] = True
            elif s[i] == '*':
                if i != len1 - 1 and j != len2-1:
                    while t < len2 and s[i+1] != p[j+1]:
                        dp[i][t] = True
                        t += 1
                else:
                    dp[i][j] = True
    print(dp)
