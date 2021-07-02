from sys import setrecursionlimit

setrecursionlimit(11000)

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(gcd(m, n))


if __name__ == '__main__':
    main()
