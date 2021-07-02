def palindrom(arr):
    f = 0
    if len(arr) == 0 or len(arr) == 1:
        return f
    elif arr[0] != arr[-1]:
        return -1
    else:
        f = 1
        return palindrom(arr[1:-1])


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        while n != 0:
            a = n % 10
            arr.append(a)
            n = n // 10
        arr.reverse()
        x = (palindrom(arr))
        if x == -1:
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    main()
