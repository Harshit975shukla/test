def sumOfAP(a, d, n):
    s = (n / 2) * (2 * a + (n - 1) * d)
    return s


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    diff = []
    for j in range(1, n):
        diff.append(arr[j] - arr[j - 1])
    for j in range(1, n - 1):
        if (diff[j] - diff[j - 1]) == 0:
            d = diff[j]
            break
    sn = int(sumOfAP(arr[0], d, n + 1))
    so = sum(arr)
    mis = sn - so
    print(mis)
