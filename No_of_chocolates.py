def upperbound(arr, n, ele):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if ele >= arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = int(input())
    for i in range(q):
        ele = int(input())
        res = upperbound(arr, n, ele)
        print(res)


if __name__ == '__main__':
    main()
