
if __name__ == "__main__":
    N, L = map(int, input().split(' '))
    for i in range(L, 101):
        if (2*N+i-i**2) % (2*i) == 0:
            start = (2 * N + i - i ** 2) // (2 * i)
            if start < 0:
                print("No")
                exit()
            ans = [str(i) for i in range(start, start + i)]
            print(" ".join(ans))
            exit()
    print("No")
