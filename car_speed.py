def main():
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        n1 = k // n
        c = 0
        for j in range(1, n1 + 1):
            if n * j % m == 0:
                c += 1
        print(c)


if __name__ == '__main__':
    main()
