
if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    ans = arr[0]
    t = arr[0]
    for i in range(1, n):
        if t < 0:
            t = 0
        t += arr[i]
        ans = max(ans, t)
    print(ans)
