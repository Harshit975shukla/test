t = int(input())
for i in range(t):
    n, m = map(int, (input().split()))
    lcf = m * n
    for j in range(1, min(m, n) + 1):
        if n > m:
            if (n * j % m) == 0:
                lcf = n * j
                break
        else:
            if m * j % n == 0:
                lcf = m * j
                break
    print(lcf)
