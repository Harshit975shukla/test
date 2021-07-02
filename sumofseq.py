def sumofseq(n, s):
    if n == 1:
        return s
    if n % 2 == 0:
        n = n // 2
        s = s + n
        return sumofseq(n, s)
    else:
        n = (3 * n) + 1
        s = s + n
        return sumofseq(n, s)


def main():
    t = int(input())
    z = (10**9) + 7
    for j in range(t):
        n = int(input())
        s = n
        x = sumofseq(n, s)
        y = x % z
        print(y)


if __name__ == "__main__":
    main()
