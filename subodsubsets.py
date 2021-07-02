def sumsub(arr, subset, index, s, a):
    print(*subset)
    s = sum(subset)
    a.append(s)
    print(a)
    for i in range(index, len(arr)):
        subset.append(arr[i])
        sumsub(arr, subset, i + 1, s, a)
        subset.pop(-1)
    return a


def main():
    t = int(input())
    for j in range(t):
        n = int(input())
        arr = list(map(int, (input().split())))
        subset = []
        a = []
        x = sumsub(arr, subset, 0, 0, a)
        print(x)
        print(sum(x))
if __name__ == '__main__':
    main()

