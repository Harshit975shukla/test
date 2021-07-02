from sys import setrecursionlimit

setrecursionlimit(11000)


def pattern(n, out):
    if n <= 0:
        return out
    else:
        n = n - 5
        out.append(n)
        return pattern(n, out)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        out = [n]
        q = pattern(n, out)
        p = out[0:len(out) - 1]
        p.reverse()
        a = q + p
        for i in range(len(a)):
            print(a[i],end=" ")
        print("")


if __name__ == "__main__":
    main()
