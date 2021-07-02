def binary_serch(a, low, high, target):
    if low > high:
        return -1
    mid = low + ((high - low) // 2)
    if a[mid] == target:
        return mid
    if a[mid] < target:
        return binary_serch(a, mid + 1, high, target)
    else:
        return binary_serch(a, low, high - 1, target)


def pair(k, arr, N):
    c = 0
    for i in range(N):
        t = arr[i] - k
        # print(t)
        x = binary_serch(arr, 0, N + 1, t)
        if x != -1:
            # print("@",x)
            c += arr.count(arr[x])
    return c


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = pair(k, arr, n)
    print(res)


if __name__ == '__main__':
    main()
