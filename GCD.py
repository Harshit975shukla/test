from sys import setrecursionlimit

setrecursionlimit(11000)


def factors(n, out):
    if n == 1:
        return out
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                out.append(i)
                n = n // i
                return factors(n, out)


def main():
    t = int(input())
    out1 = [1]
    out2 = [1]
    out = []
    res = 1
    for i in range(t):
        n, p = map(int, (input().split()))
        factors(n, out1)
        factors(p, out2)
        z = min(len(out1), len(out2))
        for j in range(z):
            if z == len(out1):
                if out1[j] in out2:
                    out.append(out1[j])
            else:
                if out2[j] in out1:
                    out.append(out2[j])
        for j in range(len(out)):
            res = res * out[j]
        print(res)
        res = 1
        out = []
        out1 = []
        out2 = []


if __name__ == "__main__":
    main()
