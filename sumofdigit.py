def sumDigits(no):
    if no == 0:
        return 0
    else:
        x = no % 10
        return x + sumDigits((no // 10))


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sumDigits(n),end="")
        print("")


if __name__ == "__main__":
    main()
