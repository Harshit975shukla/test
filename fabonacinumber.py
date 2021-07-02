def fab(n):
    if n == 0 or n == 1:
        return n
    else:
        return fab(n - 1) + fab(n - 2)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(fab(n))


if __name__ == "__main__":
    main()
