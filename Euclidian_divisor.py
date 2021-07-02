def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def main():
    t = int(input())
    while (t !=0):
        m, n = map(int, input().split())
        if (n < m):
            n, m = m, n
        print(gcd(n, m))
        t = t-1


if __name__ == '__main__':
    main()
