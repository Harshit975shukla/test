def findTotalWays(arr, n, i, k):
    if i >= n and k != 0:
        return 0
    if k == 0:
        return 1
    return findTotalWays(arr, n, i + 1, k) + findTotalWays(arr, n, i + 1, k + arr[i]) + findTotalWays(arr, n, i + 1,
                                                                                                      k - arr[i])


def main():
    t = int(input())
    for x in range(t):
        n, k = map(int, (input().split()))
        arr = list(map(int, (input().split())))
        print(findTotalWays(arr, n, 0, k))


if __name__ == '__main__':
    main()

