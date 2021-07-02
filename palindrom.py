def palindrom(st, f):
    if len(st) == 1 or len(st) == 0:
        return f
    elif st[0] != st[-1]:
        f = -1
        return palindrom(st[1:-1], f)
    else:
        f = 1
        return palindrom(st[1:-1], f)


def main():
    t = int(input())
    for i in range(t):
        s = input()
        f = 0
        x = (palindrom(s, f))
        if x == -1:
            print("No")
        else:
            print("Yes")


if __name__ == '__main__':
    main()
