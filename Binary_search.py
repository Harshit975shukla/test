def BinarySearch(arr, n, target):
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    res = BinarySearch(arr, n, target)
    print(res)


if __name__ == '__main__':
    main()
