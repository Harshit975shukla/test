def count(a, b, c):
    if a == 0 or b == 0:
        return c
    if a > b:
        c = c+(a//b)
        return count(a%b, b, c)
    else:
        c =c+(b//a)
        return count(a, b%a, c)


def main():
    t = int(input())
    for i in range(t):
        p, q = map(int, input().split())
        print(count(p, q, 0))

if __name__ == '__main__':
    main()
