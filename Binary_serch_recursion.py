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


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    res = binary_serch(arr, 0, n + 1, target)
    print(res)


if __name__ == '__main__':
    main()
