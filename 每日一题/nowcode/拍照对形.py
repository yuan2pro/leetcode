if __name__ == "__main__":
    n = int(input())
    s = input()
    shang = (n - 1) // 3  # 2
    xia = n - 2 * shang  # 3
    for i in range(0, 2*shang, 2):
        print(" "*(i//2)+s[i]+" "*(2*shang-1-i)+s[i+1])
    for i in range(2 * shang, n):
        print(" "*shang+s[i])
