import math


def sieve(n):
    sieve = [1] * (n+1)
    sieve[1] = 0
    sieve[0] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve[i] == 1:
            for j in range(i*i, n + 1, i):
                sieve[j] = 0
    return sieve


def main():
    n = int(input())
    arr = sieve(n)
    for i in range(len(arr)):
        if arr[i] == 1:
            print(i, end=" ")


if __name__ == '__main__':
    main()
