def capital(N, i, x):
    if i >= x:
        return -1
    elif N[i].isupper():
        return i
    if i < x:
        return capital(N, i + 1, x)


def main():
    t = int(input())
    for j in range(t):
        N = input()
        N = list(N)
        x = len(N)
        y = (capital(N, 0, x))
        print(y)


if __name__ == '__main__':
    main()