def lowerbound(arr, n, ele):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if ele <= arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low


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
    arr = list(map(int, input().split()))
    t = int(input())
    for i in range(t):
        ele = int(input())
        u = upperbound(arr, len(arr), ele)
        l = lowerbound(arr, len(arr), ele)
        print("upperbound is ", u)
        print("lowerbound is ", l)
if __name__ == '__main__':
    main()